import base64
import os
import time
import requests
import binascii
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def encode_file(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
    
def decode_file(b64_string, output_path):
    with open(output_path, 'wb') as f:
        f.write(base64.b64decode(b64_string.encode('utf-8')))

def split_and_save(b64_string, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    total_len = len(b64_string)
    chunk_size = total_len // 10
    remainder = total_len % 10
    
    chunks = []
    start = 0
    for i in range(10):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunks.append(b64_string[start:end])
        start = end
    
    for i, chunk in enumerate(chunks):
        chunk_path = os.path.join(output_dir, f'part{i}.enc')
        with open(chunk_path, 'w') as f:
            f.write(chunk)

def merge_from_local(parts_dir, output_path):
    chunks = []
    
    for i in range(10):
        part_path = os.path.join(parts_dir, f'part{i}.enc')
        with open(part_path, 'r') as f:
            chunks.append(f.read())
    
    combined = ''.join(chunks)
    try:
        base64.b64decode(combined, validate=True)
    except binascii.Error:
        return False
    
    decode_file(combined, output_path)

    return True

def download_chunk(i, base_url, save_dir):
    try:
        url = f"{base_url}/part{i}.enc"
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        save_path = os.path.join(save_dir, f'part{i}.enc')
        with open(save_path, 'wb') as f:
            f.write(response.content)
            
        sys.stdout.write(f'██')
        sys.stdout.flush()
        return True
    except Exception as e:
        print(f'\n补全依赖 {base_url.split("/")[-1]} 的第 {i} 块时出现错误：{e}。')
        exit(False)

def cleanup(foldername):
    oldPath = os.getcwd()
    os.chdir(foldername)
    for i in os.listdir():
        os.remove(i)

    os.chdir(oldPath)
    os.removedirs(foldername)

def merge_from_url(base_url, output_path):
    timestamp = int(time.time())
    temp_dir = os.path.join(os.getcwd(), f'download_{timestamp}')
    os.makedirs(temp_dir, exist_ok=True)
    
    sys.stdout.write(f'正在补全依赖 {base_url.split("/")[-1]}: [')
    sys.stdout.flush()
    success = True
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(download_chunk, i, base_url, temp_dir) 
                  for i in range(10)]
        
        for future in as_completed(futures):
            if not future.result():
                success = False

    print(']')
    if success:
        merge_from_local(temp_dir, output_path)
        cleanup(temp_dir)
        return True
    else:
        cleanup(temp_dir)
        return False
    