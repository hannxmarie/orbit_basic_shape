import numpy as np
import matplotlib.pyplot as plt
from api_calls import User, Project, get_info

data_file = f'{User}/{Project}/data.JSON'
data = get_info(data_file)
data = data[0]

name = str(data['SATNAME'])
period = float(data['PERIOD'])
inclination = float(data['INCLINATION'])
apogee = float(data['APOGEE'])
perigee = float(data['PERIGEE'])

# Semi-major axis (average of Apogee and Perigee)
a = (apogee + perigee) / 2

# Semi-minor axis calculation based on elliptical orbit
b = np.sqrt(apogee * perigee)

# Focus distance (c) from the center of the ellipse to the foci (where Earth is located)
c = np.sqrt(a**2 - b**2)

# Generate theta for plotting the ellipse
theta = np.linspace(0, 2 * np.pi, 500)

# Parametric equations for the ellipse (Earth at focus, (0,0))
x = a * np.cos(theta) - c  # Shift the x values by -c to place Earth at the focus
y = b * np.sin(theta)