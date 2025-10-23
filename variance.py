'''

file: varianceofSet.py
Author: James Henry
Functionality: To understand the functionality of data analytics in python, 
I decided to write this script. It computes the mean, median, deviation, squared deviations, 
and variance of a dataset. Lastly, the user can see the results from the display/print function. 

'''

# first we need a dataset to work with
data = [3,6, 9, 12, 15, 18]

# next, the data has to be sorted when computing 

sorted_data = sorted(data)
n = len(sorted_data) #n will store the sotred data 

# Mean is always: SUM OF DATA / n 
mean = sum(sorted_data) / n 

# Median depends on if n is odd or even 
if n % 2 == 1: 
    median = sorted_data[n//2]
else:
    median = (sorted_data[n //2 - 1] + sorted_data[n //2]) / 2

# Now that I have the mean and median, I can solve for deviation 
deviations = [x - mean for x in sorted_data]
squared_deviations = [(x-mean) ** 2 for x in sorted_data]

#After the deviation, it is easy to calculate the variance 
variance = sum(squared_deviations) / (n-1)

# NOW DISPLAY SO THE USER CAN SEE :) 

print("\nWE HAVE:")
print(f"Mean: {mean:.2f}")
print(f"Median: {median:.2f}")
print(f"Variance: {variance:.2f}")
