import datetime,time,webbrowser,random

#use military time
alarm = input("Set Alarm: (Format: HH:MM)\n>> ")

today = datetime.datetime.today()

#convert hours to minutes and add to minutes, then convert to seconds
sleepDuration = ( (int(alarm[0:2])-(today.hour))*60 +
                  (int(alarm[3:5])-(today.minute)) )*60

time.sleep(sleepDuration)

print("ALARM!!!")

#wait till the alarm goes off to open the file and video
with open("youtube.txt") as file:
    youtubeURL = file.readlines()
    #open a random url containing a youtube video
    webbrowser.open( random.choice(youtubeURL) )
