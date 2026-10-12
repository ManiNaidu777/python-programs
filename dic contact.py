contacts={}
while True:
    print("1.Add Contact Name")
    print("2.Search Contact")
    print("3.update")
    print("4.Delete Contact")
    print("5.Display contact")
    print("6.Exit")

    choice=int(input("Enter your Choice :"))

    if choice==1:
        Name =input("Enter Name:")
        phone =int(input("Number:"))
        contacts[Name]=phone
        print("Contact Add Successfully")

    elif choice == 2:
        Name = input("Enter name:")
        if Name in contacts:
            print("Phone",contacts[Name])
        else:
            print("Contact Not Found")

    elif choice==3:
        Name=input("Enter contact name:")
        if Name in contacts:
            phone=input("Enter new phone:")
            contacts[Name]=phone
            print("updated successfully")
        else:
            print("contact Not Found")
    elif choice==4:
        Name=input("Enter Contact Name:")
        if Name in contacts:
            del contacts[Name]
            print("delete succeessfully")
        else:
            print("contact Not found")

    elif choice==5:
        print("\n Contacts List")
        for Name,phone in contacts.items():
            print(Name,"=",phone)

    elif choice==6:
        print("THank You")
        break
    else:
        print("Invalid choice")





