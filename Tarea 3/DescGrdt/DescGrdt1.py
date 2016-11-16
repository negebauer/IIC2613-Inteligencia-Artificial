import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import AsaUtils

#Section 1. Define target function  
x = np.linspace(-15,15,200)
y = x**2
   
#Section 2. Plot function and mark minimum value
fig1 = plt.figure(figsize=(8, 6))  
plt.axis([-12, 12,-5, 150]) 
funcMin=AsaUtils.getTrueMin()
plt.plot(x,y,'k',funcMin[0], funcMin[1],'bo',linewidth=2.0, markersize=12)
plt.title('Quadratic function')
   
#Section 3. Define relevant parameters to perform the gradient descent estimation
old_min = 10  #This is the initial value for x
learningRate = 0.1
precision = 0.0001  # This is the minimum error to stop the gradient descent loop


#Section 4. Main loop to descent the gradient
mins = []
while True:
    gradient = AsaUtils.getDerivative(old_min) 
    move = gradient * learningRate
    new_min = old_min - move
    mins.append(new_min)
    #Check if we are close enough to a minimum
    if(abs(new_min - old_min) < precision):
        break
    else:
        old_min=new_min
           
     
print("Local minimum occurs at {}.".format(round(new_min,2)))

#Section 5. Now define visualization function to show animation of the minimization steps    
def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    x_n = mins[i]
    y_n = x_n**2
    line.set_data(x_n, y_n)
    return line,
    
fig2 = plt.figure(figsize=(8, 6))
plt.axis([-12, 12,-5, 150]) 
plt.plot(x,y, 'k', linewidth=2.0)
line, = plt.plot([], [], 'ro', markersize=12)

anim = animation.FuncAnimation(fig2, animate, init_func=init, blit=True, frames=len(mins), repeat=False)
 
plt.show()
