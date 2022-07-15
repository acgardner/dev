import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_theme()


x = np.linspace(0, 2.*np.pi)
f = lambda x: np.sin(x)

xmin, xmax = np.pi/2., np.pi

corners = np.array([
    [xmin, xmax],
    [f(xmin), f(xmax)]])

def draw_box(corners: np.array) -> None:
    """
        corners = np.array([[xmin, xmax], [ymin, ymax]])
    """
    sf = 0.1
    df = corners[1,1] - corners[1,0]

    bottom_edge_x = np.linspace(corners[0,0], corners[0,1])
    bottom_edge_y = (corners[1,0] - sf*df) * np.ones_like(bottom_edge_x)

    upper_edge_x = bottom_edge_x.copy()
    upper_edge_y = (corners[1,1] + sf*df) * np.ones_like(upper_edge_x)
    
    left_edge_y = np.linspace(corners[1,0] - sf*df, corners[1,1] + sf*df)
    left_edge_x = corners[0,0] * np.ones_like(left_edge_y)

    right_edge_y = left_edge_y.copy()
    right_edge_x = corners[0,1] * np.ones_like(right_edge_y)

    return bottom_edge_x, bottom_edge_y, upper_edge_x, upper_edge_y, left_edge_x, left_edge_y, right_edge_x, right_edge_y

bottom_edge_x, \
bottom_edge_y, \
upper_edge_x, \
upper_edge_y, \
left_edge_x, \
left_edge_y, \
right_edge_x, \
right_edge_y = draw_box(corners)

plt.figure()

plt.plot(x, f(x))
plt.plot(bottom_edge_x, bottom_edge_y, color="black")
plt.plot(upper_edge_x, upper_edge_y, color="black")
plt.plot(left_edge_x, left_edge_y, color="black")
plt.plot(right_edge_x, right_edge_y, color="black")
plt.plot(xmin, f(xmin), "*", color="red")
plt.plot(xmax, f(xmax), "*", color="red")

plt.show()
