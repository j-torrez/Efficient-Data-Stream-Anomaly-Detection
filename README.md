# Efficient Data Stream Anomaly Detection

## Project Overview

This project is designed to simulate a **real-time data stream** and detect **anomalies** in the data. The data stream represents a continuous sequence of values, such as financial transactions or system metrics. The goal of this project is to identify data points that **deviate significantly** from normal behavior, which we call anomalies. These could represent unusual activities like errors, fraud, or system failures.

## How It Works

The project uses a **sine wave** to simulate regular patterns (seasonal variations) and adds **random noise** to make the data stream look more realistic. The anomaly detection is based on the **Exponential Moving Average (EMA)** algorithm, which tracks the general trend of the data.

Each new data point is compared to the EMA. If the difference (deviation) between the data point and the EMA is larger than a certain percentage, we flag the data point as an anomaly.

## Algorithm: Exponential Moving Average (EMA)

We chose the **Exponential Moving Average (EMA)** as our core algorithm for anomaly detection. The EMA is a type of **moving average** that gives more importance to recent data points, making it quick to react to new changes in the data. This is especially useful for detecting anomalies in **real-time** because:

- **It adapts dynamically**: The EMA quickly adjusts to changes in the data stream, making it suitable for detecting sudden spikes or drops.
- **It smooths out random noise**: While the EMA reacts quickly to major changes, it smooths out smaller, random fluctuations (noise), so not every small change is flagged as an anomaly.

In summary, EMA is effective for **real-time anomaly detection** because it balances **sensitivity** (quickly reacting to changes) with **stability** (ignoring small, random variations). This makes it a good choice for detecting unusual behavior in continuous data streams.

## Key Features

- **Data Stream Simulation**: The program generates a continuous data stream that includes both regular patterns and random noise.
- **Real-Time Anomaly Detection**: The EMA algorithm checks each data point and flags any points that deviate significantly from the expected pattern.
- **Visualization**: A real-time plot shows the data stream, with anomalies highlighted in red for easy identification.

## Installation

To run this project, you need Python 3.x installed on your machine. You also need the following libraries:

- `matplotlib`
- `numpy`

You can install the required libraries using this command:

```bash
pip install -r requirements.txt

## Start Project

To run this project:

- `python main.py`