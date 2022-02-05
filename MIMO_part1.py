# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4  2022

@author: Pierluigi De Rogatis
"""

# MIMO EXERCISES AND PROJECTS - PART 1


'''
# 1. PYTHON BASICS
# 1.1 LOCATION DATA
Aim to use variables to record data points as countries' name.
Therefore, first I will create a variable and I will assign the name of the 
continent, of the country, of the county, of the city, and data ID: 
'''

continent = "Europe"
country = "United Kingdom" 
county = "Essex"
city = "Colchester"
Country_ISO = 826


'''
# 1.2 SMART LIGHT SWITCH
Aim to create a programme that swith on and off the light based on daytime
First, I created a variable "day" in which store if it is daytime or not. 
Then I created a second variable where to insert if to switch the 
light on or off. 
I used the "not" function since the light_on variable need to do the opposite 
than day variable.
Since I have to store longer value of explanation, I will use the three 
apostrophe function to accomplish such task.
'''

day = False
lights_on = not day 

'''
Then, I will use the "print" function to display the result of my input.
In other words, I will ask if it daytime and if the programme needs to 
switch on the lights, replying with the previously stored data. 
'''

print("Daytime?")
print(day)

print("Lights on?")
print(lights_on)


'''
# 1.3 TRACK SALESE DATA
Aim to track the sales data for an online shop to see if reached the sell target.
Firstly, I will store the value of the book stock, book sold, and sell target 
inside their correspective variables.
'''

book_stock = 600
book_sold = 500
sell_target = 500

'''
Then, I will use the "==" operator to understand if the shop reached the target
or not. Since the reply will be True or False (boolean), then I will ask the 
programme if the sale target was hit or not. Hence:
'''

target_done = book_sold == sell_target
print("Hit books sale target:")
print(target_done)

'''
Then, to understand if there are still books in the store, I will subtract the
amount of books sold to the number of book in stock. After that, I will use 
"!=" (not equal operator) to udnerstand if the shop has still something in stock.
Since the reply will be True or False (boolean), then I will ask the 
programme if there is still something or not. Hence:
'''

current_stock = book_stock - book_sold
in_stock = current_stock != 0
print("Books in stock:")
print(in_stock)



'''
# 2. TYPES AND COMPARISONS
# 2.1 MEASURE HEART RATE DATA
With this programme, I will display if the heart rate, stored in a variable
named "heart_rate" is too elevated or too low. For this task, I will employ
"<" (less than operator) and ">" (greater than operator). Thus:
'''

heart_rate = 64

too_low = heart_rate < 55
too_high = heart_rate > 120

print("Heart rate too low:")
print(too_low)

print("Heart rate too high:")
print(too_high)


'''
# 2.2 SURVEY DATA INSIGHTS
Aim to use string comparisons to label data acquired through a survey
For this reason, I created two variables to collect the results of the 
survey. Then, I used some coding to assess the level of activity and intensity
of the respondant. Thus:
'''

frequency = "never"
intensity = "low"

high_active = frequency == "daily"
print("Highly active user:")
print(high_active)

low_active = frequency == "once a week"
print("Low active user:")
print(low_active)

non_active = frequency == "never"
print("Inactive user:")
print(non_active)

high_intensity = intensity == "high"
print("High intensity sports:")
print(high_intensity)

low_intensity = intensity == "low"
print("Low intensity sports:")
print(low_intensity)



'''
# 3. CONDITIONAL STATEMENTS
# 3.1 DOOBER FARE CALCULATOR
Aim to calculate the different fares depending on chosen types.
First, I will store the typology of show and the number of credits owned by
the person. Then, I will use the "if, elif, else" statements to display the 
different fares based on the show type. Finally, I will insert the final price
which is deducted if the person own some credits. Hence:
'''

show_type = "Black"
credits = 4

if show_type == "DooberX":
    show_price = 17.5
elif show_type == "Black":
    show_price = 42.3
else:
    show_price = 13.7

print("Show price:")
print(show_price)

if credits > 0:
    final_price = show_price - credits

print("Final price:")
print(final_price)

    

'''
# 4. LOOPS
# 4.1 SHIPPING COST CALCULATOR
Aim to code a shipping cost calculator
First, I will store the value of the purchase and if it will be an 
international shipping or not and shipping cost as zeor. Then, I created an 
if statement that increases the cost for international shipping. After that,
I created a code block to change the shipping costs based on the value of the
purchase. Finally, I will use the "f" to combine everything inside an unique 
string to display the code of the total shipping cost. 
'''

international_shipping = True
total = 150
shipping_cost = 0

if international_shipping:
    shipping_cost += 25
    print("International base cost applied")

if total <= 50:
    shipping_cost += 10
elif total <= 100:
    shipping_cost += 8
else:
    shipping_cost += 5
    
print(f"Shipping cost: {shipping_cost}")


'''
# 4.2 COMPOUND INTEREST CALCULATOR
Aim to see the increase in the amout stored in a bank account.
Firstly, I will create the variable where to store the account value, the 
interest rate, and the years in the process. Then, I will create a counter 
variable to store the first year (or first interaction) in mine while loop.
Indeed, I create a while loop with condition based on the number of years that
the money will stay in the account. Inside the while, I calculated the accrued
interest, then I summed the accrued interest to the account value, I printed
the result, and then I increased the counter variable by 1. 
'''

account = 10000
interest_rate = 0.02
year = 5

print(f"Initial amount: {account}")

counter = 1
while counter <= year:
    accrued_interest = account * interest_rate
    account += accrued_interest
    print(f"year {counter}: {account}")
    counter += 1
    
    
    
'''
# 5. ORGANISING DATA
# 5.1 NEW PRODUCT RATING
Aim to store the results of how products were rated in a consumer product test.
Therefore, I created the lists containing the flavours of the new products,
their ratings based on the consumer test, and if they passed the threshold of 
an evaluation/rating of 3. Indeed, I inserted the objects contained in each
list inside square brackets []. 
'''

flavour = ["chocolate", "cream", "vanilla", "lemon"]
print("New flavours:")
print(flavour)

rating = [2.5, 4.5, 3, 2]
print("Consumer ratings:")
print(rating)

passed = [False, True, True, False]
print("Released:")
print(passed)


'''
# 5.2 STOCKS TRACKER
Aim to keep track of a company's stock values.
Thus, I created a list with the firm's stock values. Then, I used the indices
to change the errate values inside the list and to display the values 
corresponding to the request data.
'''

firm_stocks = [744.9, 793.6, 721.4, 712.3, 800.1]

firm_stocks[0] = 745.6
print("Latest value:")
print(firm_stocks[4])

firm_stocks[2] = 803.6
print("Highest value:")
print(firm_stocks[2])

print("Lowest value:")
print(firm_stocks[3])


'''
# 5.3 HUMIDITY MONITOR
Aim to list the data collected based on soil humidity measurements.
I collected all the data in a list called "humidity_level". Then, I used the 
".append" function to add a value at the end of the list, the ".insert" 
function to insert a value in a specific position of the list, and the ".pop" 
function to eliminate the final value inside the list.
'''

humidity_level = [91, 83, 86, 79, 87, 95, 88]

humidity_level.append(92)
humidity_level.insert(3, 85)
humidity_level.pop()

print(humidity_level)