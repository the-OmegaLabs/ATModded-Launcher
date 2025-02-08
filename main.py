import os
import check
import threading
import time
import notify

version = 1

def main():
    startTime = time.time()

    metadata = check.synchronize()
    check.saveMetadata(metadata)
    check.update()

    launcher = threading.Thread(target=os.system, args=(f'{os.getcwd()}/game/launcher.exe',))
    launcher.daemon = True
    launcher.start()

    print(f'启动成功，用时 {round(time.time() - startTime, 2)} 秒。')
    notify.toast('ATMod Client 启动成功', '您的启动器已更新至最新版本。')
    

    while launcher.is_alive():
        pass


if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    main()