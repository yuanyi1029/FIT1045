#From Applied 7.2
class Robot:
    """ Robot class for representing and manipulating robots. """

    phrase = "Hello World!" # Class Variable.

    def __init__(self, name): # Constructor (with parameters).
        """ Create a new robot. """
        self.name = name
        self.phrase = self.phrase
        self.hand = []

    # Methods
    def get_name(self):
        return self.name

    def get_phrase(self):
        return self.phrase

    def set_phrase(self, phrase):
        self.phrase = phrase

    def greet_another_by_name(self, robot):
        return "Greetings " + robot.get_name() + ", my name is " + self.get_name()  + "."

    def self_replicate(self):
        return Robot(self.get_name() + " Jr.")

r1 = Robot("test")
r1.hand = [1,2,3,4,5]
print(r1.hand)
