import json 

# Load the username if it has been stored recently
# Otherwise, prompt for the username and store it

def greet_user():
    """Greet the user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
            
    except FileNotFoundError:
        username = input("what is your name?")

        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('We\'ll remember you when you come back, ' + username)
    else:
        print('Welcome back, ' + username +'!')

greet_user()
