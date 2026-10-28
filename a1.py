from abc import ABC, abstractmethod

class Absclass(ABC):
    def prints(self,x):
        print("Passed Value: ", x)
    @abstractmethod
    def task(self):
        pass

class test_class(Absclass):
    def task(self):
        print("I am inside of the child class")

test_obj = test_class()
test_obj.task()
test_obj.prints(100)