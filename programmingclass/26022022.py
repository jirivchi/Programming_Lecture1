##EVALUATING CONDITIONS
def savings():
    saving=9000
    if saving==0:
        print('Sorry no savings')
    elif saving<1000:
        print('your savings are lows')
    elif saving<10000:
        print('welcome Sr')
    else:
        print('nada')

#savings()

# EVALUATION TWO CONDITIONS WITH "AND" AND "OR" AND "NOT"
message = ''    #mensaje vacio
message = None  #null, no tiene dato





#BUCLE FOR
first=[1,2,3,4,5,6,7]
for n in first:
    if n%2==0:
        print(f'{n} is even')




# EXERCISES

#Identify if number is even and greater than 16. Then print 'Good job'
def evalnumero():
    numero = 8
    even=numero%2
    print(even)
    if even==0 and numero>16:
        print('God Job')
    else:
        print('No good job')
#evalnumero()


minimum=0
for i in (2,3,-5,10,4,8):
    if i<minimum:
        minimum=i
print(f'minimum is {minimum}')



