import random 

# digits = list(range(10))
# random.shuffle(digits)
# chosen = (digits[:3])
# print(chosen)

# guess = list(input("What is your guess? "))
# guesses = [int(item) for item in guess]
# match_found = False

# def match():
#     for guess_num, chosen_num in zip(guesses, chosen):
#                 if guess_num == chosen_num:
#                     match_found = True
#                     print("Match")
#     if not match_found:
#         print("Close")
        
                
                
# def nope():               
#     for guess_num, chosen_num in zip(guesses, chosen):
#                 if guess_num != chosen_num:
#                     return True 
                
# if match():
#     print("Match")
# elif close():
#     print("close")
# elif nope():
#     print("nope")

# get Guess
def get_guess():
    return list(input("What is your guess? "))

def generate_code():
    digits = [str(num) for num in range(10)]
    
    #Shuffle digits and grab first 3
    random.shuffle(digits)
    return digits[:3]

#Generate clues

def generate_clues(code, user_guess):
    if user_guess == code:
        return "Code Cracked"
    
    clues = []
    
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
            
        elif num in code:
            clues.append("Close")
            
    if clues == []:
        return ["Nope"]
    
    else:
        return clues


secret_code = generate_code() 
clue_report = []

while clue_report != "Code Cracked":
    guess = get_guess()
    clue_report = generate_clues(guess, secret_code)
    print("result of code")
    for clue in clue_report:
        print(clue)
              
    