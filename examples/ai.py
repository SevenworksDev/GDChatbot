# Register at brainshop.ai if you want to manage your AI more...

from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random
from json import loads
from threading import Thread

un = input("Username: ")
pw = input("Password: ")

def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=random.randint(1,100)

    if(com.startswith("/ai")):
      c=com.split("/ai ")
      try:
          resp = requests.get("http://api.brainshop.ai/get?bid=169422&key=4GCemcdYgy50PlZ2&uid=0&msg="+c[1], headers={'Accept': 'application/json'})
          jsonResp = resp.json()
          airesp = jsonResp["cnt"]
          uploadGJComment(un,pw,f"{u}, {airesp}",perc,level)
          print("Commented...")
      except:
          return

lvl=input("Level ID: ")
while 1:
    try:
        t=Thread(target=commands,args=(lvl,))
        t.start()
        time.sleep(2)
    except:
        print("err")

