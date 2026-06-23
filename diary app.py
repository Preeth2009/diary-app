def write():
    f=open("diary.txt","a")
    a=input("Enter Note:")
    f.write(a)
    f.write('\n')
    f.close()
    print("Note saved successfully.")
    print()

def view():
    f=open("diary.txt","r")
    print("----- My Notes -----")
    print()
    for i in f:
        print(i)
    print("---------------")
    print()

def close():
    print("Thank you for using Diary App.")

while True:
    print("===== Diary App =====")
    print()
    print("1. Write Note")
    print("2. View Notes")
    print("3. Exit")
    print()
    a=int(input("Enter choice:"))
    if a==1:
        write()
    elif a==2:
        view()
    elif a==3:
        close()
        break
    else:
        print("Enter valid choice!")






    








    
    
    
