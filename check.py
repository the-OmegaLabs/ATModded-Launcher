import os
import spliting
import requests
import www
import json

metadata = {}

def synchonize():
    global metadata
    metadata = {}

    netMetadata = requests.get('https://cdn.stevesuk.eu.org/metadata.json').json()
    for i in netMetadata['metas']:
        metadata[i] = netMetadata['metas'][i].get(www.getCountryCode(), netMetadata['metas'][i]['global'])
        metadata[i]['installed'] = netMetadata['metas'][i]['installed']
        metadata[i]['name'] = netMetadata['metas'][i]['name']

    return metadata

def saveMetadata(metadata):
    with open('local.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(metadata, ensure_ascii=False, indent=4))

def get(meta, update = False):
    if not os.path.exists(meta['installed'][1:]) or update:
        print(f'\n开始补全 \'{meta['name']}\'。')
        if meta['type'] == 'split':
            return spliting.merge_from_url(f'{meta['url']}{meta['path']}', meta['installed'][1:])
        elif meta['type'] == 'subsplit':
            os.makedirs('temp', exist_ok=True)
            for i in range(10):
                if not spliting.merge_from_url(f'{meta['url']}{meta['path']}/subpart{i}', f'temp/part{i}.enc'):
                    return False

            spliting.merge_from_local(f'temp', meta['installed'][1:])

            for i in range(10):
                os.remove(f'temp/part{i}.enc')
            os.removedirs('temp')

        elif meta['type'] == 'single':
            www.download_file(f'{meta['url']}{meta['path']}', meta['installed'][1:])

def update():
    print('正在检查版本更新...')
    global metadata
    with open('local.json') as f:
        localmetadata = json.loads(f.read())

    updates_needed = []

    for dep, dep_data in metadata.items():
        if dep in localmetadata:
            local_version = localmetadata[dep].get('version', '')
            latest_version = dep_data.get('version', '')
            
            if local_version != latest_version:
                updates_needed.append(dep)
        else:
            updates_needed.append(dep)

    if len(updates_needed) == 0:
        print('今日无事可做。')
    else:
        for i in updates_needed:
            get(metadata[i], update=True)

        saveMetadata(metadata)
    
    print('正在检查完整性...')
    for i in metadata:
        get(metadata[i])