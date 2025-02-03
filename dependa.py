import requests
import os
import encryptlib

baseURL = 'https://cdn.stevesuk.eu.org/pcl2/'

os.makedirs('PCL2-CE', exist_ok=True)
os.chdir('PCL2-CE')

for i in range(10):
    response = requests.get(f'{baseURL}/pcl/parts{i}.enc')
    print(f'[{i * 10}%] Processing depend \"PCL2-CE\"...')
    with open(f'parts{i}.enc', 'wb') as f:
        f.write(response.content)


os.chdir('..')


encryptlib.exportFromParts('PCL2-CE', 'pcl2.exe')