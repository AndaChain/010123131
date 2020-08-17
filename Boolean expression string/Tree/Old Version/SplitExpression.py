class Boolean_algebra:
    def __init__(self, original):
        self.original = original
        self.operator = [] # contain Operator
        self.operate = []  # contain Operate
        self.original_list = [] # contain a expreesion is split already
        self.op_include_bracket = ["+", "&", "!", "(", ")"]
        self.binary = ["0", "1"]
        self.char = [chr(i) for i in range(65,91)] # contain alphabet A-B only upper case
        self.number = [str(i) for i in range(10)] # contain number 0-9 only upper case

    def split_expreesion(self):
        Str = self.original
        char = self.char
        number = self.number

        for i in range(len(Str)):
            if(Str[i] != " "):
                try:
                        
                    # Operate with number 0-9
                    if(Str[i] in char and Str[i+1] in number):
                        self.operate.append(Str[i]+Str[i+1])
                        self.original_list.append(Str[i]+Str[i+1])

                    # Operate only
                    if(Str[i] in char and Str[i+1] not in number):
                        self.operate.append(Str[i])
                        self.original_list.append(Str[i])

                    # Operate and, or, not, (, )
                    if(Str[i] in self.op_include_bracket):
                        if(Str[i] in self.op_include_bracket[:3]): #not include bracket
                            self.operator.append(Str[i])
                        self.original_list.append(Str[i])

                    # Binary
                    elif(Str[i] in self.binary):

                        if(i-1 == -1):
                            self.operate.append(Str[i])
                            self.original_list.append(Str[i])

                        if( (Str[i+1] in self.op_include_bracket
                            and Str[i-1] in self.op_include_bracket) ):

                            self.operate.append(Str[i])
                            self.original_list.append(Str[i])

                except IndexError:
                    # Run this section when index is last

                    # Binary
                    if(Str[i] in self.binary and Str[i-1] not in char):
                        self.operate.append(Str[i])
                        self.original_list.append(Str[i])

                    # Operate only
                    if(Str[i] in char):
                        self.operate.append(Str[i])
                        self.original_list.append(Str[i])
        
        return self.original_list

"""# ----------------Testing class--------------------
testing_data_set = (  "!(1+0)" # index 0
                    , "!(!(0+I0&1))" # index 1
                    , "(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                    , "!(I0&I1)+!(I1+I2)" # index 3
                    , "(((I0&I1&!I2)+!I1)+I3)"  ) # index 4

for test in testing_data_set:
    Testing = Boolean_algebra(test)
    print(test,"==>",Testing.split_expreesion())
    print("-"*100)"""