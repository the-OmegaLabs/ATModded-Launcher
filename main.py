import os
import check
version = 1

def main():
    os.makedirs('game', exist_ok=True)
    os.makedirs('runtime', exist_ok=True)

    metadata = check.synchonize()
    if not os.path.exists('local.json'):
        check.saveMetadata(metadata)

    check.update()



if __name__ == '__main__':
    print(f'ATMod Client build-{version}')
    main()