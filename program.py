import random as r

password = ''
# simple greeting
print('welcome to northen frock', end='********\n')
# this function is our interface to ask the user what they would like to do at the designated atm
def prompt(balance, run=True):
    if run == True:
        try:
            u = int(input('\n[1] Display balance\n[2] Withdraw funds\n[3] Deposit funds\n[9] Return card \n\n'))
            if u == 1:
                balance = displayBalance(balance, view=1)
                print(f'[*] balance: £{balance:.2f}')
            elif u == 2: balance = withdraw(balance)
            elif u == 3: 
                sum = deposit(balance)
                print(f'[*] £{sum:.2f} has been deposited to your account\n[*] balance: £{displayBalance(balance, diff = sum):.2f}')
                balance += sum
            elif u == 9: 
                run = eject()
                exit()
            else: print('**********************************************\n\[*]select a menu optionn\n\n')
        except: 
            print('_________')
            run = False
    
    if run == False: return 'EXIT'
    else: prompt(balance, run)

# function to check for correct password
def passwordCheck(p, t):
    print(f'*** tries: [{t} ', end=']\n')

    while t > 0:
        userP = input('[*] password:')
        if p == userP and t > 0: return True
        elif t == 1: print('\n*** password was incorrectly entered 3 times *** come back later :wave ')

# function to display arbitrary pseudo-random balance generated
def displayBalance(balance, diff = 0.0, view = 1):
    if balance + diff >= 0:
        balance += diff
        if view == 0: print(f'[*] £{(diff * -1):.2f} withdrawn from your account\n[*] Balance: £{balance:.2f}')
        elif view == 1: return balance
    else: print('**********balance too low')

# function to withdraw funds from balance
def withdraw(balance):
  tens = False
  displayValues = ['[1]  10', '[2]  20', '[3]  40', '[4]  60', '[5]  80', '[6]  100', '[7] other amount ', '[8] main menu']
  amounts = {1:10, 2:20, 3:40, 4:60, 5:80, 6:100, 7: 'other'}
  withdrawn = 0

  for display in displayValues[:len(displayValues)]: print(display, end='\n')
  try: user = int(input('[*] select amount: '))
  except: print('type error')

  if user == 7:
    try:
        withdrawn = int(input('[*] enter amount: '))
        if withdrawn % 10 == 0: tens = True
        print('[*] info: withdrawal amount has to be in tens', end=' \n') if tens == False else displayBalance(balance, withdrawn * -1, 0)
    except: return balance
  elif user == 8: return balance
  elif user in amounts.values(): withdrawn = user 
  elif user in amounts.keys(): withdrawn = amounts.get(user)                     # withdrawn = user if user in amounts.values() else amounts.get(user) == 0
  if withdrawn == 0: print('[*] select a valid amount')
  elif displayBalance(balance, withdrawn * -1, view=1) >= 0:
     print(f'£{withdrawn} taken out of atm!')
     balance -= withdrawn   
  return balance

# code to deposit funds into balance
def deposit(balance, accountDetails = None):
    sum = float(input('[*] deposit sum: '))
    if sum > 0: balance += sum
    return sum

# prototype function to eject card after interaction
def eject():
  out = input('\n[*] card ready -_-_  Received? Y/N ')
  if out.upper() == 'Y': out = 'goodbye! '
  else: out = '\n[*] main menu'
  #elif out.upper() == 'N': out = prompt(None)
  print('*', out, '*', sep='*************', end='')
  return False

# code to initialise atm
def welcome(code = 0):
    oldBalance = (float(r.randint(0,500)))
    loggedIn = passwordCheck('atm', t=3)
    if loggedIn == True : prompt(oldBalance)

# exit code
def exit():
    print('\n[*] thanks for using this atm')
    return 

welcome()
