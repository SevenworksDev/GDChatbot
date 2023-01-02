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
    randResp=["Yes", "No"]

    if(com.startswith("/yesOrNo")):
      try:
          xD = random.choice(randResp)
          uploadGJComment(un,pw,f"@{u}, {xD}",perc,level)
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

