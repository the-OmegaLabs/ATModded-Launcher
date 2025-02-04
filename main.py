import os
import check

version = 'b1'

def checkDepend():
    os.makedirs('game', exist_ok=True)
    os.makedirs('runtime', exist_ok=True)

    status = {}
    print('正在检查依赖 \"pcl\"')
    status['pcl'] = check.checkLauncher()
    print('正在检查依赖 \"OpenJDK\"')
    status['openjdk'] = check.checkOpenJDK()

    return status


def main():
    print('正在检查并补全依赖...')
    dependStatus = checkDepend()
    for i in dependStatus:
        print(f"依赖 {i}: {dependStatus[i]}")



if __name__ == '__main__':
    main()