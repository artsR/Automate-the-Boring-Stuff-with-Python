def collatz (number) :
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print('Enter number, my friend:')

while True:
    try:
        parameter = int(input())
        break
    except ValueError:
        print('The input should be an integer number. Please, try again.')
    
    

while True:
    parameter = collatz(parameter)
    print(parameter)
    if parameter == 1:
        break
    
