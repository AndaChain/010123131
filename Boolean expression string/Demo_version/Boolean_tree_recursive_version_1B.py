variable = ["I0","I1","I2","I3","1","0"]
stack = []
tree_list = [""]*32
#max_position_of_or = 0
stack_or = []
import filter

def Tree(left, right, root, test, q):
    # ******************************preorder********************************
    stack_or = []
    stack_and = []
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
                Is_joke = obj.check_last(test[i+1:])
                #print(Is_joke, test[i], right)
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
    tree_list[q] = root
    tree_list[pl] = left
    tree_list[pr] = right
    # *** (2*q)+1 = left index
    # *** (2*q)+2 = right index
    # *** q = root index

    # meter checking value recursive value
    #print(f"test:{test} \nleft {left} \nroot {root} \nright {right}\n-----------------------")
    if(len(left) == 1):
        tree_list[pl] = left[0]
        if( len(right) > 1):
            Tree("", "", "", right, pr)
        else:
            if(right == ""):
                tree_list[pr] = right
            else:
                tree_list[pr] = right[0]

        return tree_list

    Tree("", "", "", left, pl)

    if( len(right) > 1 ):
        Tree("", "", "", right, pr)
    else:
        #print(pl,q,pr)
        if(right == ""):
            tree_list[pr] = right
        else:
            tree_list[pr] = right[0]

    return tree_list

#((I2&I1)+(I0&I1))
# data set for testing my algorithm
test1 = ["!","(","1","+","0",")"] # OK
test2 = ["!","(","!","(","0","+","I0","&","1",")",")"] # OK

#(I0+!I1+!(I2))&(!I0+I1+I2)
test3 = ["(","I0","+","!","I1","+","!","(","I2",")",")","&","(","!"
        ,"I0","+","I1","+","I2",")"] # OK

#"!(I0&I1)+!(I1+I2)"
test4 = ["!","(","I0","&","I1",")","+","!","(","I1","+","I2",")"]

#"(((I0&I1&!I2)+!I1)+I3)"
test5 = ["(","(","(","I0","&","I1","&","!","I2",")","+","!","I1",")","+","I3",")"]

#((I2&I1)+(I0&I1))
test6 = ["(","(","I2","&","I1",")","+","(","I0","&","I1",")",")"]

#I2&I1+I0&I1
test7 = ["I2","&","I1","+","I0","&","I1"] # OK

#(I0&I1+!(I1&I2))
test_8 = ["(","I0","&","I1","+","!","(","I1","&","I2",")",")"]
q = 0
obj = filter.check_bracket()

print("#",1,"*"*50)
tree_list = [""]*32
print(Tree('','','',test1, q))

print("#",2,"*"*50)
tree_list = [""]*32
print(Tree('','','',test2, q))

print("#",3,"*"*50)
tree_list = [""]*32
print(Tree('','','',test3, q))

print("#",4,"*"*50)
tree_list = [""]*32
print(Tree('','','',test4, q))

print("#",5,"*"*50)
tree_list = [""]*32
print(Tree('','','',test5, q))

print("#",6,"*"*50)
tree_list = [""]*32
print(Tree('','','',test6, q))

print("#",7,"*"*50)
tree_list = [""]*32
print(Tree('','','',test7, q))

print("#",8,"*"*50)
tree_list = [""]*32
print(Tree("","","",test_8, q))