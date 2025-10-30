# V1 OF PROJECT 1 (STILL ADDING ADJUSTMENTS) 

# In this project,  I created a program that finds the mean, deviation, and probability of an input 
# dataset. 

# Task 1: Calculate the yearly mean and Standard Deviation values of sales (2001-2020)
# Plot the results using two bar graphs 


#2z: We would like to calculate the yearly probability of sale price randing from 
# 200k-300k inclusive. This can be accomplished by counting number of houses sold for a 
# price in that range divided by total number of houses sold that year. 


'''
file: Project1.py 
Author: James Henry
Functionality: 

Sample of input Data (from CSV)
List Year
Sale Amount
2020
325000
2020
430000
2020
179900
2020
890000
2020
1447500
2020
1250000
2020
130000
2020
677500
2020
795000
2020
335000
2020
352000
2020
250000
2020
700000

'''

# Sample input data for year 2020
year = 2020
data = [
    325000, 430000, 179900, 890000, 1447500, 1250000, 130000,
    677500, 795000, 335000, 352000, 250000, 700000
]

sales = sorted(data) 
n = len(sales) #n will store the sorted data (sales) 

# Mean is always: SUM OF DATA / n 
mean = sum(sales) / len(sales) # in this case, Sum / Length of sales 

# Now that I have the mean, I can solve for deviations
squared_devs = [(x - mean) ** 2 for x in sales] # squared dev equation from lecture 
std_dev = (sum(squared_devs) / (len(sales) - 1)) ** 0.5 # std dev from lecture 

#After the deviation, it is easy to calculate the variance 
variance = sum(squared_devs) / (n-1) # corrected variable name

# Number of sales between 200k-300k (inclusive)
count_in_range = len([x for x in sales if 200000 <= x <= 300000])
total_sales = len(sales)
prob = count_in_range / total_sales

# to store my probability: 
yearly_probabilities = {year: prob}

# Output results
print(f"Year: {year}")
print(f"Mean: ${mean:,.2f}")
print(f"Standard Deviation: ${std_dev:,.2f}")
print(f"Variance: ${variance:,.2f}")
print(f"Probability of sale between $200k–$300k: {prob:.2%}")


