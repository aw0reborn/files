## IMPORTS GO HERE
import os
## END OF IMPORTS



### YOUR CODE FOR line_count() FUNCTION GOES HERE ###
def line_count(directory, filename, boool = 0):
    counter = 0
    listoflines = []
    path_of_file = os.path.join(directory, filename)   ### it outputs the path of file
    with open(path_of_file, 'r') as f:   ### file handler
        listoflines = f.read().split('\n')
        if boool is True:
            for i in listoflines:
                for char in i:
                    if char == ' ':
                        break
                    else:
                        counter += 1
                        break
            return counter
        else:
            return len(listoflines)
#### End OF MARKER



### YOUR CODE FOR character_count() FUNCTION GOES HERE ###
def character_count(directory, filename, boool = 0):
    counter = 0
    path_of_file = os.path.join(directory, filename)   ### it outputs the path of file
    with open(path_of_file, 'r') as f:   ### file handler
#         listoflines = f.read().split('\n')
        if boool is True:
            char = f.read()
            for i in char:
                if i.isspace():
                    continue
                else:
                    counter += 1
            return counter
        else:
            char = f.read()
            return len(char)
        
        
#### End OF MARKER



### YOUR CODE FOR move_lines() FUNCTION GOES HERE ###
def move_lines(input_path, output_path, lines=0):
    list1 = []
    counter = 0
    with open(input_path, 'r') as f:
        for i in f:
            list1.append(i.strip())
    with open(input_path, 'r') as f:
        inpt = f.readlines()
        for i in range(lines):
            inpt[i] = ' \n'
    with open(input_path, 'w') as f:
        f.writelines(inpt)
    with open(output_path, 'w') as q:
        for i in list1:
            if lines != counter:
                i = i+('\n')
                q.write(i)
                counter += 1
#### End OF MARKER
