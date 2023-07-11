def arithmetic(num1,num2):
    add=num1+num2
    sub=num1-num2
    multiply=num1*num2
    division=num2/num1
    return add,sub,multiply,division

a,b,c,d=arithmetic(10,20)
print("Addition",a)
print("Subtraction",b)
print("Multiplication",c)
print("Division",d)