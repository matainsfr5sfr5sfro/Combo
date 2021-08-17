   import os,sys,random

logo = """
 ▄████▄   ▒█████   ███▄ ▄███▓ ▄▄▄▄    ▒█████  
▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▒██▒  ██▒
▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██░  ██▒
▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒██░█▀  ▒██   ██░
▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░ ████▓▒░
░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░ ▒░▒░▒░ 
  ░  ▒     ░ ▒ ▒░ ░  ░      ░▒░▒   ░   ░ ▒ ▒░ 
░        ░ ░ ░ ▒  ░      ░    ░    ░ ░ ░ ░ ▒  
░ ░          ░ ░         ░    ░          ░ ░  
░                                  ░          
"""
print(logo)
print("\033[1;92mFile Save matin.txt")
print("1- Combo Maker")
input("halbzhera : ")
for iii in range(100000):
    r1=random.randint(1000000, 9999999)
    r2=random.randint(1000000, 9999999)
    r3=random.randint(1000000, 9999999)
    r4=random.randint(1000000, 9999999)
    r5=random.randint(1000000, 9999999)
    sys.stdout=open("matin.txt","a")
    print("0750"+str(r1)+":0750"+str(r1))
    print("0750"+str(r2)+":0750"+str(r2)) 
