import random

def get_names():
    lst = []
    with open('data.dat', 'r') as file:
        for i in file:
            lst.append(i.split(',')[0])
        file.close()
        return lst

def set_random_name(lst = get_names()):
    firstname = random.choice(lst)
    lastname = random.choice(lst)
    digs = random.randrange(10000,999999)
    sep = ['', '.', '_']
    name = '%s%s%s%s' %(firstname, random.choice(sep), lastname, digs)
    print(name)

if __name__ == '__main__':
    set_random_name(get_names())