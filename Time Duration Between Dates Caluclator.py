import datetime

print('Welcome to the time elapsed calculator. Enter your desired date & time (24hr format) and it will find the difference from the current time.\n')
Calc_art = '''
 _____________________
|  _________________  |
| | TIME           0. |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________| 
'''
print(Calc_art + '\n')

year = int(input('Enter a year\n'))
month = int(input('Enter a month\n'))
day = int(input('Enter a day\n'))
hour = int(input('Enter an hour\n'))
min =  int(input('Enter a minute\n'))

dt1 = datetime.datetime(year, month, day, hour, min)
dt2 = datetime.datetime.now()



tdelta = dt2 - dt1 
print(tdelta) 
print(type(tdelta)) 
input()