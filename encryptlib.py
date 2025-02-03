import base64
import os

def encodeFile(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')
    
def decodeFile(string, path):
    with open(path, 'wb') as f:
        f.write(base64.b64decode(string.encode('utf-8')))

def makePartAndSave(string, path):
    oldPath = os.getcwd()
    chunk_size = len(string) // 10
    remainder = len(string) % 10
    chunks = []
    start = 0
    for i in range(10):
        end = start + chunk_size + (1 if i < remainder else 0)
        chunks.append(string[start:end])
        start = end
    
    os.makedirs(path, exist_ok=True)
    os.chdir(path)

    for i in range(len(chunks)):
        with open(f'part{i}.enc', 'w') as f:
            f.write(chunks[i])

    os.chdir(oldPath)
        

def exportFromParts(path, target):
    oldPath = os.getcwd()
    os.chdir(path)

    chunks = []

    for i in range(10):
        with open(f'parts{i}.enc') as f:
            chunks.append(f.read())

    string = ''.join(chunks)

    os.chdir(oldPath)
    decodeFile(string, target)