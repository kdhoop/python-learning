# Object-oriented programming practice

class Padawan:

    num_of_padawans = 0
    all_padawans = []
    
    def __init__(self, first, last, age): # "Dunder Init" Double Underscore Init
        self.first = first
        self.last = last
        self.age = age

        Padawan.num_of_padawans += 1
        Padawan.all_padawans.append(self)

    @property
    def email(self): 
        return '{}.{}@corusant-email.com'.format(self.first, self.last)

    @property
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print(f'Deleted Name: {self.fullname}')
        self.first = None
        self.last = None

    @classmethod
    def from_string(cls, jedi_str):
        first, last, age = jedi_str.split('_')
        return cls(first, last, int(age))
    
    def __repr__(self):
        return "Padawan('{}', '{}', {})".format(self.first, self.last, self.age)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.age)
    
    def __add__(self, other):
        return self.age + other.age
    
    def __len__(self):
        return len(self.fullname())


class JediMaster(Padawan):

    num_of_jedi_masters = 0
    all_masters = []

    def __init__(self, first, last, age, padawans=None):
        super().__init__(first, last, age) # Inherit the instances from the master class
        JediMaster.num_of_jedi_masters += 1
        if padawans is None:
            self.padawans = []
        else:
            self.padawans = padawans
        JediMaster.all_masters.append(self)

    @classmethod
    def promote(cls, padawan):
        new_master = cls(padawan.first, padawan.last, padawan.age)
        Padawan.num_of_padawans -= 1
        Padawan.all_padawans.remove(padawan)
        return new_master
    

pad_1 = Padawan('Obi-Wan', 'Kenobi', 25)

pad_1.fullname = 'Yoda Unknown'

print(pad_1.first)
print(pad_1.email)
print(pad_1.fullname)

# del pad_1.fullname

master_1 = JediMaster.promote(pad_1)
print(master_1.fullname)












