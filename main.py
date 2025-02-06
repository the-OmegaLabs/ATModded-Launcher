import os
import check
import threading
import time
import notifiy

version = 1

def main():
    startTime = time.time()
    os.makedirs('game', exist_ok=True)
    os.makedirs('runtime', exist_ok=True)

    metadata = check.synchonize()
    if not os.path.exists('local.json'):
        check.saveMetadata(metadata)

    check.update()

    launcher = threading.Thread(target=os.system, args=(f'{os.getcwd()}/game/launcher.exe',))
    launcher.daemon = True
    launcher.start()

    print(f'启动成功，用时 {round(time.time() - startTime, 2)} 秒。')
    notifiy.toast('ATMod Client 启动成功', '您的启动器已更新至最新版本。')
    

    while launcher.is_alive():
        pass


if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    main()