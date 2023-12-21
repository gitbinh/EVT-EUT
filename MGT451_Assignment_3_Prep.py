import random;

g = [
    [(0.5, 1000), (0.5, 0)], #left-hand gamble
    [(1.0, 450)],            #right-hand gamble
    ];
print(g[0]);

def evt(g):
    evLeft = 0
    for alternative in g[0]:
        p = alternative[0]
        v = alternative[1]
        evLeft += p*v
    evRight = 0
    for alternative in g[1]:
        p = alternative[0]
        v = alternative[1]
        evRight += p*v

    if evLeft == evRight:
        return float(random.random() > 0.5)
    else:
        return float(evLeft > evRight);


choice = evt(g);
print(choice);


#counter = 0
#for i in range(10):
#    print(i)
#    counter = counter + 1   # aka += 1
    #print(counter)
    #print("===");


def utilityDefault(value):
    return value;

def utilityHuman(value):
    return value;           #anomaly event => EVT and EUT make different prediction
    #for this example, you want to give extra utility for the human conception in EUT (risk-diverse)
    #so that EUT would suggest ppl tend to be choosing the second option instead of the first one

def eut(g, utility = utilityDefault):
    
    #if not utility:
        #utility = lambda x: x  
    
    evLeft = 0
    for alternative in g[0]:
        p = alternative[0]
        v = utility(alternative[1])
        evLeft += p * u
    evRight = 0
    for alternative in g[1]:
        p = alternative[0]
        v = utility(alternative[1])
        evLeft += p * u

    if evLeft == evRight:
        return float(random.random() > 0.5)
    else:
        return float(evLeft > evRight);
