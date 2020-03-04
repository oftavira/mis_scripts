import os

class pcitem():

    def __init__(self, itemid, itemloc):
        self.itemid   = itemid
        self.itemloc  = itemloc
        self.uniqueid = self.itemloc+"\\"+self.itemid

class FileBrowser():
    
    def __init__(self, where):
        all_here = [pcitem(files,root) for root, dirs, files in os.walk(where)]
        self.here = where
        self.info = all_here

#Obtenemos la lista de los subdirectorios donde
#nos encontramos
