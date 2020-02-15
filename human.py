class Human:
   

   def say_hello(self,name=None):

      if name is not None:
         print('Hello',name)
      else:
         print('Hello')

#Create Instance
obj=Human()

#Call The Method
obj.say_hello()

#Call the Method With a Parameter
obj.say_hello('Everyone')

  
