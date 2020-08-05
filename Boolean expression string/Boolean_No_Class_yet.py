def make_array(origin):
    #origin = "(I0&I1 + !(I1&I2))"
    n = len(find(origin)[0])
    A = ['None']
    i = 0
    while n >= 2**i:
        i += 1
        temp = (2**i)-1
    return A*temp

def tree(origin, array):
    origin_slide = origin[2]
    origin_not = []
    for j in origin[0]:
        origin_not.append("!"+j)
    q = 0
    for i in origin_slide:
        if(i == "!"):
            index = origin_slide.index(i)
            if(origin_slide[index+1] in origin[0]):
                origin_slide[index+1] = "!"+origin_slide[index+1]
            elif(origin_slide[index+1] == "("):
                origin_slide[index+2] = "!"+origin_slide[index+2]
                origin_slide[index+4] = "!"+origin_slide[index+4]
                
                if(origin_slide[index+3] == "&"):
                    origin_slide[index+3] = "+"
                elif(origin_slide[index+3] == "+"):
                    origin_slide[index+3] = "&"
            #print(origin_slide[index],"*****")
            origin_slide.remove(i)

    for i in origin_slide:
        pl = (2*q)+1
        pr = (2*q)+2
        if i == '(':
            if array[pl] == 'None':
                q = pl
            else:
                q = pr       
        elif i in origin[0] or i in origin_not: # I ล้วนๆ
            if array[pl] in origin[0] or array[pl] in origin_not or array[pl] in ["+", "&", "!"]:
                array[pr] = i
            else:
                array[pl] = i
        elif i in ["+", "&", "!"]: # operator ล้วนๆ
            array[q] = i
        elif i == ')':
            if q%2 == 1:
                q = int((q-1)/2)
            elif q%2 == 0:
                q = int((q-2)/2)

    return array

def find(Str):
    storage_op = []
    storage_I0 = []
    storage_I0_ = []
    op = ["+", "&", "!", "(", ")"]
    char = [chr(i) for i in range(65,91)]
    number = [str(i) for i in range(10)]
    for i in range(len(Str)):
        if(Str[i] != " "):
            try:
                #I1
                if(Str[i] in char and Str[i+1] in number):
                    storage_I0.append(Str[i]+Str[i+1])
                    storage_I0_.append(Str[i]+Str[i+1])

                #I&
                if(Str[i] in char and Str[i+1] in op):
                    if(Str[i] not in number):
                        storage_I0.append(Str[i])
                        storage_I0_.append(Str[i]+Str[i+1])
                
                #&?
                if(Str[i] in op):
                    if(Str[i] in op[:3]):
                        storage_op.append(Str[i])
                    storage_I0_.append(Str[i])

                #1,0?
                if(Str[i+1] == "1" or Str[i+1] == "0"):
                    if(Str[i] not in char or Str[i] in op):
                        storage_I0.append(Str[i+1])
                        storage_I0_.append(Str[i]+Str[i+1])

            except IndexError:
                pass

    return storage_I0, storage_op, storage_I0_

original = "(I0&I1)+!(I1&I2)"
array = make_array(original)
print(tree(find(original), array))