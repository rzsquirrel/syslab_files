import tkinter as tk

def importCoordinates(fileName):
    xyFile = open(fileName, 'r')
    numLines = int(xyFile.readline()) #number of points
    array = []
    for elt in range(numLines):
       pointID, x, y = xyFile.readline().split()
       array.append([int(pointID), float(x)+600, float(y)+600] ) #NOTE: pointID is the same as the array index!
    xyFile.close()
    return array
    
def importEdges(fileName):
    elFile = open(fileName, 'r')
    numLines = int(elFile.readline()) #number of points
    array = []
    for elt in range(numLines):
       point1, point2, point3, point4 = elFile.readline().split()
       array.append([int(point1), int(point2), int(point3), int(point4)] ) # A place for an id (0, here) is appended.
    elFile.close()
    return array

class TheFrame(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, width=1200, height=1200, background="bisque")
        self.xsb = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.ysb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.ysb.set, xscrollcommand=self.xsb.set)
        self.canvas.configure(scrollregion=(0,0,1000,1000))
        
        self.xsb.grid(row=1, column=0, sticky="ew")
        self.ysb.grid(row=0, column=1, sticky="ns")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #draw stuff
        #print(self.canvas.create_rectangle(50,120,190,300, outline="black", fill="red", activefill="green"))
        #print(self.canvas.create_rectangle(50,120,190,300, outline="black", fill="red", activefill="green"))
        
        #self.canvas.itemconfig(1, fill="blue")      #call for neighbors
        
        #fred=create_rectangle(50,120,190,300, outline="black", fill="red", activefill="green")        
        
        
        
        xyArray = importCoordinates("xy00009.txt")
        elArray = importEdges("el00009.txt")
        #for integer in range(len(xyArray)):
        for element in elArray:
            if element[0] >= 0 and element[1] >= 0 and element[2] >= 0 and element[3] >= 0:
                x=self.canvas.create_polygon(xyArray[element[0]][1], xyArray[element[0]][2], xyArray[element[1]][1], xyArray[element[1]][2], xyArray[element[2]][1], xyArray[element[2]][2], xyArray[element[3]][1], xyArray[element[3]][2], outline = "black", fill = "red", activefill = "pink")
                print( x )
            else:
                pass # self.canvas.create_polygon(600, 600)
        
        
        
        
        
        #bind mouse stuff
        self.canvas.bind("<ButtonPress-1>", self.move_start)
        self.canvas.bind("<B1-Motion>", self.move_move)
        #scroll
        self.canvas.bind("<Button-4>", self.zoomerP)
        self.canvas.bind("<Button-5>", self.zoomerM)
        #self.canvas.bind("<MouseWheel>",self.zoomer)
        self.canvas.bind('<Motion>', self.motion)           #MOTION
        
    #move
    def move_start(self, event):
        self.canvas.scan_mark(event.x, event.y)
    def move_move(self, event):
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    #linux zoom
    '''
    def zoomerP(self,event):
        self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
        self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    '''
    
    def zoomerP(self,event):
        self.canvas.scale("all", self.canvas.canvasx(event.x), self.canvas.canvasy(event.y), 1.1, 1.1)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    def zoomerM(self,event):
        self.canvas.scale("all", self.canvas.canvasx(event.x), self.canvas.canvasy(event.y), 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    
    '''
    def zoomer(self,event):
        if (event.delta > 0):
            self.canvas.scale("all", event.x, event.y, 1.1, 1.1)
        elif (event.delta < 0):
            self.canvas.scale("all", event.x, event.y, 0.9, 0.9)
        self.canvas.configure(scrollregion = self.canvas.bbox("all"))
    '''
    
    
    def motion(self,event):
        #print(event.x,event.y)
        #shadeNeighbors()
        for i in range(1, 65):
            self.canvas.itemconfig(i, fill="red")
        tag = self.canvas.find_closest(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))[0]
        print(tag)
        if tag<=63 or tag%8 == 0:
            if tag <= 63:
                self.canvas.itemconfig(tag+1, fill = "hot pink")
            elif tag%8 == 0:
                self.canvas.itemconfig(tag-7, fill = "hot pink")
        if tag>=2:
            self.canvas.itemconfig(tag-1, fill = "hot pink")
        if tag<=56:
            self.canvas.itemconfig(tag+8, fill = "hot pink")
        if tag>=9:
            self.canvas.itemconfig(tag-8, fill = "hot pink")
        

    


def shadeNeighborsAndUpdate(F,xyArray,elArray):
    '''
    array = [stores previous neighbors]
    #could also just unshade everything, and then shade desired rectangles for each round
    F.canvas.itemconfig(id,fill="red")
    
    
    
    
    tag = F.canvas.find_closest(F.canvas.canvasx(event.x), F.canvas.canvasy(event.y))[0]
    F.canvas.itemconfig(tag+1, fill = "hot pink")
    F.canvas.itemconfig(tag-1, fill = "hot pink")
    F.canvas.itemconfig(tag+8, fill = "hot pink")
    F.canvas.itemconfig(tag-8, fill = "hot pink")
    
    for n in range(7, len(elArray)-9):
        if(F.canvas.itemcget(n+1, "state") == "ACTIVE"):
            F.canvas.itemconfig(n+2, fill = "hot pink")
            F.canvas.itemconfig(n, fill = "hot pink")
            F.canvas.itemconfig(n+9, fill = "hot pink") 
            F.canvas.itemconfig(n-7, fill = "hot pink")
    '''
        #if(F.canvas.itemconfig(n+1
        
if __name__ == "__main__":
    root = tk.Tk()
    F = TheFrame(root)
    F.pack(fill="both", expand=True)
    #F.canvas.create_rectangle(50,120,190,300, outline="black", fill="red", activefill="green")
    xyArray = importCoordinates("xy00009.txt")
    elArray = importEdges("el00009.txt")
    prevNeighbors = []
    #root.after(100,shadeNeighbors(F,xyArray,elArray))
    
    while True:
        #shadeNeighborsAndUpdate(F,xyArray,elArray);
        F.canvas.itemconfig(10,fill="green")
        F.canvas.itemconfig(11,fill="hot pink")
        F.canvas.itemconfig(9,fill="blue")
        root.update_idletasks()
        root.update()
