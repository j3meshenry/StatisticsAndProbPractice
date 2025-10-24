'''

file: bayesTHM.py
Author: James Henry
Functionality: To understand the functionality of data analytics in python, 
I decided to write this script. It taught me how Bayes' THM works in data. 
We check for P(A), P(B), find the conditional (A and B) and plug it in. 
'''

# P( A given B ) = P ( B given A) * P(A) / P(B)

def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):

    #Calculates P(A|B) using Bayes' Theorem.
    
    '''Parameters:
    - p_a: Prior probability of A
    - p_b_given_a: Probability of B given A
    - p_b_given_not_a: Probability of B given not A
    '''
    
    # Returns:
    # Posterior probability P(A|B)

    # Probability of not having event A 
    p_not_a = 1 - p_a 

    # Total probability of event B using Total Law 
    p_b = p_b_given_a * p_a + p_b_given_not_a * p_not_a 

    # Bayes' THM for conditional prob
    p_a_given_b = (p_b_given_a * p_a) / p_b

    return p_a_given_b

# Example: Medical test
p_a = 0.01  # P(Disease)
p_b_given_a = 0.99  # P(Positive | Disease)
p_b_given_not_a = 0.05  # P(Positive | No Disease)

posterior = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)
print(f"P(Disease | Positive Test) = {posterior:.4f}")
