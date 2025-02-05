import time
import requests
import sys
import os

def convert_size(size_bytes):
    units = ['B', 'KB', 'MB', 'GB']
    unit_index = 0
    while size_bytes >= 1024 and unit_index < len(units)-1:
        size_bytes /= 1024.0
        unit_index += 1
    return f"{size_bytes:.2f} {units[unit_index]}"

def print_progress(downloaded, total):
    bar_width = 50 
    percent = downloaded / total if total != 0 else 0
    filled = int(bar_width * percent)
    bar = '█' * filled + '-' * (bar_width - filled)
    downloaded_str = convert_size(downloaded)
    total_str = convert_size(total) if total != 0 else "?"
    sys.stdout.write(f"\r[{bar}] {percent:.1%}  {downloaded_str} / {total_str}")
    sys.stdout.flush()

def getCountryCode():
    return requests.get('http://ip-api.com/json/?fields=17031170').json()['countryCode'] # get countryCode, mobile, proxy, hosting
    

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  
        
        total_size = int(response.headers.get('content-length', 0))

        downloaded = 0
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                downloaded += len(chunk)
                if total_size != 0:
                    print_progress(downloaded, total_size)
                else:
                    sys.stdout.write(f"\rDownloaded: {convert_size(downloaded)}    ")
                    sys.stdout.flush()

        print('下载成功！')
        
    except requests.exceptions.RequestException as e:
        print(f"\n下载失败：{e}")
