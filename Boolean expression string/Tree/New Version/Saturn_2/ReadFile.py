class Read:
    def __init__(self,path):
        self.files = open(path, "r")
        self.path = path
    
    def getInput(self):
        output = self.files.read()
        return output.split("\n")

if __name__ == "__main__":
    temp = Read("C:\\Users\\s6201012620279\\Software development\\050863\Tree\\New Version\\Input.txt")
    print(temp.getInput())