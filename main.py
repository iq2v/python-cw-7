class person :
    def init (self, name, age):
         self.name = name
         self.age = age

    def is_adult(self):
        if self.age > 18 :
              return print('you have too much responcibilities')
        else: 
              return print('lucky you')

first_person = person('jana' , 16)
print(first_person.name)
print(first_person.age)
first_person.is_adult()
