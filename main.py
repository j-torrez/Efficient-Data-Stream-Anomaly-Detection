from data_stream import generate_data_stream  # Corrected function name
from anomaly_detection import exponential_moving_average, detect_anomalies_with_ema
from visualization import live_plot

def main():
    ema = None  # Initialize EMA to None
    data_stream = generate_data_stream()  # Call the correct function for generating the data stream
    data_points = []
    anomaly_points = []

    for data_point in data_stream:
        ema = exponential_moving_average(data_point, ema)  # Update EMA with the current data point

        if detect_anomalies_with_ema(data_point, ema):  # Check for anomalies
            print(f"Anomaly Detected! Data: {data_point}, EMA: {ema}")
            anomaly_points.append(data_point)  # Append anomaly data point
        else:
            print(f"Normal Data: {data_point}, EMA: {ema}")
            anomaly_points.append(None)  # Append None if not an anomaly

        data_points.append(data_point)  # Append current data point
        live_plot(data_points, anomaly_points)  # Update the live plot with new data and anomalies

if __name__ == "__main__":
    main()  # Run the main function
