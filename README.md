# Simulated Annealing
Simulated Annealing implementation using Python 3.6.

## Description
  Simulated annealing is a searching technique for approximating the global optimum of a certain function. It works by iterating the function until reaching the coolest temperature(defined limit). This task will show the minimum result of a function.

## Objective Function
  Function that will be used for this implementation. 

  ![Image of Function](https://cdn1.imggmi.com/uploads/2018/10/1/be0008d51d0922ed2fa69d705b1a3663-full.png)

## Constraint
  -10 <= X1, X2 <= 10

## Parameters
  Temperature: affect the number of iteration
      Value: 1000

  Cooling Rate: parameter for decreasing the temperature
      Value: 0.99

## Solution
   One of the global optimum for this function is:
   
   X1 : 8.0729
   
   X2 : -9.6621
   
   Cost : -19.2052

## Visualization
  Visualizing all possible cost using contour plot
  
  ![Image of Visualization](https://cdn1.imggmi.com/uploads/2018/9/24/25e09313675b886cd4ef6b960b62719f-full.png)

> x-axis is value of X1

> y-axis is value of X2

> Color show the resulted cost where smaller cost have more darker color
