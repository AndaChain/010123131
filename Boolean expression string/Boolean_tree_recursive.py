variable = [["I0"],["I1"],["I2"],["1"],["0"]]
stack = []
tree_list = [""]*100

import filter

def Tree(left, right, root, test, q):
    global max_position_of_or
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
            max_position_of_or = 0
            for j in range(len(test)):
                if(test[j] == "+"):
                    if(max_position_of_or < j):
                        max_position_of_or = j
                    elif(max_position_of_or >= j):
                        max_position_of_or = max_position_of_or
                        
            if(max_position_of_or != 0):
                print(max_position_of_or)
                root = test[max_position_of_or]
                left = test[:max_position_of_or]
                right = test[max_position_of_or+1:]

            if(test[i] == "&"):
                root = test[i]
                left = test[:i]
                right = test[i+1:]

    print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
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
test1 = ["!","(","1","+","0",")"] # Not OK but almost
test2 = ["!","(","!","(","0","+","I0","&","1",")",")"] # Not OK but almost

#(I0+!I1+!(I2))&(!I0+I1+I2)
test3 = ["(","I0","+","!","I1","+","!","(","I2",")",")","&","(","!"
        ,"I0","+","I1","+","I2",")"] # Not OK have to postorder ((((DO LAST))))

#((I2&I1)+(I0&I1))
test_s = ["(","(","I2","+","I1",")","+","(","I0","+","I1",")",")"]
#test_s = ["I2","&","I1","+","I0","&","I1"] # Not OK but almost
q = 0
obj = filter.check_bracket()

print(Tree('','','',test2, q))

# + ตัด ผิกปรกติ ต้องแก้การตัด + คือ ตัด + ที่ตำแหน่งมากสุดแต่ต้องคำนึงถึง () ด้วย
# ! ตัด ผิกปรกติ ต้องแก้การตัด !