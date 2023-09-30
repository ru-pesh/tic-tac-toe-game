import random
# random moduele is used to make computer choose a number.
one=[' ','| ',' ','| ',' ']
pr=['-+--+--']
two=[' ','| ',' ','| ',' ']
pr1=['-+--+--']
three=[' ','| ',' ','| ',' ']
print('\t \tWelcome to X O Game')
# the below function is used to add X or O to table but it is also a recursion
def add():
    k=int(input("\nEnter position no. to add"))
    if k in l:
        if k==1:
            one[0]=pl
        elif k==2:
            one[2]=pl
        elif k==3:
            one[4]=pl
        elif k==4:
            two[0]=pl
        elif k==5:
            two[2]=pl
        elif k==6:
            two[4]=pl
            
        elif k==7:
            three[0]=pl
            
        elif k==8:
            three[2]=pl
            
        elif k==9:
            three[4]=pl
        l.remove(k)    
        print(pl,'added succfully on the given position')
    else:
        print('The position is not available\n Enter another position that is vacant')
        add()
            

#The below function is noice.
def pri(a,b,c,d,e):
    all=[a,'\n',b,'\n',c,'\n',d,'\n',e]
    for i in all:
        for j in i:
            print(j,end='')


pl=random.randint(0,2)
if pl==1:
    pl='X'
    b='O'
else:
    pl='O'
    b='X'
print('\nSystem is choosing random player to start first...\n','i chose ',pl,'\n')
    
l=[1,2,3,4,5,6,7,8,9]
for i in range(9):
    pri(one,pr,two,pr1,three)
    
    print("\n\nit is turn of",pl)
    add()
        
            
    w=0
    if i>=4:
        if one[0]==one[2]==one[4]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif two[0]==two[2]==two[4]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif three[0]==three[2]==three[4]==pl:
            print(pl,'wins and', b ,'is a loser hahaha',three)
            w=1
            break
        elif one[0]==two[0]==three[0]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif one[2]==two[2]==three[2]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif one[4]==two[4]==three[4]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif one[0]==two[2]==three[4]==pl:
            print(pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
        elif one[4]==two[2]==three[0]==pl:
            print (pl,'wins and', b ,'is a loser hahaha')
            w=1
            break
    pl,b=b,pl

pri(one,pr,two,pr1,three)
if w==1:
    print('\n\nCongratulations',pl,'You win')
else:
    print('\n\nOOps!! It is a Tie')


    
