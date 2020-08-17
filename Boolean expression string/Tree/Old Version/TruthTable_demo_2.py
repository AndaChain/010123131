import SplitExpression
import CreateTree

class TruthTable:
    def __init__(self, expr_str):
        self.expr = SplitExpression.Boolean_algebra(expr_str)
        self.expr.split_expreesion()

        self.bit = len(self.expr.operate_unique)
        self.dict_operate = {}

    def getValOperate(self):
        return self.dict_operate

    def create_table(self, tree_list):
        print(tree_list)
        for j in self.expr.operate_unique:
            #print(f"| {j} |",end="") ###############
            self.dict_operate[j] = 0

        for i in range(2**self.bit):
            if( i == 0 ): # for new line first
                pass
                #print('')
            
            # cut prefix of input
            byte_str = bin(i)[2:]
            
            byte_str = self.add_bit(byte_str)
            self.row(byte_str, tree_list)

    def add_bit(self, byte_str):
        # let add bit every number to same
        if(  len(byte_str) < len(self.expr.operate_unique)  ):
            byte_str = (len(self.expr.operate_unique) - len(byte_str)) *"0"+ byte_str
        #print(  "------"*len(self.expr.operate_unique)  ) ##########
        # return byte that add bit already
        return byte_str

    def row(self, byte_str, tree_list):

        # tree_list!!
        ## outsize --> create_table --> row --> give_value --> calculator --> operation


        # each row have value of operate
        for oper,value in zip(self.expr.operate_unique, byte_str):
            self.dict_operate[oper] = value
            #print( "| "+value+"  |",end="" ) ##########

        #print() #############


        # /////////////I will calculate below/////////////
        print("/"*20,self.dict_operate,"/"*20) ###########
        given = self.give_value(tree_list)
        #print(given) ##############
        self.calculate(tree_list, given)

    def give_value(self, tree_list): # let value to operate
        # create a new list
        index = 0
        new_tree_val = []
        for i in tree_list:
            new_tree_val.append(i)
            
        for oper in tree_list:
            key = self.dict_operate.get(oper)
            #before this if key is only operate
            if(key == None):
                index += 1
                continue
                
            # It is a meter, I guess
            #print(f"{new_tree_val[index]} => {key}, index:{index}") #########
            new_tree_val[index] = key
            index += 1

        #print("*"*50) ##########
        return new_tree_val
        
    def calculate(self, tree_list, given_list):
        # create a new list
        new_tree_list = [] # for compound expression
        for i in tree_list:
            new_tree_list.append(i)

        # start calculating with far left
        pl = (len(given_list)-1) // 2 # left
        q = (pl - 1)//2 # root

        while(pl != 10):
            q = (pl - 1)//2 # root
            pr = pl + 1 # right

            if(pl == 0):
                q = pl # root
                pl = (2*q) + 1 # left
                pr = (2*q) + 2 # right
            
            left_checking = tree_list[pl] in self.expr.operate_unique
            right_checking = tree_list[pr] in self.expr.operate_unique

            left_expr_checking = tree_list[pl] not in self.expr.operate_unique and tree_list[pl] not in self.expr.operator and tree_list[pl] != ""
            right_expr_checking = tree_list[pr] not in self.expr.operate_unique and tree_list[pr] not in self.expr.operator and tree_list[pr] != ""
            
            print("********************"+" |left:"+str(pl)+"|root:"+str(q)+"|right:"+str(pr)+"| "+ "********************")
            if(   ((left_expr_checking or left_checking) and (right_checking or right_expr_checking) ) 
                or ( (left_checking or left_expr_checking) and tree_list[pr] == "" )    ): # UP!! 
                # can calculate
                result_exprForm = self.operation(pl, q, pr, tree_list, given_list)
                #print(result_exprForm[0], result_exprForm[1])
                given_list[q] = result_exprForm[0]
                tree_list[q] = result_exprForm[1]
                #print("wwwwwwwwwwwwwwwwwwwwww",tree_list[q],"wwwwwwwwwwwwwwwwwwwwww")
                # let left child is root
                #  Example:      
                #              q--> &
                #                  /  \
                #          pl--> I0    I1

                print("(" + "|left:" + tree_list[pl] + "|root:" + tree_list[q] + "|right:" + tree_list[pr] + ") 1\n")
                
                if(q%2 == 0):
                    pl = q-1
                else:
                    pl = q
            elif( (left_checking or right_checking) or (left_expr_checking or right_expr_checking) ): # Down!!
                # can't calculate

                if( left_checking or left_expr_checking ): # left is operate
                    
                    # let left child is left child of right child therefore 
                    # "right child is root"
                    #  Example:      
                    #               q-->&
                    #                  /  \
                    #                I0    + <--pr
                    #                     /
                    #       (2*pr)+1--> I3    
                    
                    print("(" + "|left:" + tree_list[pl] + "|root:" + tree_list[q] + "|right:" + tree_list[pr] + ") 2.R\n")
                    pl = (2*pr) + 1


                else: # right is operate

                    # let left child is left child of left child therefore 
                    # "left child is root"
                    #  Example:      
                    #               q-->&
                    #                  /  \
                    #          pl--> +     I2  
                    #               /     
                    # (2*pl)+1--> I3
                        
                    print("(" + "|left:" + tree_list[pl] + "|root:" + tree_list[q] + "|right:" + tree_list[pr] + ") 2.L\n")
                    pl = (2*pl)+1
            
            elif( tree_list[pl] == "" ): # left and right is blank # Up!!
                # can't calculate
                # let left child is root
                #  Example:      
                #              q--> I0
                #                  /  \
                #          pl--> ()    ()   

                print("(" + "|left:" + tree_list[pl] + "|root:" + tree_list[q] + "|right:" + tree_list[pr] + ") out\n")
                pl = q

            else: # left and right is operator # Down!!
                # let left child is left child of left child therefore 
                # "left child is root"
                #  Example:      
                #               q-->&
                #                 /  \
                #          pl--> +    +  
                #               /     
                # (2*pl)+1--> I3    

                print("(" + "|left:" + tree_list[pl] + "|root:" + tree_list[q] + "|right:" + tree_list[pr] + ") 3\n")   
                pl = (2*pl)+1

    def operation(self, left, root, right, tree_list, given_list):
        if( tree_list[root] == "!" ):
            # make exprssion for writh in truth table
            expression_form = "(" + tree_list[root] + tree_list[left] + ")"
            #######

            # calculate time!!
            if( given_list[left] == "1" ):
                return ( "0", expression_form ) 
            else:
                return ( "1", expression_form )

        elif( tree_list[root] == "&" ):
            # make exprssion for writh in truth table
            expression_form = "(" + tree_list[left] + tree_list[root] + tree_list[right] + ")"
            #######

            # calculate time!!
            if( given_list[left] == "1" and given_list[right] == "1" ):
                return ( "1", expression_form ) 
            else:
                return ( "0", expression_form )

        elif( tree_list[root] == "+" ):
            # make exprssion for writh in truth table
            expression_form = "(" + tree_list[left] + tree_list[root] + tree_list[right] + ")"
            #######

            # calculate time!!
            if( given_list[left] == "1" or given_list[right] == "1" ):
                return ( "1", expression_form ) 
            else:
                return ( "0", expression_form )

            

if __name__ == "__main__":
    # Create Tree
    table = TruthTable("(I0+!I1+!(I2))&(!I0+I1+I2)")
    #table = TruthTable("A+B")
    tree = CreateTree.CreateTree()
    tree_list = tree.Tree("", "", "", table.expr.original_list, 0)
    
    # TruthTable
    table.create_table(tree_list)

