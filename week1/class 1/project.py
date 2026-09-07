# print("=" * 40," "*15+"MY PROFILE"+" "*15,"=" * 40,"Name : Dhiraj","Age : 20","City : Patna",sep="\n")

# name = 'Dhiraj'
# age = 20
# city = 'Patna'
# pattern = '=' * 40
# space = ' ' * 15

# print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + name, "Age : " + str(age), "City : " + city, sep="\n")



# Name = input("Enter your name: ")
# Age = int(input("Enter your age: "))
# City = input("Enter your city: ")
# Skill = input("Enter your skill: ")
# pattern = '=' * 40
# space = ' ' * 15

# print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + Name, "Age : " + str(Age), "City : " + City, "Skill : " + Skill, sep="\n")


# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# skill = input("Enter your skill: ")
# pattern = '=' * 40
# space = ' ' * 15

# if age <= 0:
#     print("Invalid Age.")

# else:
#     print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + name, "Age : " + str(age), "City : " + city, "Skill : " + skill, sep="\n")



# while True:
#         try:
            
#             age = int(input("Enter your age: "))
#             valid = True
#             if age < 1:
#               raise ValueError ("Invalid Age")
                
#         except:
#             print("Invalid age")
#             valid = False

#         if valid == True:
#             break


# if valid == True:
#     name = input("Enter your name: ")
#     city = input("Enter your city: ")
#     skill = input("Enter your skill: ")
#     pattern = '=' * 40
#     space = ' ' * 15
#     category = None

#     def get_category(age):
#         if age >= 1 and age <= 12:      
#             category = "Child"
    
#         elif age >= 13 and age <= 19:
#             category = "Teenager"
        
#         elif age >= 20 and age <= 59:
#             category = "Adult"
    
#         else:
#             category = "Senior"

#         return category
    
#     print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + name, "Age : " + str(age), "City : " + city, "Skill : " + skill,"Category: "+ get_category(age),  sep="\n")


def get_name():
     while True:
               name = input("Enter your name: ")
               clean_name = name.replace(" ","")
               if clean_name.isalpha():
                    break
               else:
                    print("Only letters  are allowed")
     return name

def get_city():
     while True:
               city = input("Enter your City: ")
               clean_city = city.replace(" ","")
               if clean_city.isalpha():
                    break
               else:
                    print("Only letters  are allowed")
     return city

def get_skill():
     while True:
               skill = input("Enter your skill: ")
               clean_skill = skill.replace(" ","")
               if clean_skill.isalpha():
                    break
               else:
                    print("Only letters  are allowed")
     return skill

def get_age():
    while True:
        try:
            age = int(input("Enter your age:"))
            valid = True
            if age <= 0:
                 raise ValueError
        except:
            print("The age should be an integer and greater than Zero")
            valid = False
        if valid:
             break
    return age

def get_category(age):
         
            if age < 1:
                raise ValueError("Invalid Input") 
            elif age >= 1 and age <= 12:      
                return "Child"
        
            elif age >= 13 and age <= 19:
                return "Teenager"
            
            elif age >= 20 and age <= 59:
                return "Adult"
        
            else:
                return "Senior"

def create_profile():
      name = get_name()
      age = get_age()
      city = get_city()
      skill = get_skill()
      category = get_category(age)

      profile_data = {
            "Name":name,
            "Age":age,
            "City":city,
            "Skill":skill,
            "category":category
      }
      return profile_data
      
def show_profile(profile_data):
      pattern = '=' * 40
      space = ' ' * 15
      print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + profile_data['Name'], "Age : " + str(profile_data['Age']), "City : " + profile_data['City'], "Skill : " + profile_data['Skill'],"Category: "+ profile_data['category'],  sep="\n")




def main():
      print("="*40 ,"PROFILE APP","="*40)
      profile_data = None
      while True:
            print("1. Create Profile","2. veiw Profile","3. Update Profile","4. Delete Profile","5. Exit",sep = "\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                profile_data = create_profile()
                print("Created successfully")

                
            elif choice == "2":
                  if profile_data is not None:
                        show_profile(profile_data)
                  else:
                        print("Profile Not Found.......")
            elif choice == "3":
                  if profile_data is not None:
                        print("Enter what youn want to Update...","1. Name","2. Age", "3. City","4. skill","5. Back")
                        upd_choice = input("Enter your choice...")
                        if upd_choice == "1":
                              new_name = get_name()
                              name = new_name
                              print("Profile Updated Successfully")

                        elif upd_choice == "2":
                              new_age = get_age()
                              new_cate = get_category(new_age)
                              age = new_age
                              category = new_cate
                              print("Profile Updated Successfully")

                        elif upd_choice == "3":
                              new_city = get_city()
                              city = new_city

                        elif upd_choice == "4":
                              new_skill = get_skill()
                              skill = new_skill
                              print("Profile Updated Successfully")

                        elif upd_choice == "5":
                              continue
                  else:
                        print("No Existing Profile Found.......")

            elif choice == "4":
                  if profile_data is not None:
                        agreement = input("Are you sure ? (Y/N): ")
                        if agreement == "Y":
                              profile_data = None
                              print("profile deleted Successfully.....")
                  else:
                    print("No Profile found...")
                  
            elif choice == "5" :     
                  print("Good Bye......!")
                  break
            else:
                print("Enter valid Input")
    
main()
    