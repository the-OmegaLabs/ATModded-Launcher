from pColor import pColor
import time
def log(type, msg):
    if type == 'info':
        print(f'{pColor.BLUE}({time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})[INFO]{pColor.RESET}{msg}')
    elif type == 'warn':
        print(f'{pColor.YELLOW}({time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})[WARN]{pColor.RESET}{msg}')
    elif type == 'error':
        print(f'{pColor.RED}({time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})[WARN]{pColor.RESET}{msg}')
    else:
        print(f'{pColor.GREEN}({time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())})[DONE]{pColor.RESET}{msg}')