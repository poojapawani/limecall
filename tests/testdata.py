users =[
    {'name':'valid_name','email': 'ppawani55@gmail.com','pwd':'PRpooja09@'},
    {'name':'invalid_name','email':'ppawani55@gmail.com', 'pwd':'PRpooja'},
    {'name': 'invalid_name2', 'email': 'ppawani55@gmail.com', 'pwd': 'jdjdjf'},
    {'name': 'blank_email', 'email': '', 'pwd': 'jdjdjf'},
    {'name': 'invalid_email', 'email': 'pppp', 'pwd': 'jdjdjf'},
    {'name': 'blank_password','email': 'ppawani55@gmail.com', 'pwd': ''},
    {'name': 'add_contact1','custName': 'Swara Hotwani', 'custEmail': 'ppawani55@gmail.com','custCountry':'India'}


]

def get_user(name):
    print(name)
    try:
        for user in users:
            if user['name'] == name:
                print (user)
                return user
        # return (user for user in users if user["name"] == name).next()
    except:
        print ("\n     User %s is not defined, enter a valid user.\n" %name)