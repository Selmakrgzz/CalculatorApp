#Operations
def addition(num1, num2):
    sum=int(num1)+int(num2)
    return sum

def subtraction(num1, num2):
    sum=int(num1)-int(num2)
    return sum

def multiplication(num1, num2):
    sum=int(num1)*int(num2)
    return sum

def division(num1, num2):
    sum=int(num1)/int(num2)
    return sum

def modulo(num1, num2):
    sum=int(num1)%int(num2)
    return sum

def square():
    return 0

def percentage():
    return 0

#Converting the equation to an array
def inputAppend(input):
    result=[]
    num=''
    for i in input:
        if i.isdigit():
            num+=str(i)
        else:
            if num: #If num is not emty(holding a number)
                result.append(int(num))
                num=''
            result.append(i)
    if num:
        result.append(int(num))
    return result

def calculate(equation):
    list = inputAppend(equation)
    
    #print(list)
    sum=0
    num1=0
    num2=0
    operand=''

    for i in range(0, len(list), 1):
        if isinstance(list[i], int): #Checking if the val is an int
            if operand == '': #If the operand is an emty string, then there is a num there
                num1=list[i] #Assigning num1 to val on index i
                #print(f"num nr{i}: {num1}") 
            else:
                num2=list[i] #If the operand is not emty(we have passed an operand), we'll assign the num2 to the second val
                #print(f"num nr{i}: {num2}")
                if operand == '+': #If the operand is the given operation
                    sum=addition(num1, num2)
                if operand == '-': #If the operand is the given operation
                    sum=subtraction(num1, num2)
                if operand == '*': #If the operand is the given operation
                    sum=multiplication(num1, num2)
                if operand == '/': #If the operand is the given operation
                    sum=division(num1, num2)
                if operand == '%': #If the operand is the given operation
                    sum=modulo(num1, num2)
                operand='' #Emtying the operand string for next loop
                num1=sum #Setting num1 to sum
        elif isinstance(list[i], str): #Checking if the val is a string aka an operand
            operand=list[i] #Assigning the val to the operand variable


    return sum

