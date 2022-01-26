# class Person:
#     pass

# adam = Person()
# print(adam)

# adam.full_name = 'Adam Hayes'
# print(adam.full_name)

#if __name__ == '__main__':
#    main()

## level 2 starts here
# class Person:

#     def __init__(self):
#         pass

# adam = Person()
# print(adam)

# heather = Person()
# print(heather)

## level 3 starts here

# class Person:

#     def __init__(self, full_name = ""):
#         self.full_name = full_name
    
#     # def __str__(self):
#     #     return f"{self.full_name} is a {self.__class__}"


# adam = Person("Adam Hayes")
# print(adam)
# print(adam.full_name)

# heather = Person("Heather Purser")
# print(heather)
# print(heather.full_name)

# aubury = Person("Aubury Orr")

# print(aubury.full_name)

# number = float(2.3)
# print(number)

## level 4 starts here

class Restaurant:

    def __init__(self,name,cuisine,price,rating):
        self.name = name
        self.cuisine = cuisine
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name

class Person:

    def __init__(self, full_name = ""):
        self.full_name = full_name
    
    # def __str__(self):
    #     return f"{self.full_name} is a {self.__class__}"
    
adam = Person("Adam Hayes")
print(adam)
print(adam.full_name)
