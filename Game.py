import random
class Game:
    def computer_input(self):
        computer_choice = random.randint(0,2)
        if computer_choice == 0:
            computer_choice = 'K'
        elif computer_choice == 1:
            computer_choice = 'P'
        elif computer_choice == 2:
            computer_choice = 'N'
        print('komputer wybrał!\n')
        return computer_choice
    
    def user_input(self):
        
        user_choice = input('Jaki symbol chcesz wybrać? K, P, N?')
        return user_choice
    
    def run(self,choice,c_choice):
        
        print('Gra sie rozpoczyna')
            
        if choice == c_choice:
            print(f'komputer wybrał {c_choice} gracz wybrał {choice}')
            print('remis')
                
        elif choice == 'K' and c_choice == 'P':
            print(f'komputer wybrał {c_choice} gracz wybrał {choice}')
            print('wygrał komputer')
                
        elif choice == 'P' and c_choice == "N":
            print(f'komputer wybrał {c_choice} gracz wybrał {choice}')
            print('wygrał komputer')
                
        elif choice == 'N' and c_choice == "K":
            print('wygrał komputer')
            print(f'komputer wybrał {c_choice} gracz wybrał {choice}')
                
                
        else: 
            print('wygrał gracz')
            print(f'komputer wybrał {c_choice} gracz wybrał {choice}')
            
            
                
gra = Game()
for i in range(3):
    gra.run(gra.user_input(),gra.computer_input())
