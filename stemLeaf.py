'''

file: stemLeaf.py
Author: James Henry
Functionality: To understand the functionality of data analytics in python, 
I decided to write this script. It gives me stem leaf plots. In these plots, 
you use the tenths digit as the stem and the ones as a leaf. Each order is L->G. 


'''
def stem_and_leaf_plot(data):

    # The first step in stem leafs is to sort the data
    sorted_data = sorted(data)

    #next, I need to build the dictionary 
    plot = {}
    for num in sorted_data:
        stem = num // 10 
        leaf = num % 10
        plot.setdefault(stem, []).append(leaf)

    # Furthermore, we should be able to see what is happening 
    print("Stem | Leaves") 
    print("--------------")
    for stem in sorted(plot):
        leaves = ''.join(str(leaf) for leaf in plot[stem])
        print(f"{stem:>4} | {leaves}")

# now that I finished the function for stem and leaf, I can test it 

data = [12, 15, 17, 21, 23, 24, 25, 26, 31, 33, 35, 36, 38, 42, 44, 45, 47, 50]

stem_and_leaf_plot(data)
