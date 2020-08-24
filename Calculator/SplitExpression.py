class SplitExpression:
    def __init__(self, original):
        self.original = original
        self.stack = ""
        self.stack_bracket = []
        self.operator = [] # contain Operator
        self.operate = []  # contain Operate
        self.operate_unique = [] # contain Operate but every element are unique
        self.original_list = [] # contain a expreesion is split already
        self.op = ["+", "-", "*", "/"]
        self.precedence = {"+":1, "-":1, "*":2, "/":2}

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
                    self.original_list.append(self.stack)
        return self.original_list

    def no_space(self):
        Str = ""
        for i in self.original: # skip space
            if(i == " "):
                pass
            else:
                Str += i
        self.original = Str

    def cut_bracket(self, test):
        # put method before for loop in create tree class
        for i in range(len(test)):
            if(test[i] == "("):
                # stack index 0 is "(" and stack index 1 is index where "(" exist
                self.stack_bracket.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.stack_bracket.pop()
                range_bracket = i - position_[1]
                # if "(" and ")" has range same length of subject list cut off both
                if(range_bracket == len(test)-1):
                    return test[1:-1]
        return test # return a list is cut already

    def get_operator(self):
        return self.operator

    def get_operate(self):
        return self.operate

    def get_original_list(self):
        return self.original_list

# ----------------Testing class--------------------
if( __name__ == "__main__" ):
    data_set = ("(500+600) / 7*(1500/30)",)

    Testing = SplitExpression( data_set[0] )
    Testing.split_expreesion()

    print("<-- Operator", Testing.get_operator())
    print("<-- Operate", Testing.get_operate())
    print("<-- Original in List", Testing.get_original_list())