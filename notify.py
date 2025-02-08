import platform
import os


system = platform.system()

try:
    from plyer import notification
    import plyer.platforms.win.notification
except:
    pass

def toast(title, msg):
    if system == 'Darwin':
        pass 
    if system == 'Windows':
        notification.notify(title, msg)
    if system == 'Linux':
        os.system(f'notifiy-send "{title}" "{msg}" -a "ATCraft Client"')