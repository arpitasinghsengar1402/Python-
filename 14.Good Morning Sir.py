import time
timestamp=time.strftime('%H:%M:%S')
print("CURRENT TIME : " , timestamp)
hour=int(time.strftime('%H'))
print(" HOUR : ",hour)
if(hour>=0 and hour<12):
    print("GOOD MORNING SIR !")
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON SIR !")
if(hour>=17 and hour<0):
    print("GOOD NIGHT SIR !")
minute=int(time.strftime('%M'))
print(" MINUTE : ",minute)
second=int(time.strftime('%S'))
print(" SECOND : ",second)