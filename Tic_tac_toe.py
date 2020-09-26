#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(' ',board[7] + ' | ' + board[8] + ' | ' + board[9],' ')
    print('----------')
    print(' ',board[4] + ' | ' + board[5] + ' | ' + board[6],' ')
    print('----------')
    print(' ',board[3] + ' | ' + board[2] + ' | ' + board[1],' ')


# In[ ]:





# In[2]:


board = ['#','X','O','X','O','X','O','X','O','X','O']


# In[3]:


display_board(board)


# In[4]:


def player_input():
    marker=''
    
    while not(marker == 'X'or marker == 'O'):
        marker = input("Enter a marker X\O : ").upper()
    if marker =='X':
        return ('X','O')
    else:
        return('O','X')


# In[5]:


player_input()


# In[6]:


def place_marker(board,marker,position):
    board[position]=marker


# In[7]:


place_marker(board,'X',4)


# In[8]:


display_board(board)


# In[9]:


def win(board,marker):
    if((board[7]==marker and board[8]==marker and board[9]==marker)or
      (board[4]==marker and board[5]==marker and board[6]==marker)or 
      (board[1]==marker and board[2]==marker and board[3]==marker)or
      (board[7]==marker and board[4]==marker and board[1]==marker)or
      (board[9]==marker and board[6]==marker and board[3]==marker)or
      (board[8]==marker and board[5]==marker and board[2]==marker)or
      (board[7]==marker and board[5]==marker and board[3]==marker)or
      (board[9]==marker and board[5]==marker and board[1]==marker)):
        return True
    else:
        return False
    


# In[10]:


win(board,'O')


# In[11]:


import random
def choose_first():
    num = random.randint(0,1)
    
    if num == 1:
        return('Player 1')
    else:
        return('Player 2')


# In[12]:


choose_first()


# In[13]:


board = ['#','X','O','X','O','X',' ','X',' ','X','O']


# In[14]:


def space_check(board,position):
    return board[position]==''


# In[15]:


space_check(board,6)


# In[16]:


def full_board_check(board):
    isFull = True
    for i in board:
        if i == ' ':
            isFull = False
    return isFull
    


# In[17]:


full_board_check(board)


# In[18]:


def players_choice(board):
    position = 0
    
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Enter your next move : "))


# In[19]:


players_choice(board)


# In[20]:


def reply():
    return input("do you wanna play again Y/N").lower().startswith('y')


# In[21]:


reply()


# In[ ]:


while True:
    board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn +'will play first')
    play_game = input("do you wanna play again Y/N").lower().startswith('y')
    
    if play_game:
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player_1':
            display_board(board)
            position = players_choice(board)
            place_marker = (board, player1_marker, position)
            
            if win(board, player1_marker):
                display_board(board)
                print("Player1 won the game")
                game_on = False
                
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game is draw")
                    
                else:
                    turn = "Player2"
        else:
            display_board(board)
            position = players_choice(board)
            place_marker = (board, player1_marker, position)
            
            if win(board, player1_marker):
                display_board(board)
                print("Player2 won the game")
                game_on = False
                
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Game is draw")
                    
                else:
                    turn = "Player1"
                    
    if not replay():
        break
        

        
        


# In[ ]:




