#!/usr/bin/env python3.8
class Family:
    '''creating a family tree'''
    def __init__(self, GreatGrandParents, GrandParents, Parent):
        pass


print("MOTHER'S SIDE OF FAMILY: ")
class Motherside(Family):
    pass
x = ('Great Grandmother: unknown, Great GrandFather: uknown', 'Grandma: Vero, Grandad: Lenox', 'Mother: Nora')
print(x)

print('\n')

print("FATHER'S SIDE OF FAMILY: ")
class Fatherside(Family):
    pass
x = ('Great Grandmother: unknown, Great GrandFather: uknown', 'Grandma: unknown, Grandad: John', 'Father: Danny')
print(x)

print('\n')


print('MY IMMEDIATE FAMILY: ')
class ImmediateFamily:
     def __init__(self, Mother, Oldest, MiddleSister, TwinBrother, Me):
         self.M = Mother
         self.First = Oldest
         self.Second = MiddleSister
         self.Third = TwinBrother
         self.ThirdAlso = Me

immediate_family = ImmediateFamily('Mother: Nora', 'Sister: Asher', 'Sister: Neesha', 'Brother Twin Khan', 'Me: Shana')
print(immediate_family.M)
print(immediate_family.First)
print(immediate_family.Second)
print(immediate_family.Third)
print(immediate_family.ThirdAlso)

