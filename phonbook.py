

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
    def add_contact(self,name,surname, numberphone,*args,**kwargs):# добавляем контакты
        contact = Contact(name,surname, numberphone,*args,**kwargs)
        self.contact.append(contact)
    def find_contact(self,name): # Поиск контакта по имени
        for contact in self.contact:
            if contact.name == name:
                return contact.__str1__()
    def __str__(self): # Вывод контактов
       for contact in self.contact:
            return f'{contact.name},{contact.surname},{contact.numberphone},{contact.args},{contact.kwargs}'

    def del_contact(self,numberphone):# Удаление контакта по номеру телефона
        for contact in self.contact:
            if contact.numberphone == numberphone:
                self.contact.remove(contact)

    def like_number(self):# Вывод избранных контактов
        for contact in self.contact:
            if 'like' in contact.args:
                return contact.__str1__()

    def adv_find_contact(self,name,surname): # Поиск по имени и фамилии
        for contact in self.contact:
            if contact.name ==name and contact.surname ==surname:
                return contact.__str1__()



ols = Phonbook('jek')
ols.add_contact('Jhon', 'Smith', '+71234567809','like',telegram='@jhony', email='jhony@smith.com')





