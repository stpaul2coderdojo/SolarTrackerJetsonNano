# Solar Tracking Robot - Sunflower Simulation

This project simulates a **sunflower-like solar tracking system** for a **tilting solar panel mounted on an autonomous robot**. The system dynamically **retrieves sunrise and sunset times from the web**, computes optimal tilt (θ) and orientation (φ) to always face the sun, and plots their variations throughout the day.

## Features
- **Fetches** real-time sunrise & sunset data for any latitude & longitude.
- **Computes** optimal **tilt (θ) and orientation (φ)** based on solar altitude & azimuth.
- **Plots** Theta vs. Time and Phi vs. Time to visualize tracking performance.
- **Uses Pysolar** for solar position calculations and **matplotlib** for plotting.

## Installation
1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/solar-tracking-robot.git
   cd solar-tracking-robot
   ```
2. **Install dependencies:**
   ```bash
   pip install numpy matplotlib requests pysolar pytz
   ```

## Usage
Run the main script to compute solar tracking for Roorkee:
```bash
python solar_tracking.py
```

To get the **sunflower-tracking equation** for any specific time:
```python
from datetime import datetime
from pytz import timezone

time_sample = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(timezone("Asia/Kolkata"))
theta, phi = sunflower_tracking_equation(latitude=29.8667, longitude=77.8833, time=time_sample)
print(f"At {time_sample}, Theta: {theta:.2f}, Phi: {phi:.2f}")
```

## License
MIT License
