import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.filedialog import asksaveasfile, asksaveasfilename

from random import sample

from vArrow import VArrow
from vNode import VNode
from vValue import VValue
from hnzController import *
import webbrowser
import vUtility as vu
import pickle


class View:

    def __init__(self, parent,data=None):
        # initialize variables
        self.container = parent
        self.flagNetworkCreated = False
        self.flagNetworkTrained = False
        self.flagLoadTrainFeature = False
        self.flagLoadTrainLabel = False
        self.lastx = 0
        self.lasty = 0
        self.listVArrow = []
        self.listVNode = []
        self.listComboBox = []
        self.listInputNode=[]
        self.listOutputNode=[]
        self.controller = None
        self.listFlatVNode=[]
        self.trainLabelPath=""
        self.trainFeaturePath=""
        self.testFeaturePath = ""
        self.data = data # data file
        #The 'subscriber' here
        #pub.subscribe(self.updateLossTxt,"update loss function txt")

    def updateLossTxt(self,data):
        self.text31ErrorTxtbox.insert(INSERT, data)


    def setup(self): # run first
        """Calls methods to setup the user interface."""
        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        """Create various widgets in the tkinter main window."""
        #self.var = tk.IntVar()
        #self.background_label = tk.Label(self.container)
        self.leftFrame = Frame(self.container,width=100, height=vu.windowHeight)
        self.midFrame = Frame(self.container,width=vu.canvasWidth, height=vu.canvasHeight)
        self.rightFrame = Frame(self.container,width=100, height=vu.windowHeight)
        self.rightFrame1=Frame(self.rightFrame)
        self.rightFrame2=Frame(self.rightFrame)

        self.statusbar=tk.Label(self.midFrame,text="On the way…", bd=1, relief=tk.SUNKEN, anchor=tk.W,fg="red")
        #button
        #self.b1Arrow = tk.Button(self.leftFrame, text = "Create Arrow", command = self.createArrows, width=20, height = 1)
        self.lab1input = tk.Label(self.leftFrame,text="输入层")
        self.combo1input = ttk.Combobox(self.leftFrame,values=[1,2,3,4,5,6,7,8,9,10])

        self.lab2layer1 = tk.Label(self.leftFrame, text="隐藏层 - 1")
        self.combo2layer1 = ttk.Combobox(self.leftFrame, values=[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.lab3layer2 = tk.Label(self.leftFrame, text="隐藏层 - 2")
        self.combo3layer2 = ttk.Combobox(self.leftFrame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.lab4layer3 = tk.Label(self.leftFrame, text="隐藏层 - 3")
        self.combo4layer3 = ttk.Combobox(self.leftFrame, values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.lab5output = tk.Label(self.leftFrame, text="输出层")
        self.combo5output = ttk.Combobox(self.leftFrame, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.b2Circle = tk.Button(self.leftFrame, text = "创造网络", command = self.createNodes, width =20, height =2)
        self.lab6TrainDiv = tk.Label(self.leftFrame, text="===训练===")
        #self.b7randomNum = tk.Button(self.leftFrame, text="Random Number", command=self.randomNum, width=20, height=1)
        self.c = Canvas(self.midFrame, bg='white', width=vu.canvasWidth, height=vu.canvasHeight)
        self.c.tag_bind("drag", "<Button-1>", self.clicked)
        self.c.tag_bind("drag", "<B1-Motion>", self.drag)
        #training inputs
        self.lab7LearningRate=tk.Label(self.leftFrame,text="学习率")
        self.combo6learningRate=ttk.Combobox(self.leftFrame,values=[0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.5])
        self.lab8epoch=tk.Label(self.leftFrame,text="迭代次数")
        self.combo7epoch = ttk.Combobox(self.leftFrame,
                                               values=[10,30,50,80,100,500,1000])
        self.lab9refreshRate=tk.Label(self.leftFrame,text="信息刷新率")
        self.combo8refreshRate = ttk.Combobox(self.leftFrame,
                                        values=[1,2,5,10,30,50])
        self.b8LoadFeature=tk.Button(self.leftFrame, text="加载数据", command=self.loadTrainFeature, width=20, height=1)
        self.b9LoadLabel = tk.Button(self.leftFrame, text="加载标签", command=self.loadTrainLabel, width=20,
                                     height=1)
        self.b10StartTrain=tk.Button(self.leftFrame, text="开始训练", command=self.startTrain,

                                                        width=20, height=2)

        #prediction inputs
        self.lab10DivPredection=tk.Label(self.leftFrame,text="===预测===")
        self.b11LoadPreFeature = tk.Button(self.leftFrame, text="加载预测数据", command=self.loadPreFeature, width=20,
                                       height=1)
        self.b12StartPredict = tk.Button(self.leftFrame, text="开始预测", command=self.startPredict,
                                         width=20, height=1)
        # self.lab11PreRounding=tk.Label(self.leftFrame,text="Rounding")
        # self.combo9PreRounding = ttk.Combobox(self.leftFrame,
        #                                        values=[1, 0.1, 0.01, 0.001, 0.0001, 0.00001])

        # hyper link

        #error rate and prediction text boxes to right hand frame
        self.lab31ErrorRate=tk.Label(self.rightFrame,text="===Loss Function Value===")

        self.text31ErrorTxtbox=tk.Text(self.rightFrame1,width=30)
        self.scl31vbar = tk.Scrollbar(self.rightFrame1, orient=VERTICAL)
        self.text31ErrorTxtbox.config(yscrollcommand=self.scl31vbar.set)
        self.scl31vbar.config(command=self.text31ErrorTxtbox.yview)
        #self.scl31vbar.config(command=self.text31ErrorTxtbox.xview)
        self.lab32PredictionResult=tk.Label(self.rightFrame,text="===Prediction Result===")
        self.text32PredictTxtbox = tk.Text(self.rightFrame2,width=30)
        self.scl32vbarPre = tk.Scrollbar(self.rightFrame2, orient=VERTICAL)
        self.text32PredictTxtbox.config(yscrollcommand=self.scl32vbarPre.set)
        self.scl32vbarPre.config(command=self.text32PredictTxtbox.yview)


        #TODO add file save and load status to menubar


        self.listComboBox.append(self.combo1input)
        self.listComboBox.append(self.combo2layer1)
        self.listComboBox.append(self.combo3layer2)
        self.listComboBox.append(self.combo4layer3)
        self.listComboBox.append(self.combo5output)


    def setup_layout(self):
        self.leftFrame.pack(side = LEFT)
        self.midFrame.pack (side=LEFT)
        self.rightFrame.pack (side = RIGHT)



        #self.b1Arrow.pack( side=TOP)
        self.lab1input.pack(side=TOP)
        self.combo1input.pack(side=TOP)
        self.lab2layer1.pack(side=TOP)
        self.combo2layer1.pack(side=TOP)
        self.lab3layer2.pack(side=TOP)

        self.combo3layer2.pack(side=TOP)
        self.lab4layer3.pack(side=TOP)
        self.combo4layer3.pack(side=TOP)
        self.lab5output.pack(side=TOP)
        self.combo5output.pack(side=TOP)
        self.b2Circle.pack(side = TOP)
        # training divider
        self.lab6TrainDiv.pack(side=TOP)
        #self.b7randomNum.pack(side=TOP)
        self.lab7LearningRate.pack(side=TOP)
        self.combo6learningRate.pack(side=TOP)
        self.lab8epoch.pack(side=TOP)
        self.combo7epoch.pack(side=TOP)
        self.lab9refreshRate.pack(side=TOP)
        self.combo8refreshRate.pack(side=TOP)
        self.b8LoadFeature.pack(side=TOP)
        self.b9LoadLabel.pack(side=TOP)
        self.b10StartTrain.pack(side=TOP)

        #canvas
        self.c.pack(side=TOP)
        #save load nn

        #prediction buttons
        self.lab10DivPredection.pack(side=TOP)
        self.b11LoadPreFeature.pack(side=TOP)
        self.b12StartPredict.pack(side=TOP)
        # self.lab11PreRounding.pack(side=TOP)
        # self.combo9PreRounding.pack(side=TOP)

        #pack rightFrame
        self.lab31ErrorRate.pack(side=TOP)
        self.rightFrame1.pack(side=TOP, fill=BOTH)
        self.text31ErrorTxtbox.pack(side=LEFT)
        self.scl31vbar.pack(side=LEFT,fill=Y)

        self.lab32PredictionResult.pack(side=TOP)
        self.rightFrame2.pack(side=BOTTOM, fill=BOTH)
        self.text32PredictTxtbox.pack(side=LEFT)
        self.scl32vbarPre.pack(side=LEFT,fill=Y)

        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X)
        #set default combobox default value
        self.combo1input.current(1)
        self.combo2layer1.current(3)
        self.combo3layer2.current(0)
        #self.combo3layer2["state"]=DISABLED
        self.combo4layer3.current(0)
        #self.combo4layer3["state"] = DISABLED
        self.combo5output.current(2)
        #set train combobox
        self.combo6learningRate.current(2)
        self.combo7epoch.current(1)#1, #0 for testing
        self.combo8refreshRate.current(2)#2, #0 for testing
        # self.combo9PreRounding.current(1)#2 round to 0.1
        self.statusbar["text"] = "Ready."

    def callback(self, url):
        webbrowser.open_new(url)

    def loadPreFeature(self):
        if self.flagNetworkTrained == False:
            tk.messagebox.showinfo(title="Error", message="Please create and train network first")

        else:
            self.testFeaturePath = ""
            self.testFeaturePath = askopenfilename(initialdir="./",
                                                    filetypes=[("Text File", "*.txt"), ("All Files", "*.*")],
                                                    title="Choose a file."
                                                    )
            self.controller.loadTestFeature(self.testFeaturePath)

    def loadTrainFeature(self):
        if self.flagNetworkCreated==False:
            tk.messagebox.showinfo(title="Error", message="Please create network first")
        else:
            self.trainFeaturePath=""
            if len(self.data) > 0:
                self.controller.loadTrainFeature("ture",self.data)
            else:
                self.trainFeaturePath = askopenfilename(initialdir="./",
                                       filetypes=[('Excel File',"*.xlsx"),("Text File", "*.txt"), ("All Files", "*.*")],
                                       title="选择一个文件"
                                       )
                self.controller.loadTrainFeature(self.trainFeaturePath)

            #self.flagLoadTrainFeature=True

    def loadTrainLabel(self):
        if self.controller.flagTrainFeatureLoad==False:
            tk.messagebox.showinfo(title="Error", message="Please create network, and load training feature set first")
        else:
            self.trainLabelPath=""
            self.trainLabelPath = askopenfilename(initialdir="./",
                                   filetypes=[("Text File", "*.txt"), ("All Files", "*.*")],
                                   title="Choose a file."
                                   )
            self.controller.loadTrainLabel(self.trainLabelPath)

            #self.flagLoadTrainLabel=True
    def startTrain(self):
        if self.controller.flagTrainLabelLoad == False:
            tk.messagebox.showinfo(title="Error", message="Please create network, and load training feature and label first.")
        else:
            self.b10StartTrain["state"] = DISABLED
            self.statusbar["text"] = "Training....."
            #complete start train
            self.controller.startTrain()
            self.b10StartTrain["state"] = NORMAL
            self.flagNetworkTrained=True
    def startPredict(self):
        if self.controller.flagTestFeatureLoad == False:
            tk.messagebox.showinfo(title="Error", message="Please load data for prediction")
        # TODO complete start Predict
        else:
            self.b12StartPredict["state"] = DISABLED
            self.statusbar["text"] = "Predicting....."
            self.controller.startPredict()
            self.b12StartPredict["state"] = NORMAL
    def updateBias(self,controlFlatBiasList):
        for i in range (0, controlFlatBiasList.__len__()):
            self.listFlatVNode[i].updateBias(controlFlatBiasList[i])
        pass
    def flattenListVNode(self): #no input layer
        self.listFlatVNode.clear()
        for layer in range(1,self.listVNode.__len__()):
            for n in self.listVNode[layer]:
                self.listFlatVNode.append(n)

    def updateWeight(self,controlFlatWeightList):
        for i in range (0, controlFlatWeightList.__len__()):
            self.listVArrow[i].updateWeight(controlFlatWeightList[i])

    def createArrows(self):
        for i in range (0, len(self.listVNode) ):
            #get column into J
            for j in self.listVNode[i]:
                arrowStart = j.getRightCod()


                if i<len(self.listVNode)-1:
                    #get rows in column
                    listArrowCol = []
                    for q in self.listVNode[i+1]:
                        arrowEnd = q.getLeftCod()
                        vArrow = VArrow()
                        vArrow.create(self.c, arrowStart,arrowEnd)
                        q.addLeftArrow(vArrow) #link from node
                        j.addRightArrow(vArrow)
                        #link node in arrow
                        vArrow.leftNode=j
                        vArrow.rightNode=q
                        self.listVArrow.append(vArrow)

    def clearInputValue(self):
        for n in self.listInputNode:
            n.updateValue(0.0)

    def clearOutputValue(self):
        for n in self.listOutputNode:
            n.updateValue(0.0)
    def clear(self):
        #remove all from canvas
        self.c.delete("all")
        self.lastx = 0
        self.lasty = 0
        self.listVArrow.clear()
        self.listVNode.clear()
        #self.listComboBox.clear()
        self.listInputNode.clear()
        self.listOutputNode.clear()
        self.listFlatVNode.clear()
        self.controller.clear()


    def createNodes(self):
        #network exists clear first
        if self.flagNetworkCreated:
            self.clear()

        listComboGet=[]
        #put combobox number into listComboGet
        for cb in self.listComboBox:
            if cb.get() != '0':
                listComboGet.append(cb.get())
        vu.tprint("listComboGet")
        vu.tprint(listComboGet)

        totalColumn=len(listComboGet)
        j=0
        #listNodeCoord=[]
        index=0
        for i in listComboGet:
            j=j+1
            #node coord by column
            listNodeCoord=vu.getNodePosition(totalColumn,int(i),j)
            listLayer=[]
            index+=1
           #create nodes based on coordination
            for c1 in listNodeCoord:
                vNode = VNode()
                vNode.create(self.c, c1[0], c1[1])
                # append value box if in first or last column
                if index == 1:#node with input
                    vNode.what="input"
                    self.listInputNode.append(vNode)
                elif index == listComboGet.__len__():
                    # setup output node
                    vNode.what = "output"
                    self.listOutputNode.append(vNode)
                listLayer.append(vNode)
            self.listVNode.append(listLayer)


        #pub.sendMessage("Button_createNode_Clicked")
        #self.b2Circle["state"]=DISABLED
        #create arrows
        self.createArrows()
        self.flattenListVNode()
        #setup controller network
        self.setupControlNetwork()
        # generate random weight and bias
        self.randomNum()
        # set flag as true
        self.flagNetworkCreated = True
        self.flagNetworkTrained = False
        #reload train feature and label if they have been loaded before
        if self.controller.flagTrainFeatureLoad:
            self.controller.loadTrainFeature(self.trainFeaturePath)
        if self.controller.flagTrainLabelLoad:
            self.controller.loadTrainLabel(self.trainLabelPath)
        #vu.tprint (self.listVNode)
    def randomColor(self):# not in use
        listColor = ["red","blue","yellow","green","orange","purple"]
        return sample (listColor,1)

    def clicked (self,event):
        self.clickedid= event.widget.find_withtag('current')[0]
        self.lastx, self.lasty = event.x, event.y
        #self.c.tag_raise(self.clickedid)
        #self.c.itemconfig(self.clickedid,fill="red")
        #vu.tprint ("clicked id: "+str(self.clickedid))

    def drag(self,event):
        # search id to see if the item is in a node
        for column in self.listVNode:
            for n in column:
            #another loop to get node element
                if n.containAny(self.clickedid):
                    #vu.tprint("arrow found: "+str(self.clickedid))
                    n.move(event.x-self.lastx, event.y-self.lasty)
                    self.lastx = event.x
                    self.lasty = event.y
                    return
        self.c.move(self.clickedid,event.x-self.lastx, event.y-self.lasty)
        self.lastx=event.x
        self.lasty=event.y
    def randomNum(self):
        self.controller.randomWeights(self.listVNode)
        self.controller.randomBias(self.listVNode)
        #self.b7randomNum["state"] = DISABLED

        #self.lab6TrainDiv.pack(side=TOP)
    def setController(self,con): #set link to controller
        self.controller=con
    def setupControlNetwork(self):#pass number to controller
        self.controller.numInput=len(self.listInputNode)
        self.controller.numOutput=len(self.listOutputNode)
        vu.tprint(len(self.listComboBox))
        for i in range (len(self.listComboBox)):
            vu.tprint ("i=")
            vu.tprint (i)
            if (i >0) and i<len(self.listComboBox)-1:
                # setup total hidden layer in controller
                j=int(self.listComboBox[i].get())
                if j!=0:
                    self.controller.numOfHLayers.append(j)
        vu.tprint("number of hidden layer")
        vu.tprint(self.controller.numOfHLayers)
#test view
if __name__ == "__main__":
    mainwin = Tk()
    WIDTH = vu.windowWidth
    HEIGHT = vu.windowHeight
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    #mainwin.resizable(0, 0)
    mainwin.title("view testing")

    view=View(mainwin)
    view.setup()
    mainwin.mainloop()