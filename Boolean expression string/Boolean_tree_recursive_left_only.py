variable = [["I0"],["I1"],["I2"],["1"],["0"]]
stack = []
tree_list = [""]*100
#max_position_of_or = 0
stack_or = []
import filter

def Tree(left, right, root, test, q):
    stack_or = []
    RUN_OR = True
    test = obj.check_last(test)
    for i in range(len(test)):
        # check "(" and ")"
        if( test[i] == "(" ):
            RUN_OR = False
            stack.append(i)
        elif( test[i] == ")"):
            position = stack.pop()

        # if stack is empty
        if(len(stack) == 0):
            RUN_OR = True

        # filter "!" sinario !(I0&I1), (!I1&I2) and !(I0)
        if(  test[i] == "!" and (test[i+1] in variable or test[i+1] == "(")  ):
            if(RUN_OR == False):
                pass
            elif(RUN_OR == True):
                root = test[i]
                left = test[i+1:]
                right = right
        if(RUN_OR):
            # find the max position of + for split to left root right
            if(test[i] == "+"):
                max_position_of_or = i
                root = test[max_position_of_or]
                left = test[:max_position_of_or]
                right = test[max_position_of_or+1:]
                stack_or.append(max_position_of_or)

            if(test[i] == "&"):
                root = test[i]
                left = test[:i]
                right = test[i+1:]

            if(len(stack_or) > 0):
                root = test[max_position_of_or]
                left = test[:max_position_of_or]
                right = test[max_position_of_or+1:]
            

    #print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
    tree_list[q] = root
    tree_list[(2*q)+1] = left
    tree_list[(2*q)+2] = right
    # *** (2*q)+1 = left index
    # *** (2*q)+2 = right index
    # *** q = root index
    q = (2*q)+1

    if(left in variable):
        return tree_list

    Tree("", "", "", left, q)
    
    # postorder

    return tree_list

#((I2&I1)+(I0&I1))
# data set for testing my algorithm
test1 = ["!","(","1","+","0",")"] # OK
test2 = ["!","(","!","(","0","+","I0","&","1",")",")"] # OK

#(I0+!I1+!(I2))&(!I0+I1+I2)
test3 = ["(","I0","+","!","I1","+","!","(","I2",")",")","&","(","!"
        ,"I0","+","I1","+","I2",")"] # OK

#((I2&I1)+(I0&I1))
test_s1 = ["(","(","I2","&","I1",")","+","(","I0","&","I1",")",")"]

#I2&I1+I0&I1
test_s2 = ["I2","&","I1","+","I0","&","I1"] # OK
q = 0
obj = filter.check_bracket()

print(Tree('','','',test3, q))