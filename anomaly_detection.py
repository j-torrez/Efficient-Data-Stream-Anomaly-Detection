def exponential_moving_average(data_point, prev_ema, alpha = 0.1):

	"""
	We use tree arguments, we tried to implement recursion function.

	Our Function is based on the EMA formula (Exponential moving average)
	Args:
	data point: Current data point in the stream (Float numbers)
	prev_ema: The previous EMA value
	alpha: The smothing factor, default: 0.1 (According to our EMA formula)
	"""

	if prev_ema is None:
		return data_point # We are basically going to initialize EMA with the first data point
	return  alpha * data_point + (1 - alpha) * prev_ema


def detect_anomalies_with_ema(data_point, ema, threshold = 20):
	"""
	This function will detect the anomalies. It will compare the data point with the current EMA and if it is above the threshold we 
	previously set (20%) it will flagged the data point as an anomalie

	Args:
	Data point: Current Data Point
	ema: Current EMA value
	threshold: The percentage deviation that is falgged as an anomalie 
	"""

	deviation = abs(data_point - ema) / ema * 100 # Calculate the percentage deviation from EMA
	return deviation > threshold # If the deviation exceed the threshold, its an anomaly