import random
import fileIoHelper as fh
import json
from datetime import datetime

EMPTY = 'e'
TREASURE = 't'
MONSTER = 'm'
SWORD = 's'
POTION ='p'
VENOM= 'v'

FILE_PATH="gamelog.json"
SECONDCELL=" "

userDict= {}
userData= {}
startTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

whatToAddInGrid = (TREASURE, TREASURE, TREASURE, TREASURE, TREASURE, MONSTER, MONSTER, MONSTER, MONSTER, MONSTER, SWORD, SWORD, POTION, POTION, POTION, VENOM, VENOM, VENOM)

SCORE =0
numberOfSword=[]
numberOfPotion=[]
moveList = []

NROWS_IN_GRID = 6
NCOLS_IN_GRID = 7
grid = []
secondGrid = []
for r in range(0, NROWS_IN_GRID): 
  aRow = []
  for c in range(0, NCOLS_IN_GRID):
    aRow.append(EMPTY)  
  grid.append(aRow)

def findEmptyCell(aGrid, nRows, nCols):
  while True:
    row = random.randrange(nRows)
    col = random.randrange(nCols)
    if(aGrid[row][col] == EMPTY):
      return row, col

for item in whatToAddInGrid:
  rowRandom, colRandom = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
  grid[rowRandom][colRandom] = item

for r in range(0, NROWS_IN_GRID): 
  rowCell = []
  for c in range(0, NCOLS_IN_GRID):
    rowCell.append(SECONDCELL)  
  secondGrid.append(rowCell)
 
startRow, startCol = findEmptyCell(grid, NROWS_IN_GRID, NCOLS_IN_GRID)
secondGrid[startRow][startCol] = EMPTY

for row in secondGrid:
  print(row)
  
while True:
  print() 
  print('Score:', [SCORE],'','Sword:',[len(numberOfSword)],'','Potion:',[len(numberOfPotion)]) 
  print()
  direction = input('Press A, W, D, S to move: ').lower()
  print()
  prevCol = startCol
  prevRow = startRow 
  prevValue = grid[startRow][startCol]
  moveList.append(str(direction))
  
  if(direction == 'a'):
    if(startCol == 0):
      startCol = NCOLS_IN_GRID - 1
    else:
      startCol -= 1 
  elif (direction == 'd'):
    if(startCol == NCOLS_IN_GRID - 1):
      startCol = 0
    else:
      startCol += 1      
  elif(direction == 'w'):
    if(startRow == 0):
      startRow = NROWS_IN_GRID - 1
    else:
      startRow -= 1 
  elif(direction == 's'):
    if(startRow == NROWS_IN_GRID - 1):
      startRow = 0
    else:
      startRow += 1  
  else:
    print('Invalid move. Quitting the game.')
    break
  if secondGrid[startRow][startCol] !=SECONDCELL:
    grid[startRow][startCol]=prevValue
    startCol ,startRow = prevCol, prevRow
    print("User is not allowed to pass through a cell that is already visited before.")
    continue
  secondGrid[startRow][startCol]=grid[startRow][startCol]
  print("\033[H\033[J", end="")

  for row in secondGrid:
    print(row)

  foundInCell = grid[startRow][startCol]
  print('Now at row', startRow+1, ' col:', startCol+1, ' cell contains:', foundInCell)
  
  if foundInCell =='t':
    SCORE +=1
    print()
    print("+TREASURE")
        
  elif foundInCell =='s':
    print()
    numberOfSword.append('1')
    print("+SWORD")
          
  elif foundInCell =='p':
    numberOfPotion.append('1')
    print()
    print("+POTION!")
    
  elif foundInCell =='m':
    print()
    print("You encountered a monster.")
    if len(numberOfSword)> 0:
      numberOfSword.pop(0)
      print('You fought bravely and manage the kill monster! But,unfortunately your sword broke')
    else:
      print('You couldnt fight without a sword. Monster killed you!')
      print('Score:', [SCORE],'','Sword:',[len(numberOfSword)],'','Potion:',[len(numberOfPotion)]) 
      print()
      print('The Game Over!')
      break

  elif foundInCell =='v':
    print()
    print("You encountered a venom.")
    if len(numberOfPotion)> 0:
      numberOfPotion.pop(0)
      print('You have used your potion and covered from the venom.')
    else:
      print('You have been poisoned and because you dont have a potion you died!')
      print('Score:', [SCORE],'','Sword:',[len(numberOfSword)],'','Potion:',[len(numberOfPotion)])
      print()
      print('The Game Over.') 
      break
  SCORE +=1      

if fh.fileExists("gamelog.json"):
  content = fh.readFile("gamelog.json")
  userDict = json.loads(content)

userData["moves"]= moveList
userData["score"] = SCORE
userDict[startTime]= userData
dict_str=str(userDict)
dict_str=dict_str.replace("\'", "\"")

fh.writeFile("gamelog.json",dict_str)