@echo off


pyinstaller --onefile --optimize 2 --hide-console minimize-early -i AC_Header_Gen4.ico --uac-admin main.py