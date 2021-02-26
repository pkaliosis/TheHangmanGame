from hangman_functions import *
leksiko=['εικονα', 'ακρογιαλι', 'παραθυρο', 'αναπτηρας', 'πυροσβεστης', 'ορθοπεδικος', 'οφθαλμιατρος', 'αποτελεσμα', 'ισοπαλια', 'καθρεφτης', 'εμπιστοσυνη', 'αδιαφορια', 'βαλιτσα', 'εικασια', 'ελευθερια', 'ισοτητα', 'δικαιοσυνη', 'νερατζι', 'νεροτσουληθρα', 'οπτασια', 'αλαζονεια', 'αλληλεγγυη', 'βυσσοδομω', 'δεισιδαιμονια', 'δωσιλογος', 'κρησφυγετο', 'καλαισθησια', 'ετυμηγορια', 'ευφυια', 'κανελα', 'προσοχη', 'μπαλα', 'ομοφωνια', 'παλιρροια', 'πιρουνι', 'πλημμελημα', 'στιλετο', 'ταξιδι', 'φαράγγι', 'χρεοκοπια', 'χειμαρρος', 'ψιθυρος', 'ευτυχια', 'σκυλος', 'αποδιοπομπαιος', 'αρχαιοκαπηλια', 'ρηξικελευθος', 'καινοτομος', 'απορριμματοφορο', 'τραυματιοφορεας']
participants=int(input('Εισάγετε τον αριθμό παικτών: '))
names=[]
for i in range(participants):
    p=input('Δώσε το όνομα του παίκτη: ')
    names.append(p)
print('')
print('Στο παιχνίδι υπάρχουν 3 επίπεδα δυσκολίας. Το Ε=Εύκολο στο οποίο έχεις 8 ζωές. \nΤο Μ=Μέτριο στο οποίο έχεις 6 ζωές και το Δ=Δύσκολο στο οποίο έχεις 4 ζωές. Κάθε\nφορά που θα έρχεται η σειρά σας θα σας ζητείται να διαλέξετε το επιπεδο \nδυσκολίας στο οποίο θα παίξετε για τον εκάστοτε γύρο.')
rounds=0
player=0
played_the_round=0
lekseis_pg=[]
lekseis_tg=[]
participants2=participants
w=len(names)
round_ended=False
while participants>1 or round_ended==False:
    round_ended=False
    print('Παίζει ο παίκτης: ', end='')
    print(names[player])
    print('Έχεις περιθώριο για 5 λάθος επιλογές γραμμάτων ώστε να βρείς τη λέξη.')
    print('')
    print('Το 6ο λάθος γράμμα σε βγάζει εκτός παιχνιδιού.')
    print('')
    lvl_check=False
    g=1
    while lvl_check==False:
        if g==1:
            lvl=input('Διάλεξε επίπεδο δυσκολίας: ')
            print('')
        else:
            lvl=input('Δώσατε μη υπαρκτό επίπεδο δυσκολίας. Παρακαλώ ξαναπροσπαθήστε, διαλέγοντας ανάμεσα σε Ε=Εύκολο, Μ=Μέτριο και Δ=Δύσκολο. Διαλέξτε επίπεδο δυσκολίας: ')
            print('')
        if lvl=='Ε':
            life=8
            lvl_check=True
        elif lvl=='Μ':
            life=6
            lvl_check=True
        elif lvl=='Δ':
            life=4
            lvl_check=True
        g+=1
    word=random_word(leksiko)
    elegxos_lekshs(word, lekseis_pg, lekseis_tg, leksiko)
    letter=input('Δώσε γράμμα: ')
    lekseis_tg.append(word)
    check1= False
    while check1== False:
        if is_letter(letter)== True:
            check1= True
        else:
            print('Δεν δώσατε γράμμα, παρακαλώ ξαναπροσπαθήστε.')
            letter=input('Δώσε γράμμα: ')
    check2= False
    leksh= word_into_underdashedList(word)
    while life>-1 and check2== False:
        letter_in_word(lvl, letter, word, life, leksh)
        if life_reducer(letter, life, word)== False:
            life-=1
        if dashes_in_list(leksh)==True:
            check2= True
        elif dashes_in_list(leksh)==False and life>-1:
            print('')
            letter=input('Δώσε γράμμα: ')
        elif life==-1:
            participants-=1
            names.pop(player)
            player-=1
    player+=1
    played_the_round+=1
    if played_the_round==participants2:
        if participants>1:
            print('Νέος γύρος!')
        rounds+=1
        player=0
        played_the_round=0
        round_ended=True
        participants2=participants
        lekseis_pg=lekseis_tg
        for k in lekseis_tg:
            lekseis_tg.remove(k)
if participants==1:
    print('Νικητής του παιχνιδιού: ', end='')
    for x in names:
        print(x)
if participants==0:
    print('Δεν υπήρξε κανένας νικητής.')

    
    
        
        
            
    
    
    
    
    
