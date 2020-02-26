#!/usr/bin/env python3.8
class Family:
    '''creating a family tree'''
    def __init__(self, GreatGrandParents, GrandParents, Parents, Children, ChildOfChilden):
        self.GGP = GreatGrandParents
        self.GP = GrandParents
        self.P = Parents
        self.C = Children
        self.COC = ChildOfChilden

  
print("THE FIRST BORNS ON MOTHER'S SIDE: ")
class motherside(Family):
    pass
x = ('Great Grandmother: unknown', 'Grandma: Vero', 'Mother: Nora','Sister: Asher', 'Niece: Kayla')
print(x)

print('\n')

print("THE FIRST BORNS ON FATHER'S SIDE: ")
class fatherside(Family):
    pass
x = ('Great Grandfather: unknown', 'Grandfather: James', 'Father: Bond','Sister: Beyonce', 'Niece: N/A')
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

