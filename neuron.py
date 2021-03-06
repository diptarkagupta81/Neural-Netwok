# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 03:26:29 2020

@author: Diptarka
"""
from matplotlib import pyplot as plt
import numpy as np
data=[[3,1.5,1],[2,1,0],[4,1.5,1],[3,1,0],[3.5,.5,1],[2,.5,0],[5.5,1,1],[1,1,0]]
mystery_flower = [4.5, 1]

#print(r)
#m1=r[0]
#m2=r[1]
#y=r[2]
#print(m1)
#print(m2)

#def pred(m1,m2):
#    w1=np.random.randn()
#    w2=np.random.randn()
#    b=np.random.randn()
#    z=m1*w1+m2*w2+b
#    return sigmoid(z)
def sigmoid(x):
    return(1/(1+np.exp(-x)))
def sigmoid_p(x):
    return sigmoid(x) * (1-sigmoid(x))
#s=pred(m1,m2)
#print(s)
#ss=print("rounded value  "+str(int(np.round(s))))

## slope funtion to run the loop to train the model to get closer to the target value y
#def slope(b):
#    return 2*(b-y)
#b=s
#for i in range(30):
#    b = b - .1 * slope(b)
#    print("target value "+str(b))

def train():
    #random init of weights
    w1 = np.random.randn()
    w2 = np.random.randn()
    b = np.random.randn()
    
    iterations = 10000
    learning_rate = 0.1
    costs = [] # keep costs during training, see if they go down
    
    for i in range(iterations):
        # get a random point
        ri = np.random.randint(len(data))
        point = data[ri]
        
        z = point[0] * w1 + point[1] * w2 + b
        pred = sigmoid(z) # networks prediction
        
        target = point[2]
        
        # cost for current random point
        cost = np.square(pred - target)
        
        # print the cost over all data points every 1k iters
        if i % 100 == 0:
            c = 0
            for j in range(len(data)):
                p = data[j]
                p_pred = sigmoid(w1 * p[0] + w2 * p[1] + b)
                c += np.square(p_pred - p[2])
            costs.append(c)
        
        dcost_dpred = 2 * (pred - target)
        dpred_dz = sigmoid_p(z)
        
        dz_dw1 = point[0]
        dz_dw2 = point[1]
        dz_db = 1
        
        dcost_dz = dcost_dpred * dpred_dz
        
        dcost_dw1 = dcost_dz * dz_dw1
        dcost_dw2 = dcost_dz * dz_dw2
        dcost_db = dcost_dz * dz_db
        
        w1 = w1 - learning_rate * dcost_dw1
        w2 = w2 - learning_rate * dcost_dw2
        b = b - learning_rate * dcost_db
        
    return costs, w1, w2, b
costs, w1, w2, b = train()
fig = plt.plot(costs)
print("w1 "+str(w1)+"w2 "+str(w2))
z = w1 * mystery_flower[0] + w2 * mystery_flower[1] + b
pred = sigmoid(z) *100

print("pred is "+str(pred))







