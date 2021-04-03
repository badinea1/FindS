# Amulya Badineni, Michael Giordano, Rishi Konkesa, Jason Swick
# CSC 426-01
# Project 2

import numpy as np
from train import TrainingExample



# s: used to store most specific hypothesis
s = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]

# task: used to hold user input to determine which task to perform 
task = 0

# findS function: performs the findS algorithm. Takes in a TrainingExample object, data, and will adjust 's' (the most specific hypothesis) based on the data
def findS(data):
    
    # Check if the data is a positive example. If the data is positive, then iterate through loop. Else, do nothing.
    if data.train[6] == "yes":
        counter = 0
        # for each attribute: 
        for i in range(6):
            # if 'data' and 's' have different values and 's' has a NULL value, set 's' to 'data's value
            if (data.train[counter] != s[counter]) and s[counter] == "NULL":
                s[counter] = data.train[counter]
            # else if 'data' and 's' have different valules, set 's' to '?'
            elif data.train[counter] != s[counter]:
                s[counter] = "?"
            counter += 1
            
    # if user is performing task 1, print out 's' in order to provide a trace of the algorithm.
    if task == 1:
        print(s)

# main function
def main():
    print("running main")

if __name__ == "__main__":
    main()
    print("Enter '1' to run task 1 & 2, enter '2' to run task 3 and the experimental question")
    
    # take in user input: '1' will use class example and provide a trace of the algorithm. '2' will run the algorithmm with randomly generated training examples
    task = int(input())
    if task == 1:
        # initialize TrainingExample objects based on the in-class example
        data1 = TrainingExample("sunny", "warm", "normal", "strong", "warm", "same", "yes")
        data2 = TrainingExample("sunny", "warm", "high", "strong", "warm", "same", "yes")
        data3 = TrainingExample("rainy", "cold", "high", "strong", "warm", "change", "no")
        data4 = TrainingExample("sunny", "warm", "high" , "strong", "cool", "change", "yes")
        # Perform findS for each training example
        findS(data1)
        findS(data2)
        findS(data3)
        findS(data4)
    elif task == 2:
        
        # read in user input for the number of times the program should run (note: the program will run until the learned hypothesis becomes the same as the target concept.)
        print("Enter the number of times you want the program to run (whole number greater than 0)")
        num_trials = int(input())
        num_iterations = 0
        
        # list_iterations: an array that holds integer values representing the number of training examples required for the algorithm to learn the target concept
        list_iterations = []
        
        # loop through findS algorithm num_trials times (baesd on user input)
        for i in range(num_trials):
            # While condition checks if the algorithm has learned the target concept
            while s != ["sunny", "warm", "?", "?", "?", "?"]:
                # random_data: a TrainingExample object that is first initialized, then given random values for each attribute, i.e., a randomly generated training example
                random_data = TrainingExample()
                random_data.example()
                # call findS algorithm on this randomly generated training example
                findS(random_data)
                # increment counter
                num_iterations += 1
            # update list_iterations to hold the number of training examples required to learn the target concept for this iteration of the findS algorithm
            list_iterations.append(num_iterations)
            # reset counter variable and s.
            num_iterations = 0
            s = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
        print(list_iterations)
