# It is a new string formatting mechanism introduced by the PEP 498. It is also known as Literal String Interpolation or more commonly as F-strings (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

# When we prefix the string with the letter 'f', the string becomes the f-string itself. The f-string can be formatted in much same as the str.format() method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

country=input("ENTER COUNTRY NAME :")
name=input("ENTER YOUR NAME: ")

print(f"Hey my name is {name } and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

print(f"{2 * 30}")