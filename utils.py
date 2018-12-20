import numpy as np

# in this script we will define the functions needed to solve this problem
# we would need 3 functions:
## 1 : get_simulation_input() ==> to read the files and extract input data from them
## 2 : run_simulation_once() ==> to simulate one attack on the fortress
## 3 : run_simulation_on_demo == > to test the functionality of run_simulation_once()

def get_simulation_input(PATH_TO_INPUT):

    # PATH_TO_INPUT : is the only input for the function and it holds the
    # path to the file on which we will run the simulation.
    # This function would opens the file as a .txt and parses it

    # This function returns a tuple encapsulating the needed inputs.
    
    l= []
    new_e= []
    d = []
    file = open(PATH_TO_INPUT, "r")
    lines = file.readlines()
    for line in lines:
       temp = line.split(',')
       for e in temp:
          if ('\n') in e:
            temp.remove(e)
            new = e.replace('\n','')
            temp.append(new)
       l.append(temp)
       
    file.close()
    N = int(l[0][0])
    p = int(l[0][1])
    k = int(l[0][2])
    for e in l[1:]:
        for i in e:
           new_e.append(int(i))
        d.append(new_e)
        new_e = []
    return (N,p,k,d)

def run_simulation_once(input_tuple, inital_wights_per_grid = 1, print_rows = False):

    # input_tuple : a tuple containing the elements necessairy to run a simulation
    # initial_wights_per_grid (optional): an integer that holds the initial number of wights per grid
    # print_rows (optional) : boolean to determine whether or not to print the result of the simulation in each row

    ## this function runs one iteration of the simulation and returns a boolean indicating whether or not
    ## the invasion was successful.
    
    N = input_tuple[0]
    p = input_tuple[1]
    k = input_tuple[2]
    d = input_tuple[3]

    row = np.ones(N) * inital_wights_per_grid 
    for i in range(0,N):
        row = row - d[i]
        row[row < 0] = 0  
        s = N-1-i
        max_percentage =  max(0,p-s)
        
        if (max_percentage > 0):
            random_percentages = np.random.randint( max_percentage, size= N )
        else :
            random_percentages = np.zeros(N)
        
        percentage_left = 100 - random_percentages 
        row = row * (percentage_left/100)
        if (print_rows) : print (row)

    captured = (sum(row) > k)

    return captured

def run_simulation_on_demo(input_tuple, inital_wights_per_grid = 15):

    # this function is the equivalent of the previous one, only it is designed
    # to run the simulation on the demo given in the problem discription.
    # since the random seed was not provided, the percentages were forced to be the same
    # as in the description.
    # it does not return any values, rather, it is forced to print the results to help us
    # visulaize the functionality of our code

    N = input_tuple[0]
    p = input_tuple[1]
    k = input_tuple[2]
    d = input_tuple[3]

    row = np.ones(N) * inital_wights_per_grid 
    for i in range(0,N):
        row = row - d[i]
        row[row < 0] = 0  
        s = N-1-i
        max_percentage =  max(0,p-s)
       
        if (i ==0) : random_percentages = np.array([4,0,2])
        if (i ==1) : random_percentages = np.array([10,2,0])
        if (i ==2) : random_percentages = np.array([6,20,15])
   
        percentage_left = 100 - random_percentages 
        row = row * (percentage_left/100)
        print(row)

    captured = (sum(row) > k)

     

