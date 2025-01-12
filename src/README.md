# Genetic Programming Toolbox

This is Toolbox developed for the course Computational Intelligence at Politecnico di Torino.

## Run a simulation 
To run one simulation of this software you have to upload one of the file named *problem_{number}.npz*, using the numpy function *np.load([input])*. 

The first operation of the program is to set a dictionary variable that contains all method in the numpy library. These methods are divided in 2 containers, those methods that need one input and those operators that need 2 inputs to define an output.

In the dictionary variables are defined only the operational methods ( e.g. "add", "subtract", "multiply", "divide",  "power", "sin", "cos", "log" ), logical or conditional operators are filtered because our target samples have only numerical value. 
More experiments can be conducted by the introduction of dataset with Boolean or Array inputs.

To define the constant for Symbolic regression the software uses the range of the input dataset, taking the *max_value* and the *min_value* as upper and lower bound.

## Classes 
The main class in this toolbox is the Node Object.

This object contains four main attribute:
- operator -> contains a numpy operator
- value -> contains a variable or a constant
- left -> contains a sub-nodes or None
- right -> contains a sub-nodes or None
  
The Node can be classified in 2 typologies of node:
- as operational node in which the attribute operator is numpy operator, the right or left node can contain sub-node.
- as leaf, in which the operational is *None* and the Node has only a value that is av variable (given from dataset) or a costant.

Node object contains the following methods:
- *is_leaf(self)* -> check if the node is an operational or a leaf node
- *__str__(self)* -> when the Node is print in output, the following output will be the formula of the Node object
- *compute(self, variables_values)* -> the method compute the value in output using a dictionary *variables_values* that contain the variables of the dataset
- *print_attributes(self)* -> print the attributes of Node ( operator - value - left - right ) 

## Tree Generation
The program deals with 2 methods to create the trees:
- *generate_grow_tree(depth=3, variables={"x0":0, "x1":0})* -> creates tree with a specific max depth given in input and also using a dictionary to set the x variables in input, the level of depth for each tree is defined randomly at each level step ( each side can have different levels).
- *generate_full_tree(depth=4, variables={"x0":0, "x1":0})* -> creates tree with a specific max depth given in input and the input variabels are defined using a dictionary, the method defined in each level the operation, only the last level defined randomly contain only variables or costants. 

## MSE function 
- *MSE_train(Node)* -> Given in input the entire tree containing the formula, the tool compute the MSE based on the dataset uploaded in the first step

## Parent Selection 
- *tournament_selection(population, tournament_size=10)* -> the method returns the Node with the best fitness in the offspring defined by the *tournament_size*. Default offspring size is *tournament_size=10*.
- *select_operation(mutation_prob=0.05, crossover_prob=0.95)* -> the method define which operational mutation will be used with different probability. Default probability are *mutation_prob=0.05*, *crossover_prob=0.95*.
- *get_node(node)* -> the method extracts a sub-node to deal with operational mutation.

## Mutation Function
- *hoist(obj_input)* -> Extract a sub-node and uses as new child, this operation is employed to avoid redundant node or node too deep beyond the theory of Bloat (survival of the fattest).
- *point_mutation(obj_input)* -> mutate the operator in a specific level of the node.
- *permutation(obj_input)* -> inverte the values of a leaf node ( e.g. a - b  ->  b - a ) 

## Recombination Function
- *recombination(obj1 , obj2)* -> Recombine the sub-node of each obj in input and combine them to 2 new child

## Implementation GP
- *filtered_POP(POP)* -> the population is filtered to 500 samples, and are removed redundant solution or solution with the same fitness ( sharing more time the same loci  ) 
- *generate_POP(POP)* -> the method generate 250 samples for both methods generate_full_tree and generate_grow_tree

The toolbox uses a for loop to check in the generation the population is at least 100 samples, can happens that the generate tree is not able to compute a feasible result.

## Simulation 
The simulation is based on 1000 generation to mutate the population, the simulation uses also a variable *lenght_sample* for the tourment selection to select dinamically 20% of the population lenght.
For each iteration is extracted 2 samples using the tournament selection, the typology of mutation used *select_operation()* and is computed the MSE.
After the generation a filter function is used to kill the worst fitness solutions to apply a steady state approach. 


