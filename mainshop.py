import shop
key = input ("Admin --> A or User --> U :  Q ---> exit")


    
if key == 'A':
   username =input('Enter admin username:')
   pwd = input('Enter admin pwd:')
   if shop.login(username,pwd):
        print("loginsuccessful")
        while True:
            print("""
            V : View the Items
            E : Edit the Items
            R : Remove the Items
            I : Insert New Item
            """)
            key = input("Enter a key : ")
            if key == 'V':
               shop.viewAll()
            elif key == 'I':
                shop.insert_items()
            elif key == 'R':
                id = input ("enter an item to remove ")
                shop.remove_item(id)
            elif key == 'E':
                id = input ("Enter an item's id to Edit ")
                shop.edit_items(id)
            elif key == 'Q':
                 break
elif key == 'U':
    print("sign up --> R or Sign in --> L")
    key = input("Enter a key:")
    if key == 'R':
        pass
                
                
else:
    print("Admin login Fails")