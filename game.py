def crosses_wins(map):
    if map[0][0]==map[1][1]==map[2][2]=='+' or map[0][2]==map[1][1]==map[2][0]=='+':
        return True
    for i in range (0,3):
        if map[i][0]==map[i][1]==map[i][2]=='+' or map[0][i]==map[1][i]==map[2][i]=='+':
            return True
    return False

def zeroes_wins(map):
    if map[0][0]==map[1][1]==map[2][2]=='0' or map[0][2]==map[1][1]==map[2][0]=='0':
        return True
    for i in range (0,3):
        if map[i][0]==map[i][1]==map[i][2]=='0' or map[0][i]==map[1][i]==map[2][i]=='0':
            return True
    return False

def correct_move(map,line,column):
    if line in ('1','2','3') and column in ('1','2','3'):
        return map[int(line)-1][int(column)-1]==' '
    return False

map=[[' ',' ',' '],
     [' ',' ',' '],
     [' ',' ',' ']]

print('Welcome the game! To make a move, enter numbers of line and column, where you want your sign to be placed \n')
for i in map:
    print(i)
print(' ')

move=1

crwin=False
zrwin=False

while (not(crwin) and not(zrwin)):

    if move%2==1:
        print('Now crosses \n')
        coordinates=input()
        coordinates=coordinates.split()
        while not(correct_move(map,coordinates[0],coordinates[1])):
            print(' ')
            print('Something has been already placed here or coordinates are outside of map. Please, enter correct coordinates \n')
            coordinates=input()
            coordinates=coordinates.split()
        map[int(coordinates[0])-1][int(coordinates[1])-1]='+'
        print(' ')
        for i in map:
            print(i)
        print(' ')
        move+=1
        crwin=crosses_wins(map)
    
    if crwin:
        print('Crosses wins!')
        break

    if move==10:
        print("It's draw!")
        break

    if move%2==0:
        print('Now zeroes \n')
        coordinates=input()
        coordinates=coordinates.split()
        while not(correct_move(map,coordinates[0],coordinates[1])):
            print(' ')
            print('Something has been already placed here or coordinates are outside of map. Please, enter correct coordinates \n')
            coordinates=input()
            coordinates=coordinates.split()
        map[int(coordinates[0])-1][int(coordinates[1])-1]='0'
        print(' ')
        for i in map:
            print(i)
        print(' ')
        move+=1
        zrwin=zeroes_wins(map)
        
    if zrwin:
        print('Zeroes wins!')