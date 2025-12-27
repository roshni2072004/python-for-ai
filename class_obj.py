class Animals:
  def __init__(self,name):
    print("object created")
    self.name=name

  def bark(self):
    print("Barking")
    
    
class Dog(Animals):
  def make_sound(self):
    return f"{self.name} barks: woof!"


puppy=Dog("jimmy")
puppy.make_sound()
