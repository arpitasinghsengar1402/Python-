# strings are immutable 
a="!!!Arpita Singh Sengar!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())

print(a.rstrip("!"))

print(a.replace("Arpita", "Doll"))

print(a.split(" "))

b="hcst college"
print(b.capitalize())

str1="WELCOMEtotheconsole"
print(len(str1))
print(len(str1.center(50)))
print(str1.endswith(" !!!"))
print(str1.endswith("to",4,10))
print(str1.find("to"))
print(str1.isalnum())

str="helloworld"
print(str)
print(str.islower())
print(str1.isprintable())
str2=" "
print(str2.isspace())
print(str1.istitle())
print(str1.startswith("Python"))
print(str1.swapcase())
print(str1.title())