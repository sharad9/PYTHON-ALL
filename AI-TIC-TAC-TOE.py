#import sys
#sys.setrecursionlimit(9500)
import random
class Point:
 x=0
 y=0
 def _init_(self,x,y):
  self.x=x
  self.y=y
class Board():
    
 
 box=[[" " for x in range(3)]for y in range(3)]
    
    
 def display(self):
  for i in range(3):
   
   for j in range(3):
    print("|",end="")
    print(self.box[i][j],end="")
   print("|")
     

 def placeElement(self,p,s):
  self.box[p.x][p.y]=s
                                      
 def  Remove(self,p):
  self.box[p.x][p.y]=" "
        
 def getAvailableBoxes(self):
  availableBoxes=[]
  for i in range(3):
   for j in range(3):
    if(self.box[i][j]==" "):
     availableBoxes.append(Point(i,j))
        
  return availableBoxes
        
 def takeHumanInput(self):
  i=int(input())
  EmptySpaces=self.getAvailableBoxes()
  self.placeElement(EmptySpaces[i-1],"X")
        
 def HasWon(self,s):
  if((self.box[0][0]==self.box[1][1] and self.box[1][1]==self.box[2][2] and self.box[2][2]==s) or (self.box[0][2]==self.box[1][1] and  self.box[1][1]==self.box[2][0] and self.box[2][0]==s)):
   return True
           
  for i in range (3):
   if((self.box[i][0]==self.box[i][1] and self.box[i][1]==self.box[i][2] and self.box[i][2]==s) or (self.box[0][i]==self.box[1][i] and self.box[1][i]==self.box[2][i] and self.box[2][i]==s)):
		  return True
	  
  return False			
		
 def isGameOver(self):
  return (self.HasWon("X") or self.HasWon("O") or self.getAvailableBoxes()==[])
       
 def minimax(self,depth,isMax):
  boxAvailable=self.getAvailableBoxes()
  if(self.HasWon("O")): return 1
  if(self.HasWon("X")): return -1
  if(boxAvailable==[]): return 0
       
  Min=2147483647
  Max=-2147483648
  for i in (boxAvailable):
   if(isMax==True):
    self.placeElement(i,"O")
    Max=max(self.minimax(depth+1,False),Max)
    self.Remove(i)
   else:
    self.placeElement(i,"X")
    Min=min(self.minimax(depth+1,True),Min)
    self.Remove(i)
         
  return isMax==True and Max or Min  
  
                     
 def findBestMove(self):

  leftBoxes=self.getAvailableBoxes() 
  bestVal=-2147483648
  for i in leftBoxes:
   self.placeElement(i,"O")
   moveVal=self.minimax(0,False)
   if(moveVal>bestVal):A=i
   bestVal=max(moveVal,bestVal)
   self.Remove(i)
  return A
  
if _name=='main_':
 b=Board()
 print("AI:")
 toss=random.randint(0,2)
 if(toss==0):
  print("I WON toss")
  c=Point(random.randint(0,2),random.randint(0,2))
   
  b.placeElement(c,"O")
 else:print("You Won Toss")
 while(b.isGameOver()==False):
  print("Make Your Move:")
  b.display()
  print("____________") 
  b.takeHumanInput()
 
  if(b.isGameOver()==True):break 
  ai=b.findBestMove()
  b.placeElement(ai,"O")
  
 b.display()
 if(b.HasWon("O")):
  print("YOU LLLLost")
 else:
  if(b.HasWon("X")):
   print("Nooooo")
  else:
   print("Its Draw")
