#Kort sammenfatning av hva jeg gjorde med pen, se bilde av notaten nede:
#Funksjonen vi har fått i oppgaven består av 2 faktorer, så må bruke produktregelen og kjerneregelen,
#til å derividere funksjonen. 
#Vi gjør det siden vi må løse den derividerte av funksjonen for lik null. 
#Sånn finner man toppunktet(maks). 
#Når jeg gjorde  dette fikk jeg en alt for komplisert likning så bruker python for å løse

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#Funksjonen gitt:
def f(x):
    return (np.e**(-x/4))*np.arctan(x)

#Likningen f(x) derivert som skal bli satt lik null:
def g(x):
    return np.arctan(x)-(4/((x**2)+1))

#Setter null for å finne løsningen, bruker fsolve:
x0 = 1 
x_topp = fsolve(g, x0) [0]
y_topp = f(x_topp)

#Printer resultat:
print(f"x = {x_topp: .4f} " )
print(f"f(x) = {y_topp: .4f}")


    
#(np.arctan(x)-(4/((x**2)+1))) = 0
#(np.arctan(x) = (4/(x**2)+1)
#x = np.tan((4/(x**2)+1))  ||  (np.arctan(x))*((x**2)+1) = 4

x = np.linspace(-5, 20, 1000)
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.show()



print("It barks at no one else but me like It's seen a ghost I guess it's seen the sparks flowing no one else would know hey man slow down, slow down idiot, slow down, slow down sometimes I get overcharged that's when you see sparks they ask me where the hell I'm going at a thousand feet per second hey man slow down, slow down idiot, slow down, slow down hey man slow down, slow down idiot, slow down, slow down")
