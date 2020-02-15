#program to illustrate protected access modifier in a class and installing base class members using instance method

#super class
class protecteddemo:

    #protecteddata member
    _name =None
    _roll =None
    _branch =None

    def _getdata(self,name,roll,branch):
        self._name =name
        self._roll =roll
        self._branch =branch

        #derived class
        class student(protecteddemo):

            #public member function
            def displayDetails(self):

                #accessing protected data member of super class
                print("name:",self._name)
                print("roll:",self._roll)
                print("branch:",self._branch)
                #creating object of derived class
                obj=student()
                #calling public member functions of the class
                obj._getdata("ghanshyam",120,"Information technology")
                obj._displayDetails()
