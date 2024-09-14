import random
import math
import time

def generate_data_stream():

	t = 0
	while True:
		seasonal_pattern = 50 * math.sin(0.1 * t) # This simulate the pattern, in this case is a sine wave that we want to simulate to make it real
		random_noise = random.uniform(-10, 10) # This is use to add random noise to our data, to make it look real
		data = 100 + seasonal_pattern + random_noise # Baseline value + seasonal pattern + random noise
		yield data # Return the generated data
		t += 1
		time.sleep(1) #Wait a second to generate the other data point 
