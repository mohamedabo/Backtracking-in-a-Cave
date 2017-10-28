# Abdirahman Mohamed CSC 236 Lab 2
from Stack import*
import copy
import time
class Map:
    """Initializes a cave map where you iterate through it and find the treasure"""
    def __init__(self):
        """Initialize class values"""
        self.map= [] # empty list of the map
        self.row = -1 # the row
        self.col = -1 # the col
        self.initialrow = -1 # initial row
        self.initialcol = -1 # initial col
        self.currentrow = -1 # current row
        self.currentcol = -1 # current col
        self.location = Stack() # the location of the stack
        self.score = 0 # the score
        self.visited = [] # empty list of vistied directions
    def finding_m(self):
        """Finds M in the map"""
        for i in range (int(self.row)):
            for j in range (int(self.col)):
                if self.map[i][j]=="M":
                    self.initialrow = int(i) # the initial row
                    self.initialcol = int(j) # the initial col
                    self.currentrow = int(i) #  the current row
                    self.currentcol = int(j) # the current col
    def check_m(self):
        """Checks if M is in the map"""
        if (self.initialcol==-1) and (self.initialrow==-1):
            print("M is not found")
    def decide_next_step(self):
        """Decides the next step"""
        if self.currentrow ==0:
            print("You can't go north anymore!")
        if self.currentcol == (self.col-1):
            print("You can't go east anymore!")
        if self.currentrow==(self.row-1):
            print("You can't go south anymore!")
        if self.currentcol==0:
            print("You can't go west anymore!")
    def next_step(self):
        """Moves m in four directions: north,west,south and east to find the treasure"""
        if self.north()==True:
            print("You can move north")
            self.location.push([self.currentrow , self.currentcol]) # update the stack with  locations
            self.visited.append([self.currentrow,self.currentcol]) # appending the locations to visited
            self.map[self.currentrow][self.currentcol] = '.' # updating the map with the locations of the dots
            self.currentrow-=1 # decrement of the current row
            self.map[self.currentrow][self.currentcol] = 'M' # updating the map with the location of M
            self.print_map() # printing the map
            self.next_step() # recursive call
        if self.east()==True:
            print("You can move east")
            self.location.push([self.currentrow , self.currentcol]) # update the stack with  location
            self.visited.append([self.currentrow,self.currentcol]) # appending the locations to visited
            self.map[self.currentrow][self.currentcol] = '.' # updating the map with the locations of the dots
            self.currentcol+=1 # increment of the current col
            self.map[self.currentrow][self.currentcol] = 'M' # updating the map with the location of M
            self.print_map() # printing the map
            self.next_step() # recursive call
        if self.south()==True:
            print("You can move south")
            self.location.push([self.currentrow , self.currentcol]) # update the stack with  location
            self.visited.append([self.currentrow,self.currentcol]) # appending the locations to visited
            self.map[self.currentrow][self.currentcol] = '.' # updating the map with the locations of the dots
            self.currentrow+=1 # increment of the current row
            self.map[self.currentrow][self.currentcol] = 'M' # updating the map with the location of M
            self.print_map() # printing the map
            self.next_step() # recursive call
        if self.west()==True:
            print("You can move west")
            self.location.push([self.currentrow , self.currentcol]) #update the stack with  location
            self.visited.append([self.currentrow,self.currentcol]) # appending the locations to visited
            self.map[self.currentrow][self.currentcol] = '.' # updating the map with the locations of the dots
            self.currentcol-=1 # decrement of the current col
            self.map[self.currentrow][self.currentcol] = 'M' # updating the map with the location of M
            self.print_map() # printing the map
            self.next_step() # recursive call
        print("You are stuck between walls!")
        self.backtrack() # recursive call of the backtrack
    def backtrack(self):
        """Backtracking if M was stuck"""
        if self.location.size()==0: # if the stack is empty
            print("You can't backtrack")
        else: # if the stack is not empty
            self.map[self.currentrow][self.currentcol]="." # updating the map with the locations of the dots
            p = self.location.pop() # removes and returnes the first element in the location
            self.currentrow = p[0] # current row
            self.currentcol = p[1] # current col
            self.map[self.currentrow][self.currentcol]="M" # updating the map with the location of M
            self.print_map() # printing the map

            #self.next_step()
    def north(self):
        """Moves m to north"""
        if self.map[self.currentrow-1][self.currentcol]  == "T": # if the row and col are equal to t
            self.treasurepath() # recursive call to the treasure path function
        elif self.map[self.currentrow-1][self.currentcol]  == "." and not [self.currentrow-1,self.currentcol] in self.visited: # if there are dots and we didn't visit the north
            return True # returnes to the next step function
    def east(self):
        """Moves M to the east"""
        if self.map[self.currentrow][self.currentcol+1] == "T" :
            self.treasurepath()
        elif self.map[self.currentrow][self.currentcol+1] == "." and not [self.currentrow,self.currentcol+1] in self.visited: # if there are dots and we didn't visit the east
            return True # returnes to the next step function
    def south(self):
        """Moves M to the south"""
        if self.map[self.currentrow+1][self.currentcol] == "T":
            self.treasurepath()
        elif self.map[self.currentrow+1][self.currentcol]  == "." and not [self.currentrow+1,self.currentcol] in self.visited: # if there are dots and we didn't visit the south
            return True # returnes to the next step function
    def west(self):
        """Moves M to the west"""
        if self.map[self.currentrow][self.currentcol-1]  == "T":
            self.treasurepath()
        elif self.map[self.currentrow][self.currentcol-1]  == "." and not [self.currentrow,self.currentcol-1] in self.visited: # if there are dots and we didn't visit the west
            return True # returnes to the next step function
    def treasure(self,r,c):
        """Creats the path and score"""
        if self.map[r][c]=="T": # if the rows and col in the map equal to t
            self.score+=1 # increment of score
            self.path = copy.deepcopy(self.location) # deep copy of the stack
            self.path.push([r,c]) # pushes the updated rows and col to the stack
        self.treasurepath() # recursive call to treasure path
    def make_map(self,file1):
        """Opens the map file and reads it"""
        file = open(file1)
        k = file.readline()
        self.row, self.col = k.split()
        self.row = int(self.row)
        self.col = int(self.col)
        while k != "":
            k=file.readline()
            self.map.append(k.strip('\n').split()) # appending the splitting of k
    def treasurepath(self):
        """Finds the treasure path"""
        t = [] # empty list
        self.path = copy.deepcopy(self.location)
        for p in range(self.path.size()): # in the length of the path
            t.append(self.path.pop()) # appending the items of t
        print("you found treasure!")
        print(t)
        time.sleep(1)
    def print_map(self):
        """Displays the map on the screen"""
        v = ""
        for i in self.map:
            v+=" ".join(i) # Converts the map list to a string
            v+="\n"
        print(v)
        time.sleep(1)
