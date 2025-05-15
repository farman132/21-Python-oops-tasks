def log(fn):
    def wrapper():
        print("Function is being called")
        fn()
    return wrapper

@log
def say_hello():
    print("Hello!")

say_hello()
