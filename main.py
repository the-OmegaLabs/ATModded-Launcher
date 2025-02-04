import os
import check

version = 'b1'

def checkDepend():
    print('正在检查依赖...')
    os.makedirs('game', exist_ok=True)
    os.makedirs('runtime', exist_ok=True)

    print(f'正在检查 launcher...', end='')
    check.checkLauncher()
    print(f'正在检查 openjdk...', end='')
    check.checkOpenJDK()




def main():
    checkDepend()



if __name__ == '__main__':
    print(f'ATMod Client {version}')
    main()