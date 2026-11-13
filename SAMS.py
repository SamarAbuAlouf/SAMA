from termcolor import colored
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

total_student = []

def menu():
   print(colored("\n1. Add New Student.", "cyan"))
   print(colored("2. Delete Student (By Name).", "magenta"))
   print(colored("3. Show Performance Chart.", "cyan"))
   print(colored("4. Export Data To Excel.", "magenta"))
   print(colored("5. View Students List.", "cyan"))
   print(colored("6. Exit", "magenta"))

print(colored("\n--- Academic Management System ---", "green", attrs=["bold"]))
count = 3
PIN ="2026"
access = False
while count > 0 :
    PIN_try = input("Enter your PIN : ")
    if PIN_try == PIN:
        print(colored("Login Succsseful", "green", attrs=["bold"]))
        access=True
        break

    else :
        count -=1
        print(colored(f"you have just {count} chance .. uncorrect PIN, please try again:", "red", attrs=["bold"]))

if access == True:
   while True:
    print(colored("\n=================================================", "yellow", attrs=["bold"]))
    print(colored("ACADEMIC DASHBOARD", "yellow", attrs=["bold"]))
    print(f"Total Student is : {len(total_student)}")
    print(colored("=================================================", "yellow", attrs=["bold"]))

    menu()
    choice = input(colored("\nselect one option (1-6): ", "red", attrs=["bold"]))

    if choice == "1" :
        print(colored("\n--- Add New Student ---", "green", attrs=["bold"]))
        name = input("Enter student full name: ").lower()
        print(colored(f"Enter grade for {name} (0-100) : ", "yellow"))

        Programming= int(input("Enter your Programming Grade: "))
        if Programming > 100 :
            print(colored("This grade not valied", "red", attrs=["bold"]))
            int(input("Enter your Programming Grade: "))

        Data_Science= int(input("Enter your Data Science Grade: "))
        if Data_Science > 100 :
            print(colored("This grade not valied", "red", attrs=["bold"]))
            int(input("Enter your Data Science Grade: "))

        Database = int(input("Enter your Database Grade: "))
        if Database > 100 :
           print(colored("This grade not valied", "red", attrs=["bold"]))
           int(input("Enter your Database Grade: "))

        Ai = int(input("Enter your AI Grade: "))
        if Ai > 100 :
           print(colored("This grade not valied", "red", attrs=["bold"]))
           int(input("Enter your AI Grade: "))

        
        student_info = {"name"               : name ,
                        "Programming Grade"  : Programming ,
                        "Data Science Grade" : Data_Science ,
                        "Database Grade"     : Database ,
                        "AI Grade"           : Ai   
                     }
        
        total_student.append(student_info)
        print(colored(f"Student {name} Added Successfully!", "green", attrs=["bold"]))
        print(total_student)


    elif choice == "2" :
       del_name = input(colored("Enter the EXACT name of the student to delete: ", "yellow", attrs=["bold"]))

       found = False
       
       for item in total_student :
            if del_name == item["name"]:

                del_qestion = input(colored(f"Are you sure you want to delete '{del_name}' ? (yes/no) :", "blue", attrs=["bold"]) ).lower()
                if del_qestion == "yes": 
                    total_student.remove(item)
                    found = True
                    print(colored(f"Student {del_name} has been removed from the system", "green", attrs=["bold"]))
                    print(total_student)

                elif del_qestion == "no":
                    print(colored(f"The student name {del_name} will not be deleted", "green", attrs=["bold"]))

                else:
                    print(colored("Unknowable Value", "red", attrs=["bold"]))
                    
            elif del_name != item["name"]:
                print(colored("This name does not exist", "red", attrs=["bold"]))
                input(colored("Enter the EXACT name of the student to delete: ", "magenta", attrs=["bold"]))

            else:
                print(colored("Unknowable Value", "red", attrs=["bold"]))
                input(colored("Enter the EXACT name of the student to delete: ", "magenta", attrs=["bold"]))


       if not found :
            print(colored("The Name Not Found !", "red", attrs=["bold"]))
            input(colored("Enter the exact name of the student to delete: ", "magenta"))


    elif choice == "3" :
        if not total_student :
            print(colored("No data to show !", "red", attrs=["bold"]))
            continue

        df = pd.DataFrame(total_student)
        print(df)
        total =(( df["Programming Grade"] + df["Data Science Grade"] + df["Database Grade"] + df["AI Grade"]) /4 )
        print(total)
        width = 0.2 

        x = np.arange(len(df["name"]))

        plt.figure(figsize=(10,6))
        plt.bar(x - 0.4, df["Programming Grade"], width , label="Programming Grade", color="#6fb3f7")
        plt.bar(x - 0.2, df["Data Science Grade"] , width , label="Data Science Grade", color="#F35FE7")
        plt.bar(x, df["Database Grade"] , width , label="Database Grade", color="#44e687")
        plt.bar(x  +0.2, df["AI Grade"] , width , label="AI Grade", color="#d0eb36")

        plt.plot(x , df["Programming Grade"] , color="red")
        plt.plot(x , df["Data Science Grade"] , color="cyan")
        plt.plot(x , df["Database Grade"] , color="magenta")
        plt.plot(x , df["AI Grade"] , color="yellow")
        plt.plot(x , total , color = "#c41400" , marker ='h' , label ="Total marks", linewidth = 3  ,  linestyle="--")

        plt.xticks(x,df["name"])
        plt.xlabel("Student Names")
        plt.ylabel("Student Marks")
        plt.legend(loc="upper left")
        plt.title("Student performance")
        plt.title("A chart showing the grades of each student ")
        plt.grid(axis="both",  linestyle="--")

        plt.show()


    elif choice == "4" :
        if not total_student:
              print(colored("No data to show !", "red", attrs=["bold"]))
              continue
        df = pd.DataFrame(total_student)
        print(df)
        df.to_csv("SAMS.csv",index=True)

        
    elif choice == "5":
        if not total_student:
              print(colored("No data to show !", "red", attrs=["bold"]))
              continue
        for item in total_student :
             print(colored(f"The name is :{item["name"]} and grade of 'Programming Grade' is :{item["Programming Grade"]} and grade of 'Data Science Grade' is :{item["Data Science Grade"]} and grade of 'Database Grade' is :{item["Database Grade"]} and grade of 'AI' is :{item["AI Grade"]}", "yellow"))


    elif choice == "6":
        print(colored("Good Bye Doctor !", "cyan", attrs=["bold"]))
        break

    else:
        print(colored("your choice is wrong ! ", "yellow", attrs=["bold"]))
