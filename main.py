#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint


# In[ ]:


print("Greetings, Welcome to the Void")
print('...')
print('......')
print('.........')
print('............')


# In[ ]:


hasplayed = input('Have you played before? Yes or No? ')

while hasplayed != 'yes' or hasplayed !='no':
    if hasplayed.lower() == 'no':
        username = str(input("What's your name? "))
        with open(username + '_saved_userdata.txt',mode='w') as userdata:
            userdata.write(username + "'s" + ' \nSaved Data\n')
            userdata.close()
            break
    elif hasplayed.lower() == 'yes':
        username = str(input("Remind me, what's your name again? "))
        print('Welcome back ' + username + '!')
        break
    else:
        hasplayed = str(input('Try again. Yes or No? ')).lower()




# In[ ]:


if hasplayed.lower() == 'no':
    print("Let's play.\n")
    print("The rules are simple.\n")
    print("...\n......\n.........")
    print("I'll think of a number 1 to 100.\n Your job is to give your best guess.\n To make things a little more fair, I'll even give you hints each guess to tell you if you are 'Warmer' or 'Colder'.\n When you win, I'll say'YOU WIN!!'\n")
    com_num = randint(1,100)
    print("Alright, I got a number")
    com_guess = {'Guess' : com_num}
elif hasplayed.lower() == 'yes':
    rog = str(input('Do you want me to explain the rules of the game again? '))
    while rog != 'yes' or rog != 'no':
        if rog.lower() == 'yes':
            print("The rules are simple.\n")
            print("...\n......\n.........")
            print("I'll think of a number 1 to 100.\n Your job is to give your best guess.\n To make things a little more fair, I'll even give you hints each guess to tell you if you are 'Warmer' or 'Colder'.\n When you win, I'll say'YOU WIN!!'\n")
            com_num = randint(1,100)
            print("Alright, I got a number.")
            com_guess = {'Guess' : com_num}
            break
        elif rog.lower() == 'no':
            com_num = randint(1,100)
            print("Alright, I got a number.")
            com_guess = {'Guess' : com_num}
            break
        else:
            rog = str(input("Try again. 'Yes' or 'No' "))


# In[ ]:


user_guess = int(input('Pick a number 1 to 100\n'))
attempts = 1
guess_data = []
within_ten = abs(user_guess - com_num) <= 10
not_within_ten = abs(user_guess - com_num) > 10


while user_guess != com_num:
    if 100 < user_guess or user_guess < 1:
        user_guess = int(input("'OUT OF BOUNDS\n TRY AGIAN.\n'"))
        attempts = attempts + 1
        guess_data.append('OUT OF BOUNDS')
        continue
    elif attempts == 1 and within_ten == True:
        attempts = attempts + 1
        guess_data.append(user_guess)
        last_within = abs(user_guess - com_num)
        user_guess = int(input("'YOU ARE WARM!' \n"))
        continue
    elif attempts == 1 and not_within_ten == True:
        attempts = attempts + 1
        guess_data.append(user_guess)
        last_within = abs(user_guess - com_num)
        user_guess = int(input("'YOU ARE COLD!' \n"))
        continue
    elif attempts >= 2 and abs(user_guess - com_num) < last_within:
        attempts = attempts + 1
        guess_data.append(user_guess)
        last_within = abs(user_guess - com_num)
        user_guess = int(input("'WARMER!' \n"))
        continue
    elif attempts >= 2 and abs(user_guess - com_num) > last_within:
        attempts = attempts + 1
        guess_data.append(user_guess)
        last_within = abs(user_guess - com_num)
        user_guess = int(input("'COLDER!' \n"))
        continue
    else:
        user_guess = int(input('Nope, sorry.\nTry again.\n'))
        guess_data.append(user_guess)
        continue

print('Great guess!!!\n')
print('I was thinking ' + str(com_num) + '.\nAnd you got it in ' + str(attempts) + ' guesses!\n')
print('YOU WIN!!!\n')


# In[ ]:


with open(str(username) + '_saved_userdata.txt',mode='a') as userdata:
           userdata.write('\n' + str(guess_data))
           userdata.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




