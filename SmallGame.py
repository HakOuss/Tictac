from tabulate import tabulate
import numpy as np
mat = np.array([[1,2,3],[4,5,6],[7,8,9]])
tab = mat.tolist()
player1 =[]
player2 =[]
def check_pos(pos,player):
    for i in player:
        if i == pos:
            return False
    return True
def get_pos(pos):
    for i in range(3):
        for j in range(3):
            if pos == mat[i,j]:
                x=i
                y=j
                return [x,y]
def check_column(pos,player,mat):
    s=0
    for i in range(len(player)):
        if player[i] in mat[:,pos[1]]:
            s+=1
    return s == 3
def check_line(pos,player,mat):
    s = 0
    for i in range(len(player)):
        if player[i] in mat[pos[0], :]:
            s += 1
    return s == 3
def check_diag(player,mat):
    s = 0
    for i in range(len(player)):
        if player[i] in np.diag(mat):
            s+=1
        elif player[i] in np.diag(np.fliplr(mat)):
            s+=1
    return s == 3
def check_state(pos,player,mat):
    if pos in [2,4,6,8]:
        return check_column(get_pos(pos),player,mat) or check_line(get_pos(pos),player,mat)
    else:
        return check_column(get_pos(pos),player,mat) or check_line(get_pos(pos),player,mat) or check_diag(player,mat)
def X_O(pos,tab,mark):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] == pos:
                tab[i][j] = mark
player = -1
pos = 0
for i in range(9):
    player = -player
    if player > 0:
        while True:
            try:
                pos = int(input("player1 enter the position between 1 and 9:"))
            except ValueError:
                pass
            if pos in range(1, 10) and check_pos(pos,player1) and check_pos(pos,player2):
                player1.append(pos)
                X_O(pos, tab, "X")
                print(tabulate(tab, tablefmt="fancy_grid"))
                if check_state(pos, player1, mat):
                    print("player1 wins")
                break
    else:
        while True:
            try:
                pos = int(input("player2 enter the position between 1 and 9:"))
            except ValueError:
                pass
            if pos in range(1, 10) and check_pos(pos,player2) and check_pos(pos,player1):
                player2.append(pos)
                X_O(pos, tab, "O")
                print(tabulate(tab, tablefmt="fancy_grid"))
                if check_state(pos, player2, mat):
                    print("player2 wins")
                break
    if check_state(pos, player1, mat) or check_state(pos, player2, mat):
        break
if check_state(pos, player1, mat) or check_state(pos, player2, mat):
    pass
else:
    print("draw")