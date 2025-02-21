import numpy as np
import matplotlib.pyplot as plt
T1 = -140+273
T2 = -130+273
T3 = -120+273
T4 = -110+273
T5 = -100+273
R= 8.314
a = 0.1382
b=3.19*10**-5
def f(V,T):
    return (R*T)/(V-b) - a/(V**2)

V =  np.linspace(4.19*10**-5,10**-3 , 1000)
P1 = f(V,T1)
P2 = f(V,T2)
P3 = f(V,T3)
P4 = f(V,T4)
P5 = f(V,T5)
fig, axs = plt.subplots(1, 6, figsize=(16, 5))
axs[0].plot(V,P1)
axs[0].set_xlabel("V")
axs[0].set_ylabel("P")
axs[0].set_title("T1")

l1 =  5.5 * 10 ** -5
right = 9.2 * 10 ** -5
def f(V):
    return (R * T2) / (V - b) - a / (V ** 2)
while(abs(right - l1) > 10 ** -8):
        i = l1 + abs(right-l1)/3
        j = right - abs(right-l1)/3
        if f(i) < f(j):
            right = j
        else:
            l1 = i
print("Локальный минимум:", f(l1))
left1 =  9.4 * 10 ** -5
right =  1854 * 10**-4
def f(V):
    return (R * T2) / (V - b) - a / (V ** 2)
while(abs(right - left1) > 10 ** -8):
        i = left1 + abs(right-left1)/3
        j = right - abs(right-left1)/3
        if f(i) > f(j):
            right = j
        else:
            left1 = i
print("Локальный max:", f(left1))
I = l1 + 10**-9
sumi = 0
while I < left1:
    sumi += ((10**-8)**2 + abs(f(I+10**-8) - f(I))**2) ** 0.5
    I+= 10**-8
print(sumi)
P_nas = 3664186.998
def f1(V):
    return (R * T2) / (V - b) - a / (V ** 2) - P_nas
fig = plt.figure(figsize=(14, 6))
ax = plt.subplot(1, 1, 1)
plt.plot(V,f1(V))
plt.axhline(y=0,color = "red")
# КОРНИ НАШЕЛ ИЗ ГРАФИКА
print(6.152572631835937e-05, 0.0001003925, 0.000194786839)
axs[1].plot(V,P2)
axs[1].set_xlabel("V")
axs[1].set_ylabel("P")
axs[1].set_title("T2")
axs[1].axhline(y=0, color='r')

axs[2].plot(V,P3)
axs[2].set_xlabel("V")
axs[2].set_ylabel("P")
axs[2].set_title("T3")

axs[3].plot(V,P4,color = "red")
axs[3].set_xlabel("V")
axs[3].set_ylabel("P")
axs[3].set_title("T4")


axs[4].plot(V,P5)
axs[4].set_xlabel("V")
axs[4].set_ylabel("P")
axs[4].set_title("T5")

plt.show()
