password = input("Enter an 8 character password:")
if len(password) > 8:
	print ("must be eight characters")
if len(password) < 8:
	print("must be 8 characters")
password = str(password)

strength = 0

if "a" in password or "b" in password or "c" in password or "d" in password or "e" in password or "f" in password or "g" in password or "h" in password or "i" in password or "j" in password or "k" in password or "l" in password or "m" in password or "n" in password or "o" in password or "p" in password or "q" in password or "r" in password or "s" in password or "t" in password or "u" in password or "v" in password or "w" in password or "x" in password or "y" in password or "z" in password:
	strength = strength + 1
if "A" in password or "B" in password or "C" in password or "D" in password or "E" in password or "F" in password or "G" in password or "H" in password or "I" in password or "J" in password or "K" in password or "L" in password or "M" in password or "N" in password or "O" in password or "P" in password or "Q" in password or "R" in password or "S" in password or "T" in password or "U" in password or "V" in password or "W" in password or "X" in password or "Y" in password or "Z" in password:
	strength = strength + 1
if "1" in password or "2" in password or "3" in password or "4" in password or "5" in password or "6" in password or "7" in password or "8" in password or "9" in password or "0" in password:
	strength = strength + 1
if "!" in password or "@" in password or "#" in password or "$" in password or "%" in password or "^" in password or "&" in password or "*" in password or "(" in password or ")" in password:
	strength = strength + 1
if strength == 1:
	print("weak")
if strength == 2:
	print("ok")
if strength == 3:
	print("strong")
if strength == 4:
	print("very strong")
