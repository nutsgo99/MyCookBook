#-------------------------------------------------------------------------------
# Name:        Recipe Holder
# Purpose:      Hold recipes
#
# Author:      Ashley Collinge
#
# Created:     25/02/2013
# Copyright:   (c) Ashley Collinge 2013
#-------------------------------------------------------------------------------
def menu():
    print "Recipe Holder"
    print "Use the numbers to navigate the menu."
    print ""
    print ""
    print "1) View Recipes"
    print "2) Add Recipes"
    print "3) Delete Recipe"
    print ""
    choice_completed = False
    while choice_completed == False:
        choice = raw_input("")
        if choice == "1":
            choice_completed = True
            view_recipe()
        elif choice == "2":
            choice_completed = True
            add_recipe()
        elif choice == "3":
            choice_completed = True
            delete_recipe()
        else:
            choice_completed = False

def view_recipe():
    print ""
    print ""
    mypath = "/recipe"
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir("H:/Recipes/recipes") if isfile(join("H:/Recipes/recipes",f)) ]
    a = -1
    for i in onlyfiles:
        a = a +1
        print a, i
    print ""
    print "Type in the number of the recipe you would like to view, below and press enter."
    print ""
    choice = input("")
    import os, sys
    print onlyfiles[choice]
    something = str(onlyfiles[choice])
    directory =  "recipes" + "\\" + something
    from itertools import takewhile, imap
    with open(directory) as f:
        items = list(takewhile("heading1".__ne__, imap(str.rstrip, f)))
        print "Recipe for " + directory
        for h in range(len(items)): #following three lines to take the list of recipe and split it by line in to instructions then display
            print str(h)+". "+str(items[h])
    def getColumn(title,file):
        result = []
        global result
        with open(file) as f:
            headers = f.readline().split(',')
            index = headers.index(title)
            for l in f.readlines():
                result.append(l.rstrip().split(',')[index])
            return result

    ingredients = (getColumn("ingredients",directory))
    weight = (getColumn("weight",directory))
    measurement = (getColumn("measurement",directory))
    print directory
    print "Ingredients"
    for i in range(len(ingredients)):
        print ingredients[i]+" "+weight[i]+" "+measurement[i]
    input("")

def delete_recipe():
    print "Delete Recipe"
    print "Type in the number of the recipe you would like to delete, below and press enter."
    mypath = "/recipe"
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir("H:/Recipes/recipes") if isfile(join("H:/Recipes/recipes",f)) ]
    a = -1
    for i in onlyfiles:
        a = a +1
        print a, i
    choice = input("")
    import os, sys
    print onlyfiles[choice]
    something = str(onlyfiles[choice])
    directory =  "recipes" + "\\" + something
    os.remove(directory)

menu()