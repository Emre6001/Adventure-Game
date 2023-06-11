import os

def fileExists(filePath):
  exists = os.path.exists(filePath)
  return exists
  
def writeFile(filePath, textToWrite):
  fileHandle = open(filePath, 'w')
  fileHandle.write(textToWrite)
  fileHandle.close()
  
def readFile(filePath):
  if not fileExists(filePath):
    print('The file, ' + filePath + ' does not exist - cannot read it.')
    return ""
  fileHandle = open(filePath, 'r')
  data = fileHandle.read()
  fileHandle.close()
  return data