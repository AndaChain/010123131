from SplitExpression import * # Split a Expression
import time

class CreateTree:

    def __init__(self):
        self.stack = []
        self.tree_list = [""]

    def Tree(self, left, right, root, test, q):
        # ******************************Preorder********************************
        stack_op = []
        run = True
        test = exp.cut_bracket(test)
        for i in range(len(test)):
            # check "(" and ")"
            if( test[i] == "(" ):
                run = False
                self.stack.append(i)
            elif( test[i] == ")"):
                self.stack.pop()

            # if stack is empty
            if(len(self.stack) == 0):
                run = True

            # 
            if( (test[i] == "-") ):
                if(run == False):
                    pass
                elif(run == True):
                    if( root != "-" ):
                        Is_joke = exp.cut_bracket(test[i+1:])
                        root = test[i]
                        left = Is_joke
                        right = right

            if(run and test[i] in exp.get_operator()):
                if( len(stack_op) == 0):
                    stack_op.append( test[i] )

                if( exp.precedence[ test[i] ] <= exp.precedence[ stack_op[-1] ] ):
                    root = test[i]
                    left = test[:i]
                    right = test[i+1:] 
                stack_op.append(test[i])

        pl = (2*q)+1
        pr = (2*q)+2
        #print(pr, len(self.tree_list), "**************before*************")
        if( pr >= len(self.tree_list) ):
            self.resize()
        #print(pr, len(self.tree_list), "**************after*************")

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
        
        return self.tree_list

    def resize(self):
        print(self.tree_list)
        new_number = 2*( len(self.tree_list)+1 ) -1
        new_one = [""]*new_number

        for j in range(len(self.tree_list)):
            new_one[j] = self.tree_list[j]
        
        self.tree_list = new_one


# ----------------Testing class----------------
if( __name__ == "__main__" ):
    Test_data_set = ( '7/8+5*9-50-7', ) 

    for test,index in zip(   Test_data_set, range (len(Test_data_set))   ):
        exp = SplitExpression(test)
        split_expression = exp.split_expreesion()
        Test = CreateTree()
        print(split_expression)

        print(index,"*"*100)
        result = Test.Tree('','','',split_expression, 0)
        print(result)
        print(index,"*"*100)
