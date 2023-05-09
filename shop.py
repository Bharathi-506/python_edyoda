import json , csv
def login(username,password):
    with open('admin.json') as fr:
        data = json.load(fr)
        if data['username'] == username and data['password'] == password:
            print("Login successful")
            print("V---> View items")
            v = input("Enter a key:")
            if v == 'V':
               viewAll()
        else:
            print("please try login with admin details")
        
def viewAll():
    with open('fooditems.csv') as fr:
        r =csv. reader(fr)
        for items in r:
            print(items)

def insert_items():
    with open('fooditems.csv') as fr:
        r = csv.reader(fr)
        id = 0
        for i in r:
            if len(i) > 0:
                id = i[0]
            

    with open('fooditems.csv','a') as fw:
        w = csv.writer(fw)
        name = input('Enter a item name:')
        price = input('Enter price:')
        w.writerow([str(int(id)+1), name, price])


def remove_item(id):
    with open ('fooditems.csv') as fr:
        r = csv.reader(fr)
        lines = []
        for items in r:
            if id not in items:
                lines.append(items)
    with open('fooditems.csv','w',newline ='')as fw:
        w = csv.writer(fw)
        w.writerows(lines)

def edit_items(id):
    with open ('fooditems.csv') as fr:
        r = csv.reader(fr)
        lines = []
        for items in r :
            if id in items:
                price = input("Enter a price :")
                items[2] = price
            lines.append(items)
    with open ('fooditems.csv','w', newline='') as fw:
        w = csv.write(fw)
        w.writerows(lines)

def signUp():
    name =input("Enter a name:")
    mobile = input(" Enter mobile number:")
    email = input("Enter email :")
    pwd = input("Create password :")
    with open('User_RegData.csv') as fr:
        data = fr.read()
        filehasData = False
        if len(data)  > 0:
            filehasData = True
    with open('User_RegData.csv','a', newline='') as fw:
        w=csv.writer(fw)
        if not filehasData:
            columns = ['UserID', 'Nmae','Mobilenumber', 'Email', 'Password']
            w.writerow(columns)




        

