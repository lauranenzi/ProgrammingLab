import random


class Person():

    def __init__(self, name, surname):
        # set name and surname
        self.name = name
        self.surname = surname

    def __str__(self):
        return 'Person "{} {}"'.format(self.name, self.surname)

    def say_hi(self):
        #generate a random number between 0,1,2
        random_number = random.randint(0, 2)

        #choose a random geeting
        if random_number == 0:
            print('Hello, I am {} {}.'.format(self.name, self.surname))
        elif random_number == 1:
            print('Hello, I am {}!'.format(self.name))
        elif random_number == 2:
            print('Yo bro! {} here!'.format(self.name))


class Student(Person):

    def __str__(self):
        return 'Student "{} {}"'.format(self.name, self.surname)


class Professor(Person):

    def __str__(self):
        return 'Prof. "{} {}"'.format(self.name, self.surname)

    def say_hi(self):
        print('Hello, I am professor {} {}.'.format(self.name, self.surname))

    def original_say_hi(self):
        return super().say_hi()


student = Student('Mario', 'Rossi')
student.say_hi()

student = Professor('Laura', 'Rossi')
student.say_hi()


class Testo(str):

    def __len__(self):
        return len(self.split(' '))


mio_testo = Testo('Ciao, come va?')
print(len(mio_testo))
