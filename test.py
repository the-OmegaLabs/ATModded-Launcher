import os
import spliting
from concurrent.futures import ThreadPoolExecutor

os.chdir('openjdk')

for i in range(10):
    spliting.merge_from_local(f'subpart{i}', f'part{i}.enc')

os.chdir('..')

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(spliting.merge_from_local, f'part{i}.encf', f'part{i}.enc') 
                for i in range(10)]

spliting.merge_from_local('openjdk', 'zulu.zip')