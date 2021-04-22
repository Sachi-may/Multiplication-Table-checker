import random

#Wrong multiplication table function
def wrongFunction(num):
    wrongValue=random.randint(0,9)
    multiplication_Table=[i*num for i in range(1,11)]
    multiplication_Table[wrongValue]=multiplication_Table[wrongValue]+random.randint(0,9)
    return multiplication_Table

#multiplication table checker function
def tablecheckerFunction(table,num):
    for i in range(1,11):
        if table[i-1] != i*num:
            print ("The wrong index is",[i-1],"and the number is",table[i-1])
    return None

if __name__ == '__main__':
    n=int(input("Enter a number for multiplication table\n"))
    result=wrongFunction(n)
    print(result)
    tablecheckerFunction(result,n)

