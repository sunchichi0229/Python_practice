from animal import dog #animalというpackageからdogというmoduleを呼び出す
from animal import cat #animalというpackageからcatというmoduleを呼び出す

from animal import * #animal packageが持っているすべてのmoduleを呼び出す

d = Dog() 
c = Cat()

d.hi()
c.hi()