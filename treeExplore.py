from numpy import *

from Tkinter import *
import reg_tree

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def reDraw(tolS,tolN):
    reDraw.f.clf()       
    reDraw.a = reDraw.f.add_subplot(111)
    if chkBtnVar.get():
        myTree=reg_tree.createTree(reDraw.rawDat, reg_tree.modelLeaf,\
                                   reg_tree.modelErr, (tolS,tolN))
        yHat = reg_tree.createForeCast(myTree, reDraw.testDat, \
                                       reg_tree.modelTreeEval)
    else:
        myTree=reg_tree.createTree(reDraw.rawDat, ops=(tolS,tolN))
        yHat = reg_tree.createForeCast(myTree, reDraw.testDat)
    reDraw.a.scatter(array(reDraw.rawDat[:,0]), array(reDraw.rawDat[:,1]), s=5) 
    reDraw.a.plot(reDraw.testDat, yHat, linewidth=2.0)
    reDraw.canvas.show()
    
def getInputs():
    try: tolN = int(tolNentry.get())
    except: 
        tolN = 1 
        print "enter Integer for tolN"
        tolNentry.delete(0, END)
        tolNentry.insert(0,'1')
    try: tolS = float(tolSentry.get())
    except: 
        tolS = 0 
        print "enter Float for tolS"
        tolSentry.delete(0, END)
        tolSentry.insert(0,'0')
    return tolN,tolS

def drawNewTree():
    tolN,tolS = getInputs()
    reDraw(tolS,tolN)
    
root=Tk()

reDraw.f = Figure(figsize=(5,4), dpi=100)
reDraw.canvas = FigureCanvasTkAgg(reDraw.f, master=root)
reDraw.canvas.show()
reDraw.canvas.get_tk_widget().grid(row=0, columnspan=3)

Label(root, text="tolN").grid(row=1, column=0)
tolNentry = Entry(root)
tolNentry.grid(row=1, column=1)
tolNentry.insert(0,'1')
Label(root, text="tolS").grid(row=2, column=0)
tolSentry = Entry(root)
tolSentry.grid(row=2, column=1)
tolSentry.insert(0,'0')
Button(root, text="ReDraw", command=drawNewTree).grid(row=1, column=2, rowspan=3)
chkBtnVar = IntVar()
chkBtn = Checkbutton(root, text="Model Tree", variable = chkBtnVar)
chkBtn.grid(row=3, column=0, columnspan=2)

reDraw.rawDat = mat(reg_tree.loadDataSet('Training data.txt'))
reDraw.testDat = arange(min(reDraw.rawDat[:,0]),max(reDraw.rawDat[:,0]),0.01)
reDraw(0, 1)
               
root.mainloop()
