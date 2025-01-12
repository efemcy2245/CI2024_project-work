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



