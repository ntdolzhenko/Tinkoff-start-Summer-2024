n = int(input())

dirs = dict()

for i in range(n):
    dirPath = input().split('/')
    temp = dirs
    # for each subdir in path
    for d in dirPath[1:]:
        #if it is new dir, add it
        if d not in temp:
            temp[d] = dict() 
        # move to new dir
        temp = temp[d]
        
# add root dir from last subdir path
dirs = { dirPath[0]: dirs }
        
def printDirs(dirList, koef=0):
    sortDirsList = sorted(dirList.keys())
    for d in sortDirsList:
        print('  ' * koef + d)
        printDirs(dirList[d], koef + 1)
        
printDirs(dirs)
