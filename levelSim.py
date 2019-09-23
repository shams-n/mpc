import numpy as np
import pandas as pd
import bump

# NOTES:
# - start off with SISO system, easier to use at first
#     - need one output variable and one input variable (one MV and one CV) 
#     - tank level system
#     - transfer function is available

# DEFINE CONSTANTS
Rv = 4.01 * (10 ** -5) #in units of cubic meters per second
A = 5 # in square meters

