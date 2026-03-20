#Kort sammenfatning av hva jeg gjorde med pen, se bilde av notaten nede:
#Funksjonen vi har fått i oppgaven består av 2 faktorer, så må bruke produktregelen og kjerneregelen,
#til å derividere funksjonen. 
#Vi gjør det siden vi må løse den derividerte av funksjonen for lik null. 
#Sånn finner man toppunktet(maks). 
#Når jeg gjorde  dette fikk jeg en alt for komplisert likning så bruker python for å løse

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#definerer Funksjonen gitt:
def f(x):
    return np.exp(-x/4)*np.arctan(x)

#Likningen som blir når f(x) blir derivert sånn at den kan bli satt lik null:
def g(x):
    return np.arctan(x)-(4/((x**2)+1))

#Setter null for å finne løsningen, bruker fsolve:
x0 = 1 #evt startsted
x_topp = fsolve(g, x0) [0]
#finner funksjonsverdien
y_topp = f(x_topp)

#Printer resultat:
print(f"x = {x_topp:.4f} " )
print(f"f(x) = {y_topp:.4f}")

# Får returnert svaret:
#    x = 1.7207
#    f(x) = 0.6010

#Lager koden for plot: 
x = np.linspace(0, 5, 1000)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.scatter(x_topp, y_topp, label="Toppunkt")
#Forklaring
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafen av f(x) med toppunktet")
#Lager ruter for lettere lesing
plt.grid()

#Viser ploten
plt.show()
#Kort sammenfatning av hva jeg gjorde med pen, se bilde av notaten nede:
#Funksjonen vi har fått i oppgaven består av 2 faktorer, så må bruke produktregelen og kjerneregelen,
#til å derividere funksjonen. 
#Vi gjør det siden vi må løse den derividerte av funksjonen for lik null. 
#Sånn finner man toppunktet(maks). 
#Når jeg gjorde  dette fikk jeg en alt for komplisert likning så bruker python for å løse

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

#definerer Funksjonen gitt:
def f(x):
    return np.exp(-x/4))*np.arctan(x)

#Likningen som blir når f(x) blir derivert sånn at den kan bli satt lik null:
def g(x):
    return np.arctan(x)-(4/((x**2)+1))

#Setter null for å finne løsningen, bruker fsolve:
x0 = 1 #evt startsted
x_topp = fsolve(g, x0) [0]
#finner funksjonsverdien
y_topp = f(x_topp)

#Printer resultat:
print(f"x = {x_topp:.4f} " )
print(f"f(x) = {y_topp:.4f}")

# Får returnert svaret:
#    x = 1.7207
#    f(x) = 0.6010

#Lager koden for plot: 
x = np.linspace(0, 5, 1000)
y = f(x)

plt.plot(x,y,label="f(x)")
plt.scatter(x_topp, y_topp, label="Toppunkt")
#Forklaring
plt.legend()
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Grafen av f(x) med toppunktet")
#Lager ruter for lettere lesing
plt.grid()

#Viser ploten
plt.show()
