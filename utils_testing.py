import utils
# in this script we will test the functionality of our utils functions
# by running the functions on the Demo given in the problem discription

input_tuple = utils.get_simulation_input("Demo.txt")
simulation = utils.run_simulation_once(input_tuple, 15)

print("N = "+ str(input_tuple[0]))
print("p = "+ str(input_tuple[1]))
print("k = "+ str(input_tuple[2]))
print("d = ")
for line in input_tuple[3]:
    print(line)
print("The rsult of the simulation is : ")
utils.run_simulation_on_demo(input_tuple, 15,print_rows=True)

# if our functions are correct, the expected output would
# be the following : 
'''
N = 3
p = 20
k = 19
d = 
[4, 3, 1]
[3, 1, 5]
[1, 2, 3]
The rsult of the simulation is : 
[10.56 12.   13.72]
[ 6.804 10.78   8.72 ]
[5.45576 7.024   4.862  ]

'''

