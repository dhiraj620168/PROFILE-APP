# Level - Easy
print("Hello")
print(10)
print("Hello","Python")#comma puts a blank space between strings.
print(5+3)
print("3" + "5")
print("Hi", end = ' ')#Hi There
print("There")
print("A","B","C",sep ="-")
print("Hello\nWorld")
print(10*2)
print(10/2)#always returns a float value
print("\n" * 5)


# Leve2 - Getting Tricky
print("A",end = "")
print("B")
print("Age:",20)
print("Age: " + str(20))
print("A\tB")
print("A\\B")

#Level3 - Interview Traps
x = print("Hello")#Hello -> print() shows the output on console but returns None. 
print(x)#So, x will be None.

print(print("Hello"))#Hello -> print() shows the output on console but returns None.

print("A",print("Hello"),"B")#Hello -> print() shows the output on console but returns None.

print("A",end = " ")
print("A",end = " ")
print("A",end = " ")

print("A",end = "\n\n")
print("A")

print("A","B","C",sep = "\n",end = "!\n")

print(1, 2, 3, 4, 5,sep = "+",end = " = ")
print(1+2+3+4+5)

print("Python",sep = "-",end = " \n")

# Level5 - Very Tricky
print(10 + 20, "30")
print("10"*2 + "5")
print(2*3+4)
print(2*(3+4))
print(True + True)
print(True + False)
print(False + False)
print(True,True,flush=True)
print("A" *2 + "B" * 3 + "C" * 4)
print("A" + "B"*3)
print("A",print("B",end = ""),"C",sep = "-")