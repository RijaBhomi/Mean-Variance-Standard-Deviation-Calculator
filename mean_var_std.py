import numpy as np

def calculate(list):
    # accpets 9 numbers, otherwise throw specific error
    if len(list) !=9:
        raise ValueError("List must contain nine numbers.")

    matrix= np.array(list).reshape(3,3)  # converts python list to numpy array, reshape lays it out as 3 rows 3 columns

    #
    calculations= {
        'mean': [matrix.mean(axis=0).tolist(),matrix.mean(axis=1).tolist(), matrix.mean().item()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().item()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().item()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().item()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().item()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().item()],

    }

# returns a plain python dictionary of plain python lists
    return calculations