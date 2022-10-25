'''
Implement the singleton pattern with a twist. First, instead of storing one instance, store two instances.
And in every even call of getInstance(), return the first instance and in every odd call of getInstance(), return the second instance.
'''

# Python does not support private members/methods in classes, so singleton classes cannot be built in the strictest sense.
# A true singleton class would require a private constructor to prevent it being instantiated outside the class.

class TwoInstance:
    # Static members.
    instances = []
    is_even = False

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return f"TwoInstance class. Value: {self.val}"

    @staticmethod
    def create():
        TwoInstance.instances = []
        TwoInstance.instances.append(TwoInstance(1))
        TwoInstance.instances.append(TwoInstance(2))

    @staticmethod
    def getInstance():
        out_instance = TwoInstance.instances[0] if TwoInstance.is_even else TwoInstance.instances[1]
        TwoInstance.is_even = not TwoInstance.is_even
        return out_instance

TwoInstance.create()

print(TwoInstance.getInstance())
print(TwoInstance.getInstance())
print(TwoInstance.getInstance())
print(TwoInstance.getInstance())