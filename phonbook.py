



class Contact:
    def __init__(self,name,surname, numberphone,*args,**kwargs):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.args = args
        self.kwargs = kwargs


    def __str1__(self):

        def status():
            if 'like' in self.args:
                status = 'да'
            else:
                status = 'нет'
            return status


        def kw ():
            pop =''
            for d,f in self.kwargs.items():
                pop = pop  +f'  {d} : {f}''\n'
            return pop

        def arg ():
            pop1 = ''

            for g in self.args:
                if g != 'like':
                    pop1 = pop1+'   '+g+ '\n'
            return pop1

        return  f'Имя: {self.name}\nФамилия: {self.surname}\nТелефон: { self.numberphone}\nВ избранных: {status()}\nДополнительная информация:\n{arg()}{kw()}'

class Phonbook:
    def __init__(self,name):
        self.name = name
        self.contact = []
    def add_contact(self,new_contact):
        self.contact.append(new_contact.__str1__().split())
        return self.contact

    def __str__(self):
        return self.contact

jhon = Contact('Jhon', 'Smith', '+71234567809', 'like',telegram='@jhony', email='jhony@smith.com')
olga = Contact('Olga', 'Sleptsova', '+79152336956')
sereja = Contact('Sereja','Sleptsov', '+79252206719')

ols = Phonbook('jek')
ols.add_contact(jhon)
ols.add_contact(olga)
ols.add_contact(sereja)

print(ols.__str__())


# def foo(a,b,*args,**kwargs):
#     print(a,b)
#
#     print(args)
#     print(kwargs)
# y = foo(1,2,'Jhon', 'Smith', '+71234567809', n_typl = (), n_list = [])
# print(y)
# dd = (1,2)
# print((lambda x,y: x * y)(dd[0],dd[1]))
