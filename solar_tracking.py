import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import requests
from pysolar.solar import get_altitude, get_azimuth
import pytz

def get_sun_times_from_web(latitude, longitude):
    response = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&formatted=0")
    data = response.json()["results"]
    
    sunrise = datetime.fromisoformat(data["sunrise"]).replace(tzinfo=pytz.utc)
    sunset = datetime.fromisoformat(data["sunset"]).replace(tzinfo=pytz.utc)
    
    return sunrise, sunset

def compute_sunflower_tracking(latitude, longitude):
    sunrise, sunset = get_sun_times_from_web(latitude, longitude)
    local_tz = pytz.timezone("Asia/Kolkata")
    sunrise = sunrise.astimezone(local_tz)
    sunset = sunset.astimezone(local_tz)
    
    times = [sunrise + timedelta(minutes=i) for i in range(0, int((sunset - sunrise).total_seconds() / 60), 5)]
    
    thetas = []
    phis = []
    for t in times:
        elevation = get_altitude(latitude, longitude, t)
        azimuth = get_azimuth(latitude, longitude, t)
        
        # Sunflower-like behavior: Always facing the sun
        theta = max(0, elevation)  # Tilt follows elevation
        phi = azimuth  # Orientation follows azimuth
        
        thetas.append(theta)
        phis.append(phi)
    
    return times, thetas, phis

def plot_sunflower_tracking(latitude, longitude):
    times, thetas, phis = compute_sunflower_tracking(latitude, longitude)
    
    plt.figure(figsize=(10,5))
    
    # Plot Theta vs Time
    plt.subplot(2,1,1)
    plt.plot(times, thetas, label='Tilt Angle (Theta)', color='blue')
    plt.ylabel('Theta (Degrees)')
    plt.xlabel('Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    
    # Plot Phi vs Time
    plt.subplot(2,1,2)
    plt.plot(times, phis, label='Orientation (Phi)', color='orange')
    plt.ylabel('Phi (Degrees)')
    plt.xlabel('Time')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    
    plt.tight_layout()
    plt.show()

def sunflower_tracking_equation(latitude, longitude, time):
    elevation = get_altitude(latitude, longitude, time)
    azimuth = get_azimuth(latitude, longitude, time)
    
    theta = max(0, elevation)  # Tilt follows elevation
    phi = azimuth  # Orientation follows azimuth
    
    return theta, phi

# Example Usage
latitude = 29.8667  # Roorkee
longitude = 77.8833
plot_sunflower_tracking(latitude, longitude)

time_sample = datetime.utcnow().replace(tzinfo=pytz.utc).astimezone(pytz.timezone("Asia/Kolkata"))
theta_eq, phi_eq = sunflower_tracking_equation(latitude, longitude, time_sample)
print(f"At {time_sample}, Theta: {theta_eq:.2f}, Phi: {phi_eq:.2f}")
