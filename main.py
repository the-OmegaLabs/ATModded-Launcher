import os
import sys

import check
import threading
import time
import notify
from win32api import SetConsoleTitle

version = 1
SetConsoleTitle(f'ATMod Launcher build-{version} | 日志')

class Logger(object):
    def __init__(self, filename='log.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.terminal.flush()  # 不启动缓冲,实时输出
        self.log.flush()

    def flush(self):
        pass

def main():
    startTime = time.time()

    metadata = check.synchronize()
    check.saveMetadata(metadata)
    check.update()

    launcher = threading.Thread(target=os.system, args=(f'{os.getcwd()}/game/launcher.exe',))
    launcher.daemon = True
    launcher.start()

    print(f'\n启动成功，用时 {round(time.time() - startTime, 2)} 秒。')
    notify.toast('ATMod Client 启动成功', '您的启动器已更新至最新版本。')
    

    while launcher.is_alive():
        pass


if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    sys.stdout = Logger('./dump.log', sys.stdout)
    sys.stderr = Logger(f'./dump.log', sys.stderr)
    main()