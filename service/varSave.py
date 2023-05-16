import json
import os

class VarSaveService:
    def __init__(self,filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename,'w') as f:
                json.dump({},f,indent=4)
        self.varSave = self.getVarSave()
    
    def getVarSave(self):
        try:
            with open(self.filename,'r') as f:
                return json.load(f)
        except:
            return {}
    
    def saveVar(self,varName,varValue):
        self.varSave[varName] = varValue
        with open(self.filename,'w') as f:
            json.dump(self.varSave,f,indent=4)
    
    def getVar(self,varName):
        try:
            return self.varSave[varName]
        except:
            self.saveVar(varName,True)
    
    def deleteVar(self,varName):
        del self.varSave[varName]
        with open(self.filename,'w') as f:
            json.dump(self.varSave,f,indent=4)
    