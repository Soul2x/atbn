comId="78670965"
import os
os.system("pip install websocket-client amino.py json_minify")
os.system("clear") 
import amino
import random,names 
from amino import Client
from amino import SubClient
from amino.lib.util.exceptions import *
from concurrent.futures import ThreadPoolExecutor
from fancy_text import fancy
from os import path
import platform,socket,re,uuid,json,requests
print("Antiban Id In community\nMade By ᴠɪᴄɪᴏᴜꜱ")
THIS_FOLDER = path.dirname(path.abspath(__file__))
emailfile=path.join(THIS_FOLDER,"accounts.json")
dictlist=[]
content = open("antiban.txt").read()
with open(emailfile) as f:
    dictlist = json.load(f)
client=amino.Client()

def threadit(acc : dict):
    email=acc["email"]
    password=acc["password"]
    device=acc["device"]
    client=amino.Client(device)
    try:
        client.login(email=email,password=password)
    except:
        pass
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    print(f"logged into {email}")
    try:
        client.join_community(comId=comId)
        sub=amino.SubClient(comId=comId,profile=client.profile)
        sub.edit_profile(content=content)
        print("Off This Id Antiban" + email)
    except:
    	pass
    
    
  
def main():
    print(f"{len(dictlist)} accounts loaded")
    for amp in dictlist:
        threadit(amp)
    print("all accounts have been modified")
        	         
if __name__ == '__main__':
	main()
