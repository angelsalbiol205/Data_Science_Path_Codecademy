#Step 1 & 2
import noshmishmosh
import numpy as np

#Step 3 determine Baseline Conversion Rate, MDE, Threshold
##Step 4
all_visitors = noshmishmosh.customer_visits
##Step 5
paying_visitors = noshmishmosh.purchasing_customers
##Step 6
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
##Step 7 & 8
baseline_percent = (paying_visitor_count / total_visitor_count) * 100.0
print('Baseline = ', baseline_percent)
#baseline = 18.6

##Step 9
payment_history = noshmishmosh.money_spent
##Step 10
average_payment = np.mean(payment_history)
##Step 11
new_customers_needed = np.ceil(1240 / average_payment) #np.ceil rounds the number up
##Step 12
percentage_point_increase = (new_customers_needed / total_visitor_count) * 100.0
print('Percentage point increase = ', percentage_point_increase)
#percentage_point_increase = 9.4

##Step 13 & 14
mde = (percentage_point_increase / baseline_percent) * 100
print('MDE = ', mde)
#mde = 50.53

#Step 15 threshold 10%, add numbers sample calculator

#Step 16
ab_sample_size = 490









