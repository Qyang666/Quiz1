from asyncore import read
from tkinter.tix import COLUMN
import csv
import pandas as pd

'''
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
'''
# create a file object to open the file in read mode
with open('weapons.txt', 'r') as w:
    weapon_data= w.readlines()
print(weapon_data)

# create a csv object from the file object
weapon_csv= csv.reader(weapon_data)
#skip the header row
next(weapon_csv)

#create an empty dictionary named 'weapons_dict'
weapons_dict={}
weapons_dict['name']=[]
weapons_dict['bullets_count']=[]

#use a for loop to iterate through every row of the csv file
import weaponClass as w
for row in weapon_csv:
    #use variables for name,speed and range (optional)
    weapons_dict['name'].append(row[0])
    weapons_dict['bullets_count'].append(w.Weapon(row[0],row[1],row[2]).bullets)
    print("Name:{}".format(row[0]))
    print("Speed:{}".format(row[1]))
    print("Range:{}".format(row[2]))
    print("Bullets:{}".format(w.Weapon(row[0],row[1],row[2]).bullets))
    input("Press any key to fire the weapon")
    while w.Weapon(row[0],row[1],row[2]).bullets >=0:
        w.Weapon(row[0],row[1],row[2]).fire_bullet()
        print("Remaining bullets...", w.Weapon(row[0],row[1],row[2]).bullets, end='\r')

        
#using a loop print out the name and number of bullets from the dictionary
for i,j in weapons_dict.items():
    print(i)
    print(j)
    
    


    



