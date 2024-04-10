from numpy import pi as PI

# ---------------------------------------------
# Lidar parameters
# ---------------------------------------------
SCAN_RANGE = 50  # meters

# ---------------------------------------------
# Map parameters
# ---------------------------------------------
GRID_CELL_WIDTH = 0.5  # dimension of a grid cell
GRID_WIDTH = SCAN_RANGE * 2  # dimension of the entire grid
GRID_SIZE = int(GRID_WIDTH / GRID_CELL_WIDTH)  # grid horizontal/vertical cell count

