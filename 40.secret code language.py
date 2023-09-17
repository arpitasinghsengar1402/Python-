choice = input("To Code Message Press 1 To Decode Message Press 2: ")
if(choice == "1"):
  msg = input("Enter The Message To Be Coded: ")
  if(len(msg) > 3):
    encode1 = msg[1:] + msg[0]
    encode2 = msg[2:5] + encode1 + msg[0:3]
    print(encode2)
  
  else:
   print(msg[::-1])
  

elif(choice == "2"):
   msg =  input("Enter The Code: ")
   if(len(msg) >3):
    step1 = msg[:-3]
    step2 = step1[3:]
    step3 =step2[-1] + step2[:-1]
    print(step3)

   else:
    print(msg[::-1])
    
else:
    print("Invalid Operation")