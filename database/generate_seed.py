# Generating Dummy records for our finance.purchases TABLE by using python script.

print("Dummy records for our finance.purchases TABLE")

import random
from datetime import date, timedelta

# for genrating random dates

start_date     =    date(2023,1,1)
end_date       =    date.today()

# for random.randint(0,total_days)

total_days     =    (end_date - start_date).days 

# For dynamically creation of INSERT query

n = int(input('Enter the number n to generate n dummy data for our finance.purchases TABLE'))

# Printing INSERT query

insert = "INSERT INTO finance.purchases(seller_id, purchase_date,total_bags,waste_pieces,rate_per_piece) VALUES" 
print(insert)

# Automation

for i in range(1,n+1):

     seller_id   = random.randint(1,9)

     random_days = random.randint(0,total_days)
     p_date      = start_date + timedelta(days =random_days)

     net_bags    = random.randint(25,45)

     waste_piece = random.randint(0,15)

     per_price   = random.uniform(35.55,50.55)
     round_price = round(per_price,2) 

     # in this if condition we used , at the last to get proper syntax

     if (i < n):
          values = f"({seller_id}, '{p_date}', {net_bags}, {waste_piece}, {round_price}),"
          print(values)  

     # in this else condition we used ; at the end to get proper syntax

     else:
          values = f"({seller_id}, '{p_date}', {net_bags}, {waste_piece}, {round_price});"
          print(values)


# Generating Dummy records for our finance.payments TABLE by using python script.

print("Dummy records for our finance.payments TABLE")


method_choice = ['UPI','Cheque','Bank Transfer','Cash','Credit Card']

n = int(input("Enter the number n to generate n dummy data for our finance.payments TABLE"))

print("INSERT INTO finance.payments(seller_id,payment_date,amount_paid,payment_method)VALUES")

for i in range(1,n+1):

     seller_id      = random.randint(1,9)

     random_days    = random.randint(0,total_days)
     p_date         = start_date + timedelta(days= random_days)

     amount         = random.uniform(20000.54,65000.65)
     round_amount   = round(amount,2)

     pay_method     = random.choice(method_choice)

     if (i < n):
          value = f"({seller_id},'{p_date}',{round_amount},'{pay_method}'),"
          print(value)

     else:
          value=f"({seller_id},'{p_date}',{round_amount},'{pay_method}');"
          print(value)