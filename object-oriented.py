# Object-oriented programming practice

class Padawan:

    num_of_padawans = 0
    all_padawans = []
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

        Padawan.num_of_padawans += 1
        Padawan.all_padawans.append(self)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    @classmethod
    def from_string(cls, jedi_str):
        first, last, age = jedi_str.split('_')
        return cls(first, last, age)


class JediMaster(Padawan):

    num_of_jedi_masters = 0
    all_masters = []

    def __init__(self, first, last, age, padawans=None):
        super().__init__(first, last, age)
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


pad_1_str = 'Obi-Wan_Kenobi_29'
pad_1 = Padawan.from_string(pad_1_str)
pad_2 = Padawan('Anakin', 'Skywalker', 17)
print(pad_1.full_name())
print(pad_2.full_name())

master_1 = JediMaster('Yoda', 'Unknown', 700)
print(master_1.age)

master_2 = JediMaster.promote(pad_1)
print(master_2.full_name())








