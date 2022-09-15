#!/usr/bin/env python
# coding: utf-8

# In[ ]:


game_list = [0,1,2]


# In[ ]:


def display_game(game_list):
    print("Here is the current list : ")
    print(game_list)


# display_game(game_list)

# In[ ]:


def position_choice():
    choice = 'Wrong'
    
    while choice not in ['0','1','2']:
        
        choice = input("Pick a position (0,1,2) :")
        
        if choice not in ['0','1','2']:
            print("Wrong choice. Pick again :")
    
    return int(choice)
            


# position_choice()

# In[ ]:


def replacement_value(game_list,position):
    user_placement = input("Type a string to place in the position : ")
    
    game_list[position] = user_placement
    
    return game_list


# replacement_value(game_list,1)

# In[ ]:


def gameon_choice():
    
    choice = 'Wrong'
    
    while choice not in ['Y','N']:
        
        choice = input("Keep Playing (Y or N ?) :")
        
        if choice not in ['Y','N']:
            
            print("Sorry I dont understand. Please choose Y or N.")
            
    if choice == 'Y' or choice == 'y':
        return True 
    else:
        return False


# gameon_choice()

# In[ ]:


game_on = True
game_list = [0,1,2]

while game_on:
    
    display_game(game_list)
    
    position = position_choice()
    
    game_list = replacement_value(game_list,position)
    
    display_game(game_list)
    
    game_on = gameon_choice()


# In[ ]:




