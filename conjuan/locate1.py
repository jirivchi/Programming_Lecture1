
class user():

    name='John'
    surname='rivera'
    age=24
    nationality=''
    dictagesender={}

    def fill(self,person):
        print(f'prueba')
        self.name=(input(f'name {person}:'))
        self.surname=(input('surname:'))
        self.age=int(input('age:'))
        self.dictagesender[person]=self.age

        if self.age < 18:
            print('niño es menor')
        else:
            print('niño es mayor de edad')


sender=user()
sender.fill('sender')
print(sender.dictagesender)