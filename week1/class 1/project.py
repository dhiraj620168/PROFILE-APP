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



def create_profile(profile_id):
      name = get_name()
      age = get_age()
      city = get_city()
      skill = get_skill()
      category = get_category(age)

      profiles = {
            "User ID":profile_id,
            "Name":name,
            "Age":age,
            "City":city,
            "Skill":skill,
            "category":category

      }
      print("Profile Created Successfully...")
      return profiles
      
def show_profile(profiles):
      if profiles:
            pattern = '=' * 40
            space = ' ' * 15
            for profile_index,profile in enumerate(profiles):
                  print(pattern, space + "PROFILE : " + str(profile_index + 1) + space, pattern,"User ID :" + str(profile["User ID"]),"Name : " + profile['Name'], "Age : " + str(profile['Age']), "City : " + profile['City'], "Skill : " + profile['Skill'],"Category: "+ profile['category'],  sep="\n")
      else:
            print("Profile is not Available...")

def delete(profiles):
      if profiles:
            id_to_delete = int(input("Enter User ID to Delete:"))
            for user in profiles:
                  if user["User ID"] == id_to_delete:
                        confirm = input("Do you want to delete : (Y/N)")
                        if confirm == "Y":
                              profiles.remove(user)
                              print("Profile Delated Successfully...!")
                        break

                 
            else:
                print("User ID Not Found.....")
      return profiles

def update(profiles):
      if profiles:
                        id_to_update = int(input("Enter User ID to update:"))
                        for user in profiles:
                              if user["User ID"] == id_to_update:
                                    print("Enter what youn want to Update...","1. Name","2. Age", "3. City","4. skill")
                                    upd_choice = input("Enter your choice...")
                                    if upd_choice == "1":
                                                new_name = get_name()
                                                user["Name"] = new_name
                                                print("Profile Updated Successfully")
                                                                                                                                  
                                    elif upd_choice == "2":
                                                new_age = get_age()
                                                new_cate = get_category(new_age)
                                                user["Age"] = new_age
                                                user["category"] = new_cate
                                                print("Profile Updated Successfully")                            
                                    elif upd_choice == "3":
                                                new_city = get_city()
                                                user["City"] = new_city
                                                print("Profile Updated Successfully")
                                                                                                       
                                    elif upd_choice == "4":
                                                new_skill = get_skill()
                                                user["Skill"] = new_skill
                                                print("Profile Updated Successfully")
                                                                        
                                    else:
                                          print("Invalid Input...")
                                    break
                        else:
                              print("User ID not found....")                   

      else:
         print("No Existing Profile Found.......")

def search_profile(profiles):
        print("1. search By Id..","2. search By Name..","3. Search by City..","4. Search by skill",sep="\n")
        choice = input("Enter your choice..")
        found = False
        if choice == "1":
                  search_id = int(input("Enter user ID >>> "))
                  for user in profiles:         
                        if user["User ID"] == search_id:
                              # print("inside loop")
                              show_profile([user])
                        break
                  else:
                        print("No match found..")
        elif choice == "2":
                  search_name = get_name()
                  for user in profiles:
                        if search_name.lower() in user["Name"].lower():
                              show_profile([user])
                              found = True
                  if not found:
                        print("No match found..")
                 

        elif choice == "3":
              search_city = get_city()
              for user in profiles:
                    if  search_city.lower() in user["City"].lower():
                           show_profile([user])
                           found = True
              if not found:
                        print("No match found..")

        elif choice == "4":
              search_skill = get_skill()
              for user in profiles:
                    if search_skill.lower() in user["Skill"]:
                          show_profile([user])
                          found = True
              if not found:
                        print("No match found..")
              

def sort_profile(profiles):
      print("1. sort by Age","2. sort by Name","3. sort in descending age","4. sort by name in descending order",sep = "\n")
      choice = input("Enter your choice..>> ")
      if choice == "1":
            profiles.sort(key = lambda profile: profile["Age"])
      elif choice == "2":
            profiles.sort(key = lambda profile:profile["Name"])
      elif choice == "3":
            profiles.sort(key = lambda profile: profile["Age"],reverse = True)
      elif choice == "4":
            profiles.sort(key = lambda profile:profile["Name"],reverse = True)   
      else:
            print("Invalid choice..")
      return profiles


def main():
      print("="*20 ,"PROFILE APP","="*20)
      profiles = []
      profile_id = 100
      while True:
            print("1. Create Profile","2. veiw Profiles","3. Update Profile","4. Delete Profile",
                  "5. search profile","6. sort profile","7. Exit",sep = "\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                  profile_id += 1
                  profiles.append(create_profile(profile_id))
                  print()
            elif choice == "2":
                  if profiles:
                        show_profile(profiles)
                        print()
                  #    show_profile(profiles[-1])  # Show the most recent profile
                  else:
                     print("Profile Not Found.....Please Create profile First..\n")
            elif choice == "3":
                  update(profiles)

            elif choice == "4":
                  profiles = delete(profiles)
                  print()
            elif choice == "5":
                  if profiles:
                        search_profile(profiles)
                        print()
                  else:
                        print("No profile Exists..")

            elif choice == "6":
                  if profiles:
                        profiles = sort_profile(profiles)
                        print("Profile sorted successfully.....")
                  else:
                        print("No profile Exists..")

            elif choice == "7":
                  print("Good.. Bye...!")
                  break
            else:
                  print("Enter a valid Input.... Thank You...!")
                  print()
                 
if __name__ == "__main__":
      main()                

    
