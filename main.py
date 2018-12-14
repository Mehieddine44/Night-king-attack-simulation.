import utils
import math

# this script is the main code used to run the simulation on many iterations
# and deliver the desired output, which is the minimum total number of weights required
# to have a 95% chance to capture the fortress...

# the user should tune the following parameters to trade of
# accuracy vs speed according to their computational resources and their time and
# accuracy requirments.

INITIAL_RATE = 10
# this determines the initial rate by which we increase n
# we do not we do not want to loop through  1000 000 integers


PATH_TO_INPUT = 'TheWall.txt'
#Make this equal to the path of your input file

input_tuple = utils.get_simulation_input(PATH_TO_INPUT)
# calling the function get_simulation_input() which returns the inputs N,p,k,d
# of our simulation

capturable = False
# a boolean determining whether or not the fortress is capturable
over_increment = False
# a boolean determining if we have over incremented n and we need to go back

percentage = 0
# the number of successful simulations

n = 1
# n is the number of weights per grid

while (n < int(1000000/input_tuple[0])):
    
    for i in range(100):
        percentage+= utils.run_simulation_once(input_tuple, n)
        # accumulating the successful attempts
   
    #percentage = sum_of_success
    # the percentage of successeful attempts to the total number of attempts
    
    rate = INITIAL_RATE * math.exp(-percentage)
    # the rate at which we increment n is exponentially decaying
    # so we can reduce computation while preserving accuracy

    print("The percentage of  ( "+str(n*input_tuple[0])+") wights succeeding is : " +str(percentage)+"%")
    # ptinting the percentage the the current number of wights would succeed
    
    if (rate <= 1):
        n+= (95 - percentage)
        # in case the rate goes under 1,it means we are very close to the desired
        # percentage. So we start incrementing n.
        
    else :
        n =  int(n*rate)
        # we increase n by rate
        
    if(abs(percentage - 95)< 1):
        minimum_number_required = n*input_tuple[0]
        capturable = True
        break
        # once we reach this interveal we break the loop
    elif(percentage > 96):
        n-=1
        over_increment = True
        percentage = 0
        # if we pass 95% it means we have over increased n and we need to go back
        
    elif (over_increment and percentage < 94):
        minimum_number_required = n*input_tuple[0]
        capturable = True
        break
    else:
         percentage = 0
        

if capturable :
   print("The minimum number of wights required to take over the fortress is :" + str(minimum_number_required))
else:
   print("The fortress is uncapturable !! ")
