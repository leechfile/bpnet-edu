from hnzView import View
from hnzController import Controller
from tkinter import *
import vUtility



def nerual_start(data=None):
    mainwin = Tk()
    WIDTH = vUtility.windowWidth
    HEIGHT = vUtility.windowHeight
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    mainwin.title("Graphic Neural Network")
    #create view and controller
    controller=Controller()
    view=View(mainwin)
    #cross lin view and controller
    controller.setView(view)
    view.setController(controller)
    #setup and complete view
    view.setup()
    mainwin.mainloop()

if __name__ == "__main__":
    nerual_start()

