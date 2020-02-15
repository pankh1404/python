#program udsing getter and setter method

#defining property name
class property_fun_demo:

    #function to get value
    def get_age(self):
        print("get method called")
        return self._age

    #function to set value
    def set_age(self):
        print()
        return("set method called")

    #function to delete value
    def del_age(self):
        del self.age

    def del_age(self):
        del self.age

    age = property(get_age,set_age,del_age)



mark = property_fun_demo()
mark._age = 14
print(mark._age)
