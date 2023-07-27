import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

C_4=261.63 #c4

G_4=392 #g4

A_4=440 #A4

t = np.linspace(0 , 3, 12 * 1024)

Left_hand=np.sin(2*np.pi*0*t)

First_pair=1.5*(Left_hand+np.sin(2*np.pi*C_4*t))*(np.heaviside(t,1)-np.heaviside(t-0.5,1)) #Twinkle

Second_pair=(Left_hand+np.sin(2*np.pi*G_4*t))*(np.heaviside(t-0.75,1)-np.heaviside(t-1.25,1)) #Twinkle

Third_pair=1.5*(Left_hand+np.sin(2*np.pi*A_4*t))*(np.heaviside(t-1.5,1)-np.heaviside(t-2,1)) #little

Fourth_pair=(Left_hand+np.sin(2*np.pi*G_4*t))*(np.heaviside(t-2.25,1)-np.heaviside(t-2.75,1)) #star

Sum_of_Notes=First_pair+Second_pair+Third_pair+Fourth_pair


plt.title('Song')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.plot(t,Sum_of_Notes)

sd.play(Sum_of_Notes,3*1024)