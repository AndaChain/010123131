class check_bracket:
    def __init__(self):
        self.stack = []

    def check_last(self, test):
        # put method before for loop in create tree class
        for i in range(len(test)):
            if(test[i] == "("):
                # stack index 0 is "(" and stack index 1 is index where "(" exist
                self.stack.append([test[i], i])

            elif(test[i] == ")"):
                position_ = self.stack.pop()
                range_bracket = i - position_[1]
                if(range_bracket == len(test)-1):
                    return test[1:-1]
        
        return test

    """def check_not_last(self, index, test):
        # put method in for loop in create tree class
        last = self.check_last(self.test)
        if(last != self.test):
            if(self.test[index] == "("):
                # stack index 0 is "(" and stack index 1 is index where "(" exist
                self.stack.append([self.test[index], index])
                return False
            elif(self.test[index] == ")"):
                position_ = self.stack.pop()
                range_bracket = index - position_[1]
                if(range_bracket < len(self.test)):
                    return True
        else:
            return True
        #self.test = self.check_last(test)
        #print(len(self.stack))
        if(test[index] == "("):
            # stack index 0 is "(" and stack index 1 is index where "(" exist
            self.stack.append([test[index], index])
            return False
        elif(test[index] == ")"):
            position_ = self.stack.pop()
            range_bracket = index - position_[1]
            print(self.stack)
            if(range_bracket < len(test)-1):
                return True"""




