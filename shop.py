import json
def login (username, password):
    with open ('admin.json') as fr:
        data = json.load(fr)
        if data['Username'] == username and data['Password'] == password :
            print("Login successful")
        else:
            print("please try with admin details")
       