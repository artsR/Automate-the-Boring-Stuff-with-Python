######### CHAPTER 4 ##########


# strings - they are similar to the lists but are immutable

name = 'Zophie'
name[0]
name[-2]
name[0:4]

name[2] = 'Y' #TypeError - string cannot be changed.


'Zo' in name 
'z' in name
'p' not in name

for i in name:
    print('*** ' + i + ' ***')


# tuples - are created by "()" - they are immutable

box = ('hello', 42, 0.5)

box[2] = 99 # not executed. TypeError occurs because tuples are immutable.
