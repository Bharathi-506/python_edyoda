import shop
key = input('Admin --> A or User --> U')
if key == 'A':
    username = input("Enter admin username:")
    password = input("Enter admin password:")
    shop.login(username,password )