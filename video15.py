import time
time_stamp = time.time();
print(time_stamp)
local_time = time.ctime(time_stamp)
print(local_time)

time_string = int(time.strftime("%H"))
print(time_string)

if(time_string>=6 and time_string<=12):
  print("Good Morning")
elif(time_string >12 and time_string<=16):
  print("Good Afternoon")
elif(time_string > 16 and time_string<=19 ):
  print("Good Evening")
else:
  print("Good Night")