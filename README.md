# Expression-Evaluater
Developed a python scrpit to evaluate the expression. Following are the design constrains taken into consideration:
1) User should be able to give command line arguement (a single string as an arguement).
2) The arguement will be a combination of words and integers. 
3) The arguement will be something like - "(add 1 2)". 
4) The expression can be nested and the user can provide the expression with any depth.
5) You can assume that user will provide expression containing balanced paranthesis but handling errors is always a better option while developing the code.



Following are the instructions for the user input:
1) Please provide a command line arguement as a single string.
2) To get the correct output, please provide a valid input as follows :
  i) python calc.py "(add 1 2)"
  ii) You can also provide nested expression. For exmaple, python calc.py "(multiply 3 (add 7 8))" 
