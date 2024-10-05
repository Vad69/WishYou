import time
hour=int(time.strftime("%H", time.localtime()))
formatted_time = time.strftime("%H:%M:%S", time.localtime())

print("The time is: ",formatted_time)
if(hour>=21):
    print("Good night vardaan sir")
if(hour>=0 and hour<6):
    print("Good night vardaan sir")
if(hour>=6 and hour<12):
    print("Good morning vardaan sir")
if(hour>=12 and hour<17):
    print("Good afternoon vardaan sir")
if(hour>=17 and hour<21):
    print("Good evening vardaan sir")