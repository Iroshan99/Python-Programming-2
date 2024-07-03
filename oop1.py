#abstracton in python
from abc import ABC,abstractmethod
class Display(ABC):
    @abstractmethod
    def on_button(self):
        pass

    def button(self):
        print("iroshan")

class Telivison(Display):
    def on_button(self):
        print("This is the on button!")




display1=Telivison()
display1.on_button()
display1.button()








