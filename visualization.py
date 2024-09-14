import matplotlib.pyplot as plt

"""
Create a graph, plot the data stream in real time and highlights all the anomalies

"""

fig, ax = plt.subplots()

def live_plot(data_points, anomaly_points):

	ax.clear()
	
	ax.plot(data_points, label = "Data Stream") #Plot the data Stream
	ax.scatter(range(len(anomaly_points)), anomaly_points, color = 'r', label = "Anomalies", zorder= 5) # Mark anomalies 
	ax.legend()

	plt.draw()
	plt.pause(0.1) # Pause to update the plot