class Boolean_algebra:
    def __init__(self, original):
        self.original = original
        self.stack = ""
        self.operator = [] # contain Operator
        self.operate = []  # contain Operate
        self.operate_unique = [] # contain Operate but every element are unique
        self.original_list = [] # contain a expreesion is split already
        self.op = ["+", "&", "!"]

    def split_expreesion(self):
        self.no_space()
        Str = self.original

        for i, j in zip(  Str, range(len(Str))  ):
            if(i == "("):
                self.original_list.append(i)
                pass
            elif(i in self.op or i == ")"): #if found ")" or operator lets get them to that list!!
                if(i != ")"):
                    self.operator.append(i)

                if(len(self.stack) != 0): # for filter in case that have operator next to bracket
                    self.operate.append(self.stack)
                    self.original_list.append(self.stack)

                    if( self.stack not in self.operate_unique):
                        self.operate_unique.append(self.stack)

                self.original_list.append(i)

                self.stack = "" # and reset stack for other operate
            else:
                self.stack += i # contain operate that have numbers after alphabet on stack
                # in case without bracket in lastest word. I have to append stack on original_list
                if( len(Str) == j+1 and len(self.stack) != 0 ):
                    self.operate.append(self.stack)
                    self.original_list.append(self.stack)

                    if( self.stack not in self.operate_unique):
                        self.operate_unique.append(self.stack)

        return self.original_list

    def no_space(self):
        Str = ""
        for i in self.original: # skip space
            if(i == " "):
                pass
            else:
                Str += i
        self.original = Str

    def get_operator(self):
        return self.operator

    def get_operate(self):
        return self.operate

    def get_original_list(self):
        return self.original_list

# ----------------Testing class--------------------
if( __name__ == "__main__" ):
    testing_data_set = (  "!(1+0)" # index 0
                        , "!(!(0+I0&1))" # index 1
                        , "(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                        , "!(I0&I1)+!(I1+I2)" # index 3
                        , "(((I0&I1&!I2)+!I1)+I3)"  # index 4
                        , "ก10 + ข10") # index 5

    for test in testing_data_set:
        Testing = Boolean_algebra(test)
        print(test,"==>",Testing.split_expreesion())
        print(test,"==>",Testing.operate)
        print(test,"==>",Testing.operate_unique)
        print("-"*100)