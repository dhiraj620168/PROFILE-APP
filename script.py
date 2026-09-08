# name = 'Rahul'
# age =21
# city = 'New Delhi'
# skill = 'Python'
# equal = '=' * 40
# mul = ''
# mul =" "*15
# center = mul + "MY PROFILE"

# print(equal,
# center,
# equal, '''
# Name:  ''', name, '''
# Age:   ''', age, '''
# City:  ''', city,'''
# Skill: ''',skill,sep="\n",)

# print()

# 




# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# future_view = 15
# print("Hello", name, future_view, "yrs later you will be", age + future_view, "yrs old")

# age = int(input("Enter your age: "))
# print("Age is greater than 18 -> ", age > 18) 
# print("Age is less than 18 -> ", age < 18)

# print("dhiraj Kumar".replace(" ",""))
# def get_name():
#      while True:
#                name = input("Enter your name: ")
#                print(repr(name))
#                print(name.replace(" ",""))
#                clean_name = name.replace(" ","")
#                if clean_name.isalpha():
#                     break
#                else:
#                     print("Only letters  are allowed")
#      return name
# print(get_name())



# def test(x):
#     print("Before",x)
#     x += 1
#     print("inside",x)

# x=100
# test(x)
# print("outside",x)

l = [{"name":4,"Age":24},{"name":4,"Age":23},]
l.sort(key = lambda i: i ["Age"])
print(l)
