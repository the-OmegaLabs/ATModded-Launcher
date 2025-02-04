import os
import spliting

def checkLauncher():
    if not os.path.exists('game/launcher.exe'):
        return spliting.merge_from_url('https://cdn.stevesuk.eu.org/pcl', 'game/launcher.exe')

def checkOpenJDK():
    if not os.path.exists('runtime/openjdk.zip'):
        for i in range(10):
            if not spliting.merge_from_url(f'https://cdn.stevesuk.eu.org/openjdk/subpart{i}', f'runtime/part{i}.enc'):
                return False

        spliting.merge_from_local(f'runtime', f'runtime/openjdk.zip')

        for i in range(10):
            os.remove(f'runtime/part{i}.enc')