# Authors: Amulya Badineni, Michael Giordano, Rishi Konkesa, Jason Swick
# Filename: main.py
# Description: Implements the Find-S algorithm, produces a trace we worked out in class for 
#               the EnjoySport example with the training examples, learns the target concept

import numpy as np
from train import TrainingExample



#used to store most specific
s = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
task = 0

def findS(data):
    #print each training example
    if data.train[6] == "yes":
        counter = 0
        for i in range(6):
            if (data.train[counter] != s[counter]) and s[counter] == "NULL":
                s[counter] = data.train[counter]
            elif data.train[counter] != s[counter]:
                s[counter] = "?"
            counter += 1
    if task == 1:
        print(s)


def main():
    print("running main")

if __name__ == "__main__":
    main()
    print("Enter '1' to run task 1 & 2, enter '2' to run task 3 and the experimental question")
    task = int(input())
    if task == 1:
        data1 = TrainingExample("sunny", "warm", "normal", "strong", "warm", "same", "yes")
        data2 = TrainingExample("sunny", "warm", "high", "strong", "warm", "same", "yes")
        data3 = TrainingExample("rainy", "cold", "high", "strong", "warm", "change", "no")
        data4 = TrainingExample("sunny", "warm", "high" , "strong", "cool", "change", "yes")
        findS(data1)
        findS(data2)
        findS(data3)
        findS(data4)
    elif task == 2:
        print("Enter the number of times you want the program to run (whole number greater than 0)")
        num_trials = int(input())
        num_iterations = 0
        list_iterations = []
        for i in range(num_trials):
            while s != ["sunny", "warm", "?", "?", "?", "?"]:
                random_data = TrainingExample()
                random_data.example()
                findS(random_data)
                num_iterations += 1
            list_iterations.append(num_iterations)
            num_iterations = 0
            s = ["NULL", "NULL", "NULL", "NULL", "NULL", "NULL"]
        print(list_iterations)
