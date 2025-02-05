import os
import check

version = 1

def main():
    os.makedirs('game', exist_ok=True)
    os.makedirs('runtime', exist_ok=True)

    check.saveMetadata(check.synchonize())
    check.update()



if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    main()