
print("Hello from other2 (begining)");


def name():
    print("In other file: " + __name__);
    return "Izzy 2";


print("Hello from other2 (end)");


def wrapper(f):
    def inner():
        print("Wrapper before");
        f();
        print("Wrapper after");
    return inner;


