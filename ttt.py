def fill_tic(tic,player,player_0,player_1):
    if (player==0):
        print(player_0+' where you want to enter')
        n=int(input())
        i=n//3
        j=n%3
        tic[i][j]="x"
        print([tic[x] for x in range(3)])
        check_winner(tic,com)
        # player+=1
        print("helo")
    elif (player!=0):
        print(player_1+'where you want to enter')
        n=int(input())
        i=n//3
        j=n%3
        tic[i][j]="o"
        print([tic[x] for x in range(3)])
        check_winner(tic,com)
        # player-=1
        print("yelo")


def check_winner(tic,com):
    if tic[0][1]==tic[0][2]==tic[0][0]=="x" or tic[1][1]==tic[1][2]==tic[1][0]=="x" or tic[1][1]==tic[2][2]==tic[0][0]=="x" or tic[2][1]==tic[2][2]==tic[2][0]=="x" or tic[0][0]==tic[1][0]==tic[2][0]=="x" or tic[2][1]==tic[1][1]==tic[0][1]=="x" or tic[0][2]==tic[1][2]==tic[2][2]=="x" or tic[2][0]==tic[1][1]==tic[0][2]=="x" :
        com=1
        print(player_0+" is winner")

    elif tic[0][1]==tic[0][2]==tic[0][0]=="x" or tic[1][1]==tic[1][2]==tic[1][0]=="x" or tic[1][1]==tic[2][2]==tic[0][0]=="x" or tic[2][1]==tic[2][2]==tic[2][0]=="x" or tic[0][0]==tic[1][0]==tic[2][0]=="x" or tic[2][1]==tic[1][1]==tic[0][1]=="x" or tic[0][2]==tic[1][2]==tic[2][2]=="x" or tic[2][0]==tic[1][1]==tic[0][2]=="x" :
        com=1
        print(player_1+" is winner")
        
    
    elif " " not in tic[0] and " " not in tic[1] and " " not in tic[2] :
        com=1
        print("match draw")
        
    


print('''\t\t\t    welcome to our game
\tplease fill the block number to enter your input ate your turn
\t\t\t    format of tic tac toe
\t\t\t\t 0 : 1 : 2
\t\t\t\t ---------
\t\t\t\t 3 : 4 : 5
\t\t\t\t ---------
\t\t\t\t 6 : 7 : 8
\t\t\t\t ---------
''')
print("enter the name of players")
player_0=input()
player_1=input()
com=0
player=0
tic=[[" "," "," "],[" "," "," "],[" "," "," "]]

while(com==0):
    fill_tic(tic,player,player_0,player_1)
    if player==0:
        player=1
    else:
        player=0
    # check_winner(tic,com)
# print('where you want to enter')
# n=int(input())
# i=n//3
# j=n%3
# tic[i][j]="x"
# print([tic[x] for x in range(3)])




# def change_player(player){
#     if 
# }




          
