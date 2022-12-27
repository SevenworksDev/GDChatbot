from distutils.command.upload import upload
from bettercomm import uploadGJComment
import time,requests,random
from json import loads
from threading import Thread

# Profanity + Bypass Filter
# from better_profanity import profanity

print("LevelBot by Harm/Sevenworks")
un = input("Username: ")
pw = input("Password: ")

def commands(level):
    url=f"http://gdbrowser.com/api/comments/{level}?count=1"
    r=loads(requests.get(url).text)[0]
    u=r['username']
    com=r['content']
    perc=random.randint(1,100)

    if(com.startswith("/cmd1")):
      try:
          uploadGJComment(un,pw,f"Hello, {u}! Thanks for using /cmd1!",perc,level)
          print("{u} executed /cmd1")
      except:
          return
    elif(com.startswith("/cmd2")):
        try:
            uploadGJComment(un,pw,f"@{u}, Thanks for using /cmd2!",perc,level)
            print("{u} executed /cmd2")
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

