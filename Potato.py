#WALKING POTATO.py
import os
import time

def animate_Potato():
  distanceFromTop = 0
  distanceFromLeftSide = 0
  step = 1
  while True:
    print("\n" * distanceFromTop)
    print((" " * distanceFromLeftSide) + " _ ")
    print((" " * distanceFromLeftSide) + "( )")
    print((" " * distanceFromLeftSide) + "- -")
    distanceFromLeftSide +=step
    if distanceFromLeftSide>20 or distanceFromLeftSide<=0:
      step = -step 
      distanceFromTop += 2
      if distanceFromTop >20:
        distanceFromTop = 0
        distanceFromLeftSide = 0
        step = 1
    time.sleep(0.05)
    os.system('clear')  
  
#Main Program Starts Here....
animate_Potato()


