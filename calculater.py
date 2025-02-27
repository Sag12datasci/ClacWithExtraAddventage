def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y 
def div(x,y):
    if (y==0):
        print("Invaild number!")
    else:
        return x/y  #recursion
#Square
def squre(a,b):
    return a**b
#Floor division
def floor(x,y):
    '''Floor division'''
    if (y==0):
        print('Invalid')
    else:
        return x//y
        
    #Fractional 
def factorial(x):  
    '''takes in a number n , returns the factorial of n'''
    if (x==0 or x==1):
        return 1
    else:
        return x*factorial(x-1)

#Febonacci sequance
def febonacci(x):
    if (x==0 ):
        return 0
    elif (x==1):
        return 1
    else :
        return (x-1) + (x-2)
        
#table
def table(x):
    if x==0:
        print('Multiplicative property of zero')
    else:
        print(f'Multiplication of {x} is:')
        for i in range(1,11):
            print(f'{x}X{i}={x*i}')

    

#The operations that we can do with this calculator.
def operations():
    '''Print the available options'''
    print('Select operations')
    print('1.Addition')
    print('2.Subtraction')  
    print('3.Multiplication')
    print('4.Division')
    print('5.Floor Division')
    print('6.square')
    print('7.Fraction')
    print('8.Fibonnaci')
    print('9.Multiplication table')
    print('10.EXIT')
operations()  #call 
#variable
choice=('1','2','3','4','5','6','7','8','9','10')

# main part
while True:
    choice1=input('Enter your choice in (1/2/3/4/5/6/7/8/9/10):')
    print()
    try:
        if choice1 in ('1','2','3','4','5'):
            x=float(input('Enter the first number:'))
            y=float(input('Enter the second number:'))
        elif choice1 in ('7','8','9'):
            x=int(input('Enter the number:'))
        elif choice1 in ('6'):
            a=int(input('Enter the number:'))
            b=int(input('Enter how many times you want to square this:'))
        elif choice1 in ('10'):
            print("Exiting the program...")
            break
        else:
            print('Invalid choice\nChoice in (1/2/3/4/5/6/7/8/9/10)')
            print()
            continue
    except Exception as e:     
        print(f"An error occurred{e}")
        continue
    except KeyboardInterrupt:
        print("Exiting the program")
    if choice1=='1':
        result=add(x,y)
        print(f"{x} + {y} = {result}")
    elif choice1=='2':
        result=sub(x,y)
        print(f"{x} - {y} = {result}")
    elif choice1=='3':
        result=mul(x,y)
        print(f"{x} X {y} = {result}")
    elif choice1=='4':
        result=div(x,y)
        print(f"{x} ÷ {y} = {result}")
    elif choice1=='5':
        result=floor(x,y)
        print(f"{x} ÷ {y} = {result}")
    elif choice1=='6':
        result=squre(a,b)
        print(f'Here is the result:{result}')
    elif choice1=='7':
        result=factorial(x)
        print(f'Here is the result:{result}')

    elif choice1=='8':
        result=febonacci(x)
        print(f'Here is the result:{result}')

    elif choice1=='9':
        result=table(x)
        print(f'Here is the result:{result}')

    next_calculation=input("Let's do another calculation (yes/no): ")
    if next_calculation.lower() =='yes':
            operations()
    elif next_calculation.lower() =='no':
        print ('Thank you')
        break
    else:
        print('Invalid choice\nChoice in (yes/no)')
        last_input=input("Your answer:")
        if last_input.lower() !="yes":
            break
        else:
            continue
    
    