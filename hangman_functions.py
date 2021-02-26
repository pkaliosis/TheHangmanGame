import random
def print_figure(lvl, life):
    figure={}
    for i in range(7):
        for j in range(14):
            figure[i,j]= ' '
    if lvl=='Ε':
        if life==8:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
        elif life==7:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
        elif life==6:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
        elif life==5:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[2,10]='/'
        elif life==4:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
        elif life==3:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
        elif life==2:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
        elif life==1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
        elif life==0:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
        elif life==-1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]='|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
            figure[6,10]='f'
            figure[6,11]='i'
            figure[6,12]='r'
            figure[6,13]='e'
    elif lvl=='Μ':
        if life==6:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
        elif life==5:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
        elif life==4:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
        elif life==3:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[2,11]='|'
            figure[3,11]='|'
        elif life==2:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[4,9]='_/'
        elif life==1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[4,9]='_/'
            figure[4,11]='\\_'
        elif life==0:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
        elif life==-1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
            figure[6,10]='f'
            figure[6,11]='i'
            figure[6,12]='r'
            figure[6,13]='e'
    elif lvl=='Δ':
        if life==4:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
        elif life==3:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
        elif life==2:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
        elif life==1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
        elif life==0:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
        elif life==-1:
            for i in range(7):
                for j in range(14):
                    figure[i,0]= '|'
                    if i==0 and j<=10 and j>0:
                        figure[i,j]= '-'
            figure[0,11]='|'
            figure[1,11]='o'
            figure[2,11]='|'
            figure[3,11]='|'
            figure[2,10]='/'
            figure[2,12]='\\'
            figure[4,9]='_/'
            figure[4,11]='\\_'
            figure[5,9]='#'
            figure[5,10]='#'
            figure[5,11]='#'
            figure[5,12]='#'
            figure[5,13]='#'
            figure[6,10]='f'
            figure[6,11]='i'
            figure[6,12]='r'
            figure[6,13]='e'
    for i in range(7):
        for j in range(14):
            if j<13:
                print(figure[i,j], end='')
            else:
                print(figure[i,j])
    return None
            
        
            
            
            
            
            
            
    
def random_word(lista):
    x= random.choice(lista)
    return x

def word_into_underdashes(word):
    """Returns as many underdashes as the length of the given word.

    >>> word_into_underdashes('Hello')
    _ _ _ _ _ 
    >>> word_into_underdashes('World')
    _ _ _ _ _ 
    >>> word_into_underdashes('word')
    _ _ _ _ 
    """
    kena=[]
    x=len(word)
    for i in range(x):
        kena.append('_ ')
    for i in range(x):
        if i<x:
            print(kena[i], end='')
        else:
            print(kena[i])
    return None

def elegxos_lekshs(word, lista_pg, lista_tg, leksiko):
    done= False
    while done== False:
        if word in lista_pg or word in lista_tg:
            word= random_word(leksiko)
        else:
            done= True
    print('Η λέξη που πρέπει να μαντέψεις είναι: ', end=''), word_into_underdashes(word)
    

def word_into_underdashedList(word):
    """Returns a list with as many underdashes as the length of the given word.
    >>> word_into_underdashedList('game')
    ['_ ', '_ ', '_ ', '_ ']
    >>> word_into_underdashedList('player')
    ['_ ', '_ ', '_ ', '_ ', '_ ', '_ ']
    """
    kena=[]
    x=len(word)
    for i in range(x):
        kena.append('_ ')
    return kena

def letters_of_the_word(word):
    """Returns the letters of the given word into a list.
    >>> letters_of_the_word('hangman')
    ['h', 'a', 'n', 'g', 'm', 'a', 'n']
    >>> letters_of_the_word('python')
    ['p', 'y', 't', 'h', 'o', 'n']
    """
    leksh=[]
    n=len(word)
    for i in range(n):
        leksh.append(word[i])
    return leksh

def dashes_in_list(lista):
    """Checks if there are any underdashes in the given list.
        Returns True if there are 0 underdashes.
        Returns False if there are >=1 underdashes.
    >>> dashes_in_list([1,2,3])
    True
    >>> dashes_in_list(['a', '_ ', 'b', 'c'])
    False
    """
    k=0
    n=len(lista)
    for i in range(n):
        if lista[i]== '_ ':
            k+=1
    if k==0:
        return True
    else:
        return False

def letter_in_word(lvl, k, word, life, leksh):
    word2=letters_of_the_word(word)
    n=len(word2)
    if k in word2:
        for i in range(n):
            if word2[i]==k:
                leksh[i]=k
        print('Η λέξη που πρέπει να μαντέψεις είναι: ', end='')
        for i in range(n):
            if i<n-1:
                print(leksh[i], end='')
            else:
                print(leksh[i])
    else:
        life-=1
        print_figure(lvl, life)
        if life>-1:
            print('Έχεις ακόμα', life, 'ζωές.')
            print('Η λέξη που πρέπει να μαντέψεις είναι: ', end='')
            for i in range(n):
                if i<n-1:
                    print(leksh[i], end='')
                else:
                    print(leksh[i])
        else:
            print('Λυπάμαι, έχασες!')
            print('Η λέξη που έψαχνες ήταν: ', end='')
            print(word)
            print('')
                
    
def life_reducer(k, life, word):
    """Checks if the given letter is in the given word.
        If there is, the function returns True. Else, it returns False.
    >>> life_reducer('a', 4, 'play')
    True
    >>> life_reducer('b', 3, 'play')
    False
    """
    word2=letters_of_the_word(word)
    n=len(word2)
    if k in word2:
        return True
    else:
        return False

def is_letter(k):
    """Checks if the given string is a letter.
        If it is, then the function returns True. Else, it returns False.
    >>> is_letter('a')
    True
    >>> is_letter('word')
    False
    """
    if len(k)==1:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
