def my_decorator(function):
    def everything():
        print(f"funtion: {function.__name__}")
        function()
        print()
    return everything

@my_decorator
def text_1():
    print("every is going to be ok")

@my_decorator
def text_2():
    print("Just don't give in..")

text_1()
text_2()
#why = (("hello","world", "it is a ","bad day..."),("but i can", "keep trying","one more time..."))


def my_nested(text):
    def run_on(name):
        print(f"{name.capitalize()}, {text}")
    return run_on 

t1=my_nested("everything's ok")
t1("hersy")
t1("ashely")

# gemini
print()


def requires_login(func):
    """
    A decorator that checks if a user is logged in before allowing access.
    """
    def wrapper(log=False,*args, **kwargs):
        # In a real app, this would check a session, cookie, or token
        is_logged_in = log # Simulate a logged-in user for this example
        
        if is_logged_in:
            print(f"Access granted for '{func.__name__}'.")
            return func(*args, **kwargs) # Execute the original function
        else:
            print(f"Access denied for '{func.__name__}'. Please log in.")
            # In a web framework, you might redirect to a login page or return an error response
            return None # Or raise an exception
    return wrapper

@requires_login
def view_profile(username):
    return f"Displaying profile for {username}."

@requires_login
def edit_settings():
    return "Editing user settings."

print("--- Demonstrating @requires_login ---")
print(view_profile(True,"Alice"))
print(view_profile(False,"Hersy"))
print(edit_settings(True))

