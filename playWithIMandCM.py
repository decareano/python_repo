#this is a placeholder for all concepts re: Instance, classes and static
#methods. I will continue adding to this as I get a better picture

class MyClass:
  #obj is an instance object
  #regular IMethod below with one parameter. Can take more
  #takes an arg (self) that points to an instance
  #of MyClass when method is called
  def method(self):
    print('instance method called', self)

  # @classmethod
  # def classmethod(cls):
  #   return 'class method called', cls

  # @staticmethod
  # def staticmethod():
  #   return 'static method called'


#lets call the IM:
obj = MyClass()
obj.method()  #or
MyClass.method(obj)

#lets call the class method
#take a cls param that points to the calls not
#instance object. cannot access self
#obj.classmethod()
#or
