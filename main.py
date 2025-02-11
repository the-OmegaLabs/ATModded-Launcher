import os
import zipfile
import check
import threading
import time
import notify
import platform
from win32api import SetConsoleTitle

version = '2.hotfix+1'
SetConsoleTitle(f'ATMod Launcher build-{version} | 日志界面')
launchdir = os.getcwd()

def launch():
    system = platform.system()

    if system == 'Windows':
        os.system(f'{launchdir}/runtime/jdk-17.0.14+7/bin/javaw -jar ./launcher.jar')

def main():
    startTime = time.time()

    metadata = check.synchronize()
    print('正在检查更新...')
    check.saveMetadata(metadata)
    check.upgrade(check.update())

    if not os.path.exists('./runtime/jdk-17.0.14+7/'):
        try:
            with zipfile.ZipFile('./runtime/openjdk.zip', 'r') as zip_ref:
                zip_ref.extractall('./runtime')
        except:
            os.remove('./runtime/openjdk.zip')
            check.upgrade(check.update())
            notify.toast('ATMod Client 无法启动', '请重启启动器。')

    os.chdir('game')
    launcher = threading.Thread(target=launch, daemon=True)
    launcher.start()

    print(f'\n启动成功，用时 {round(time.time() - startTime, 2)} 秒。')
    notify.toast('ATMod Client 启动成功', '您的启动器已更新至最新版本。')
    
    os.chdir('..')
    updatenoticed = False
    while launcher.is_alive():
        remote = check.update(update=True)
        if len(remote) != 0 and not updatenoticed:
            notify.toast('ATMod Client 需要更新', '检测到新版本发布，重启启动器以安装更新。')
            updatenoticed = True
        time.sleep(10)
        


if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    main()