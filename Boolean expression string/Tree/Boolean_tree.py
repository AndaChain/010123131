import Filter # Filter a bracket
import SplitExpression # Split a Expression to a list

class CreateTree:

    def __init__(self):
        self.stack = []
        self.tree_list = [""]*100
        self.variable = ["I0","I1","I2","I3","1","0"]
        self.posfix = []

    def Tree(self, left, right, root, test, q):
        # ******************************Preorder********************************
        stack_or = []
        stack_and = []
        RUN_OR = True
        test = filter.check_last(test)
        for i in range(len(test)):
            # check "(" and ")"
            if( test[i] == "(" ):
                RUN_OR = False
                self.stack.append(i)
            elif( test[i] == ")"):
                self.stack.pop()

            # if stack is empty
            if(len(self.stack) == 0):
                RUN_OR = True

            # filter "!" sinario !(I0&I1), (!I1&I2) and !(I0) etc
            if( (test[i] == "!") ):
                if(RUN_OR == False):
                    pass
                elif(RUN_OR == True):
                    if( root != "!" ):
                        Is_joke = filter.check_last(test[i+1:])
                        root = test[i]
                        left = Is_joke
                        right = right

                #print(RUN_OR)
                #print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
            
            if(RUN_OR):
                # find the max position of + for split to left root right
                if(test[i] == "+"):
                    max_position_of_or = i
                    root = test[max_position_of_or]
                    left = test[:max_position_of_or]
                    right = test[max_position_of_or+1:]
                    stack_or.append(max_position_of_or)

                if(test[i] == "&"):
                    max_position_of_and = i
                    root = test[max_position_of_and]
                    left = test[:max_position_of_and]
                    right = test[max_position_of_and+1:]
                    stack_and.append(max_position_of_and)

                if(len(stack_and) > 0):
                    root = test[max_position_of_and]
                    left = test[:max_position_of_and]
                    right = test[max_position_of_and+1:]
                    
                if(len(stack_or) > 0):
                    root = test[max_position_of_or]
                    left = test[:max_position_of_or]
                    right = test[max_position_of_or+1:]
        
        pl = (2*q)+1
        pr = (2*q)+2
        self.tree_list[q] = root
        self.tree_list[pl] = left
        self.tree_list[pr] = right

        # *** (2*q)+1 = left index
        # *** (2*q)+2 = right index
        # *** q = root index

        # meter checking value recursive value
        print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
        # ######

        # ******************************Postorder********************************
        if(len(left) == 1):
            self.tree_list[pl] = left[0]
            if( len(right) > 1):
                print("###############Postorder###############")
                self.Tree("", "", "", right, pr)
            else:
                if(right == ""):
                    self.tree_list[pr] = right
                else:
                    self.tree_list[pr] = right[0]
            return self.tree_list

        self.Tree("", "", "", left, pl)

        if( len(right) > 1 ):
            print("###############Postorder###############")
            self.Tree("", "", "", right, pr)
        else:
            if(right == ""):
                self.tree_list[pr] = right
            else:
                self.tree_list[pr] = right[0]
        
        print(q)
        return self.tree_list

# data set for testing my algorithm
Test_data_set = (  "!(1+0)" # index 0
                    ,"!(!(0+I0&1))" # index 1
                    ,"(I0+!I1+!(I2))&(!I0+I1+I2)" # index 2
                    ,"!(I0&I1)+!(I1+I2)" # index 3
                    ,"(((I0&I1&!I2)+!I1)+I3)" # index 4
                    ,"((I2&I1)+(I0&I1))" # index 5
                    ,"I2&I1+I0&I1" # index 6
                    ,"(I0&I1+!(I1&I2))" # index 7
                    ,"!!!I1+!!I0" # index 8
                    ,"I1&I0+I3&!!I0" # index 9
                    ,"!!!I0"  ) # index 10


index = 2
q = 0
filter = Filter.check_bracket()
split_expression = SplitExpression.Boolean_algebra(Test_data_set[index]).split_expreesion()
Test = CreateTree()

print(index,"*"*100)
print(  Test.Tree('','','',split_expression, q)  )
print(index,"*"*100)
