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
      print("Profile Created Successfully...")
      return profile_data
      
def show_profile(profile_data):
      pattern = '=' * 40
      space = ' ' * 15
      print(pattern, space + "MY PROFILE" + space, pattern, "Name : " + profile_data['Name'], "Age : " + str(profile_data['Age']), "City : " + profile_data['City'], "Skill : " + profile_data['Skill'],"Category: "+ profile_data['category'],  sep="\n")

def delete(profile_data):
      if profile_data is not None:
            confirm = input("Do you want to delete : (Y/N)")
            if confirm == "Y":
               profile_data = None
               print("Profile Delated Successfully...!")
      else:
            print("No profile Found")
      return profile_data

def update(profile_data):
      if profile_data is not None:
                        print("Enter what youn want to Update...","1. Name","2. Age", "3. City","4. skill")
                        upd_choice = input("Enter your choice...")
                        if upd_choice == "1":
                            new_name = get_name()
                            profile_data["Name"] = new_name
                            print("Profile Updated Successfully")
                                                          
                        elif upd_choice == "2":
                            new_age = get_age()
                            new_cate = get_category(new_age)
                            profile_data["Age"] = new_age
                            profile_data["category"] = new_cate
                            print("Profile Updated Successfully")                            
                        elif upd_choice == "3":
                            new_city = get_city()
                            profile_data["City"] = new_city
                            print("Profile Updated Successfully")
                               
                        elif upd_choice == "4":
                            new_skill = get_skill()
                            profile_data["Skill"] = new_skill
                            print("Profile Updated Successfully")

                        else:
                             print("Invalid Input")
      
      else:
         print("No Existing Profile Found.......")



def main():
      print("="*40 ,"PROFILE APP","="*40)
      profile_data = None
      while True:
            print("1. Create Profile","2. veiw Profile","3. Update Profile","4. Delete Profile","5. Exit",sep = "\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                  profile_data = create_profile()
            elif choice == "2":
                  if profile_data is not None:
                     show_profile(profile_data)
                  else:
                     print("Profile Not Found.....Please Create profile First..")
            elif choice == "3":
                  update(profile_data)

            elif choice == "4":
                  profile_data = delete(profile_data)

            elif choice == "5":
                  print("Good.. Bye...!")
                  break
            else:
                  print("Enter a valid Input.... Thank You...!")
                  
                 
                  
main()