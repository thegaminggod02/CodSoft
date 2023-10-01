# Step 1 - Initialisation 
def take_rounds_input(name):
  text_promt = "Hey " + name + " How many rounds would you like to play ? "
  while True:
    rounds = int(input(text_promt))
    if rounds%2 == 1:
      if rounds > 2 and rounds < 10:
        return rounds
        break
      else:
        print("Your number is in not the range of 3 to 9, please enter again ")
    else:
      print('No it a even number, enter again')
      
# Step 3 - Generate a Random Computer selection out of R/P/S
import random
def give_me_a_computer_choice():
  option_list = ('rock','paper','scissor',)
  return random.choice(option_list)
  
# Step 4 - Take player input out of Rock Paper Scissor
def give_me_player_option():
  option = input("R= Rock, P = Paper, S = Scissor - ")
  if option == 'R' or option == 'r':
    return 'rock'
  elif option == 'P' or option == 'p':
    return 'paper'
  elif option == 'S' or option == 's':
    return 'scissor'
  else:
    return give_me_player_option()
    
# Step 5 - Defining Winning Possibility
def check_who_is_winning(computer_input, player_input):
  if player_input == 'scissor' and computer_input == 'scissor':
    return 'draw'
  elif player_input == 'rock' and computer_input == 'scissor':
    return 'player'
  elif player_input == 'paper' and computer_input == 'scissor':
    return 'computer'
  elif player_input == 'scissor' and computer_input == 'rock':
    return 'computer'
  elif player_input == 'rock' and computer_input == 'rock':
    return 'draw'
  elif player_input == 'paper' and computer_input == 'rock':
    return 'player'
  elif player_input == 'scissor' and computer_input == 'paper':
    return 'player'
  elif player_input == 'rock' and computer_input == 'paper':
    return 'computer'
  elif player_input == 'paper' and computer_input == 'paper':
    return 'draw'
  else:
    return "Some error is there in spellings"
    

#recording who is winning in this list

lst = []
lst.append('draw')
lst.append('player')
lst.append('player')

# Recording the Winning Data
def check_ultimate_winner(round_list):
  player = round_list.count('player')
  computer = round_list.count('computer')
  draw = round_list.count('draw')

  if player > computer:
    return "player"
  elif computer> player:
    return "computer"
  else:
    return "draw"



name = input("Please Enter your name - ")
rounds = take_rounds_input(name)
sub_round_winning_lst = []

for i in range(rounds):

  #Take player input
  player_choice = give_me_player_option()
  print("PLayer Choice - ", player_choice)

  #Take computer input
  com_choice = give_me_a_computer_choice()
  print("Computer Choice - ", com_choice)

  # Check who is the winner of the sub round
  sub_round_winner = check_who_is_winning(com_choice, player_choice )
  #store it for later use
  sub_round_winning_lst.append(sub_round_winner)

print("Winner of sub rounds ",sub_round_winning_lst)
print(check_ultimate_winner(sub_round_winning_lst), " wins the Game !!")
