import time 
mytime = int(input("Enter Time in Seconds : "))

for x in reversed(range(0,mytime)):
    
    seconds  = x % 60
    minutes = int((x / 60) % 60)
    hours = int((x/3600))
    time.sleep(1)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")
