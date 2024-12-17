import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Common edge detection method for grayscale images (perfect for this)
def find_high_boundary_areas(mask : np.ndarray, num_targets : int = 10) -> np.ndarray :

    # Convolve kernel with edges to find regions with highest density of boundaries
    ks = 10 # kernel size
    kernel2d = np.ones((ks,ks))

    boundary_density = signal.convolve2d(mask, kernel2d, mode='same', boundary='fill')

    # Generate scan target coordinates
    scan_size = 10
    n_targets = num_targets

    target_map = boundary_density.copy()

    coords = np.zeros((n_targets, 2))

    for ii in range(n_targets):
        coord = np.unravel_index(np.argmax(target_map), target_map.shape) # Find maximum density of boundaries in the current target map
        x_min = np.max((int(coord[1]-scan_size/2), 0))
        x_max = np.min((int(coord[1]+scan_size/2), target_map.shape[1]))
        y_min = np.max((int(coord[0]-scan_size/2), 0))
        y_max = np.min((int(coord[0]+scan_size/2), target_map.shape[1]))
        target_map[y_min:y_max, x_min:x_max] = 0 # Block out an area of scan_size**2 around to stop repeat imaging of the same region.

        coords[ii] = coord

    return coords