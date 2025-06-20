import numpy as np
import matplotlib.pyplot as plt
import pywt

# Load accelerometer data (3-axis)
data = np.loadtxt('C:\\Users\\Jimmy Angira\\OneDrive\\Documents\\Python\\CVS 590\\Raw Data 1.txt')

sample_rate = 20  # Hz
dt = 1.0 / sample_rate
time = np.arange(0, len(data) / sample_rate, dt)

# CWT configuration
wavelet = 'cmor'
num_scales = 100
scales = np.logspace(0.1, 2, num=num_scales)

# Initialize arrays to hold coefficients and peak frequencies
cfs = np.empty((3, len(scales), len(data)))
peak_frequencies = np.empty((3, len(data)))

# Perform CWT and extract peak frequency per axis
for i in range(3):
    cfs[i], frequencies = pywt.cwt(data[:, i], scales, wavelet, dt)
    peak_frequencies[i] = frequencies[np.argmax(np.abs(cfs[i]), axis=0)]

# Average across the three axes
average_peak_frequency = np.mean(peak_frequencies, axis=0)

# Find indices of max and min average peak frequencies
max_index = np.argmax(average_peak_frequency)
min_index = np.argmin(average_peak_frequency)

# Plot results
plt.figure(figsize=(12, 6))
plt.plot(time, average_peak_frequency, label='Average Peak Frequency')

# Mark max point
plt.scatter(time[max_index], average_peak_frequency[max_index], color='red',
            label=f'Max: {average_peak_frequency[max_index]:.2f} Hz')
plt.axvline(x=time[max_index], color='red', linestyle='--', linewidth=0.5)
plt.axhline(y=average_peak_frequency[max_index], color='red', linestyle='--', linewidth=0.5)
plt.text(time[max_index], average_peak_frequency[max_index],
         f'{average_peak_frequency[max_index]:.2f} Hz', ha='right', va='bottom', fontsize=8)

# Mark min point
plt.scatter(time[min_index], average_peak_frequency[min_index], color='green',
            label=f'Min: {average_peak_frequency[min_index]:.2f} Hz')
plt.axvline(x=time[min_index], color='green', linestyle='--', linewidth=0.5)
plt.axhline(y=average_peak_frequency[min_index], color='green', linestyle='--', linewidth=0.5)
plt.text(time[min_index], average_peak_frequency[min_index],
         f'{average_peak_frequency[min_index]:.2f} Hz', ha='right', va='bottom', fontsize=8)

# Final plot details
plt.ylabel('Average Peak Frequency (Hz)')
plt.xlabel('Time (s)')
plt.title('Average Peak Frequencies against Time for Sensor Position 1')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
