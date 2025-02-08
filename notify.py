import platform
import os


system = platform.system()

try:
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
except:
    pass

def toast(title, msg):
    if system == 'Darwin':
        pass 
    if system == 'Windows':
        toaster.show_toast(title, msg, duration=7, threaded=True)
    if system == 'Linux':
        os.system(f'notifiy-send "{title}" "{msg}" -a "ATCraft Client"')