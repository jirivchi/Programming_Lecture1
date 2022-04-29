# User class. ----------------------------------------------------------------+
class User():
    userfirstname = "John"
    userlastname = "Smith"
    useraddress = " "
    usercity = " "
    usercountry = " "
    dictroutecountry = {}
    dictroutecity = {}

    def filloutuser (self,side):

        print(f'*--------------------\u001b[33m {side} Data \u001b[0m---------------------------*')
        self.userfirstname = input(f'{side} firstname: ')
        self.userlastname = input(f'{side} lastname: ')
        self.useraddress = input (f'{side} address -street, number, floor-: ')
        self.usercity = input (f'{side} city: ')
        self.usercountry = input (f'{side} country: ')
        self.dictroutecountry [ side ] = self.usercountry
        self.dictroutecity [ side ]= self.usercity

