########### CHAPTER 8 ###########

"""
    shelve Module let add Save and Open features to my program.
    I may manage variables easier by saving and open theirs value
    from the file.
                                                                    """

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # I may change the shelf's value as if it were dictionary

print(shelfFile['cats'])

print(list(shelfFile.keys()))   # keys/values return list-like outcome so it is
print(list(shelfFile.values())) # necessary to convert it into list type

shelfFile.close()


"""
    I should use shelve module if I only want to save/read data from my Python
    programs. If I also want to read and modify then in Notepad the better
    choice will be plaintext.
                                """



