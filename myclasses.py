# Example classes
#
# This will be imported using something like this:
#
# from myclasses import MyClass1, MyClass2;
#
class MyClass1:
    name = "";
    # Constructor with an argumnent
    def __init__(self,a):
        print("Init of MyClass1 for " + a);
        self.name = a;

    def getName(self):
        return "Name was " + self.name;

class MyClass2:
    def __init__(self):
        print("Init of MyClass2");

