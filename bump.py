import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# this class is used to run a bump test.

class bump:
    def __init__(self):
        '''
        This class is used to generate bump tests as either numpy arrays or pandas dataframes.
        bump.generate()
        '''
        pass

    def generate(self, bumpSize=1, startIndex=10, N=100, npy=True):
        '''
        Generates a bump test structure as either a numpy array or a pandas dataframe
        bumpSize: size of the step generated
        startIndex: index where the step occurs
        N: size of the array
        npy: True for numpy array; false for pandas dataframe output
        '''
        zero = np.zeros(shape=(startIndex))
        step = bumpSize * np.ones(shape=(N - startIndex))
        finalArray = np.concatenate((zero, step), axis=0)
        
        if npy:
            self.bumpData = finalArray
        else:
            self.bumpData = pd.DataFrame(data=finalArray)

        return self.bumpData