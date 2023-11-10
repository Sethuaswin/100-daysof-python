#############################################################################
# This File Explains about class inhertance
############################################################################


# Let's take a class called Animal
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")


# Let's take another class called Fish it inherits attributes and  methods from the Animal class  # noqa
class Fish(Animal):  # while creating the class declare the parant class inside the paranthesis   # noqa
    def __init__(self):
        super().__init__()  # the super() function will inherit the attributes and methods form the Animal class to Fish Class   # noqa

    def breathe(self):
        super().breathe()
        print("doing this underwather")  # In addition to breathe method from animal we can add some extra things   # noqa

    def swim(self):
        print('moving in water.')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
