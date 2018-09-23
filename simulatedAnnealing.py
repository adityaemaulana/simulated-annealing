import math
import random

# initiating random floating number
def generate():
    return random.uniform(-10.0, 10.0)

# calculate objective function
def objective(x1 ,x2):
    return -(abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - (math.sqrt(x1*x1 + x2*x2) / math.pi)))))

# calculating acceptance probability for accepting new x1 & x2
# return true if accepted otherwise return false
def calculateAccProb(dE, T):
    P = math.exp(-(dE) / T)
    R = random.random()
    if(R < P):
        return True
    else:
        return False

# algorithm for Simulated Annealing
def simulatedAnnealing(x1, x2, x1b, x2b, Eb, E, T, stopT, alpha):
    Eb = E
    x1b = x1
    x2b = x2

    while T > stopT:
        # generate new solution
        x1n = generate()
        x2n = generate()
        # calculate new cost
        En = objective(x1n, x2n)
        deltaE = En - E

        # if the new solution is better than current solution
        if(deltaE < 0):
            x1 = x1n
            x2 = x2n
            E = En

            # check wether the new solution is the current best solution
            if(En < Eb):
                x1b = x1n
                x2b = x2n
                Eb = En

        # if new solution is worse than current solution
        else:
            if(calculateAccProb):
                x1 = x1n
                x2 = x2n
                E = Eb

        T *= alpha

    print(f'Energy: {Eb} X1: {x1b} X2: {x2b}')
    return

# initial value of current value and best value
x1 = x1b = generate()
x2 = x2b = generate()
# initial current energy and best energy
E = Eb = objective(x1, x2)
    
# initialize temperature, stop temperature, and cooling rate
T = 1000
stopT = 1
alpha = 0.99

# run simulated annealing
simulatedAnnealing(x1, x2, x1b, x2b, Eb, E, T, stopT, alpha)
