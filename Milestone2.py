import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft

C_4=261.63 #c4

G_4=392 #g4

A_4=440 #A4

t = np.linspace(0,3,12*1024)

Left_hand=np.sin(2*np.pi*0*t)

First_pair=1.5*(Left_hand+np.sin(2*np.pi*C_4*t))*(np.heaviside(t,1)-np.heaviside(t-0.5,1)) #Twinkle

Second_pair=(Left_hand+np.sin(2*np.pi*G_4*t))*(np.heaviside(t-0.75,1)-np.heaviside(t-1.25,1)) #Twinkle

Third_pair=1.5*(Left_hand+np.sin(2*np.pi*A_4*t))*(np.heaviside(t-1.5,1)-np.heaviside(t-2,1)) #little

Fourth_pair=(Left_hand+np.sin(2*np.pi*G_4*t))*(np.heaviside(t-2.25,1)-np.heaviside(t-2.75,1)) #star

Original_song=First_pair+Second_pair+Third_pair+Fourth_pair

sd.play(Original_song,3*1024) # original song

    
# to plot Original_song in time domain

plt.title('Original Song in Time domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(t,Original_song)  #first figure 
plt.figure()


N = 3*1024   #no of samples1

𝑓 = np.linspace(0 , 512 ,int(𝑁/2)) #frequency axis


# to plot Original_song in frequency domain

x_f = fft(Original_song)
x_f = 2/N*np.abs(x_f[0:np.int64(N/2)]) # transform original song by fourier transform
plt.title('Original Song in frequency domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.plot(f,x_f)   #second figure 
plt.figure()


𝑓𝑛1,𝑓𝑛2= np.random.randint(0,512,2) # to generate random frequencies to make noise


# to plot contaminated Song in time domain
Noise=np.sin(2*np.pi*𝑓𝑛1*t)+np.sin(2*np.pi*𝑓𝑛2*t)
contaminated_Song=Noise+Original_song     # original song with noise
plt.title('Contaminated Song in time domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(t,contaminated_Song)   #Third figure 
plt.figure()




# to plot contaminated Song in frequency domain
x_nf = fft(contaminated_Song)
x_nf = 2/N*np.abs(x_nf [0:np.int64(N/2)])
plt.title('Contaminated Song in frequency domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.plot(f,x_nf)   #fourth figure 
plt.figure()



length=len(f)

maxfreq1=0
maxfreq2=0

max_peak_of_x_f=int(round(np.max(x_f)+1))

for i in range (length):
    if x_nf[i]>max_peak_of_x_f:
        maxfreq1=f[i]
        
for i in range (length):
     if x_nf[i]>max_peak_of_x_f and f[i]!=maxfreq1:
         maxfreq2=f[i]       
           

f3n=int(round(maxfreq1))
f4n=int(round(maxfreq2))

x_filtered_t=contaminated_Song-(np.sin(2*np.pi*f3n*t)+np.sin(2*np.pi*f4n*t))

# to plot filtered Song in time domain
plt.title('filtered Song in time domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.plot(t,x_filtered_t)   #Fifth figure 
plt.figure()



# to plot filtered Song in frequency domain
filtered_in_freq_domain = fft(x_filtered_t)
filtered_in_freq_domain = 2/N*np.abs(filtered_in_freq_domain[0:np.int64(N/2)])
plt.title('filtered Song in frequency domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.plot(f,filtered_in_freq_domain)   #sixth figure 
plt.figure()


#sd.play(x_filtered_t,4*1024)


"""show Original Song in time and frequency domain in one figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

ax1.plot(t,Original_song)
ax1.set_title('Original Song in Time domain')

ax2.plot(f,x_f)
ax2.set_title('Original Song in frequency domain')

fig.suptitle('Original Song in time and frequency domain')
plt.show()
plt.figure()
"""



"""show contaminated Song in time and frequency domain in one figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

ax1.plot(t,contaminated_Song)
ax1.set_title('contaminated Song in Time domain')

ax2.plot(f,x_nf)
ax2.set_title('contaminated Song in frequency domain')

fig.suptitle('contaminated Song in time and frequency domain')
plt.show()
plt.figure()
"""


"""show filtered Song in time and frequency domain in one figure
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10, 5))

ax1.plot(t,x_filtered_t)
ax1.set_title('filtered Song in Time domain')

ax2.plot(f,filtered_in_freq_domain)
ax2.set_title('filtered Song in frequency domain')

fig.suptitle('filtered Song in time and frequency domain')
plt.show()
plt.figure()
"""


