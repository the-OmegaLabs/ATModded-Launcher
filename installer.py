import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import platform
import shutil
import ctypes
import winshell

CLIENT_VERSION = 'b1'
INSTALLER_VERSION = 1.1
INSTALLATION_PATH = 'C:/Program Files/ATMod'
if platform.system() == "Linux":
	INSTALLATION_PATH = "/opt/ATGuns"
	DEFAULT_PATH = "/opt"
else:
	DEFAULT_PATH = "C:/Program Files/"

def isAdmin():
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False


def create_shortcut(bin_path: str, name: str, desc: str):
	'''
	skid from https://blog.csdn.net/qq_45769063/article/details/124707948
	:param bin_path: exe路径
	:param name: 需要创建快捷方式的路径
	:param desc: 描述，鼠标放在图标上面会有提示
	:return:
	'''
	print(winshell.desktop())
	shortcut =  name + ".lnk"
	winshell.CreateShortcut(
		Path=shortcut,
		Target=bin_path,
		Icon=(bin_path, 0),
		Description=desc
	)
	return True

def main():
	global window
	window = tk.Tk()
	window.title('ATMod Client Installer')
	center_window(window, 510, 400)
	window.resizable(False, False)
	ttk.Separator(window).pack(fill=tk.X)
	titleLabel = ttk.Label(window, text='欢迎使用 ATMod Client Installer', font=('Arial', 20))
	titleLabel.place(x=20,y=30)
	descriptionLabel = ttk.Label(window, text=f'请确认以下信息：\nATMod Client build-{CLIENT_VERSION} \nInstaller build-{INSTALLER_VERSION}\n进行安装代表您同意我们的用户许可协议：http://shorturl.asia/x4vDj', font=('Arial', 10))
	descriptionLabel.place(x=20,y=100)
	nextstep = ttk.Button(window, text='下一步', command=lambda: step2())
	nextstep.place(x=320,y=360)
	exitBtn = ttk.Button(window, text='退出', command=lambda: exit())
	exitBtn.place(x=410,y=360)
	window.mainloop()

def step2():
	global window2,pathSelector
	window.destroy()
	window2 = tk.Tk()
	window2.title('ATMod Client Installer')
	center_window(window2, 510, 400)
	window2.resizable(False, False)
	ttk.Separator(window2).pack(fill=tk.X)
	titleLabel = ttk.Label(window2, text='请选择您的安装路径', font=('Arial', 20))
	titleLabel.place(x=20,y=30)
	pathSelector = ttk.Entry(window2, width=50)
	pathSelector.place(x=20,y=100)
	pathSelector.insert(0, INSTALLATION_PATH)
	pathselectBtn = ttk.Button(window2, text='选择路径', command=lambda: handlePath())
	pathselectBtn.place(x=410,y=100)

	nextstep = ttk.Button(window2, text='安装', command=lambda: installToPath(pathSelector.get()))
	nextstep.place(x=320,y=360)
	exitBtn = ttk.Button(window2, text='上一步', command=lambda: (window2.destroy(), main()))
	exitBtn.place(x=410,y=360)
	window2.mainloop()

def installToPath(path):
	os.makedirs(path, exist_ok=True)
	shutil.copy("./installation_binaries/buildep.exe", path)
	if create_shortcut(path + "/buildep.exe", winshell.desktop() + "/ATMod", "启动ATMod Client"):
		messagebox.showinfo("ATMod Client Installer", "安装成功")
	else:
		messagebox.showerror("ATMod Client Installer", "安装失败，请上报程序维护者")


def handlePath():
	global pathSelector
	pathSelector.delete(first=0, last=len(pathSelector.get()))
	pathSelector.insert(0, filedialog.askdirectory(initialdir="C:/Program Files/"))

def center_window(root, width, height):
	screenwidth = root.winfo_screenwidth()
	screenheight = root.winfo_screenheight()
	size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
	root.geometry(size)

if __name__ == '__main__':
	if not isAdmin():
		messagebox.showerror("ATMod Client Installer", "请以管理员身份运行此安装程序")
		exit()

	main()
