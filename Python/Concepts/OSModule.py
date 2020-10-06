import os

#to get the current directory where you are working you can use the following command:
print(os.getcwd())

#to change the directory where you want to work :
os.chdir('/Users/avije/Documents/Python Training/')
print(os.getcwd())

#now if you create a new file it will get created in the directory that was mentioned in line 7
with open('test.txt','w') as f:
    pass

os.remove('test.txt')

## to create a new folder you can use 'makedirs()' or 'mkdir()'
## makedirs() help creating tree directories whereas mkdir only creates top level directory
# od.makedirs('testfolder/testsubfolder')


## similarly to remove we use removedirs() and rmdir()
# os.removedirs('testfolder/testsubfolder')

## to rename a file we can use:
# os.rename('originalfile','newfile')

## to see the stats of a file we can use:
# print(os.stat('testfolder'))
