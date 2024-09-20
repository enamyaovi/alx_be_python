# A pattern generator

user_input = int(input('Enter the size of the pattern: '))

i = 0

while i < user_input:
    #print(f'{i+1}',end='') #row labeller
    for j in range(user_input):
        print('*', end="")
    i += 1
    print()
