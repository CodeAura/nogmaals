# name of student: Mike
# number of student: 99067408
# purpose of program: Omrekenen van wisselgeld
# function of program: Berekend wisselgeld
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #Het bedrag die de klant moet betalen
paid = int(float(input('Paid amount: ')) * 100) #Het bedrag die de klant heeft betaald
change = paid - toPay #

if change > 0: #
  coinValue = 50 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below:
# Dit zijn if-statements die contant geld laten zien. Bijvoorbeeld een briefje van 20 euro
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    elif coinValue == 0.50:
      coinValue = 0.50
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')