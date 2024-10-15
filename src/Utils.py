import numpy as np

def save_results(gm, 
                 name_method : str = 'Max', 
                 path : str = r'src/Results'):
    
    if not gm.confidence_1D is None:
        np.save(f'{path}/Confidence/{name_method}.npy', gm.confidence_1D) 
    if not gm.confidence_2D is None:
        np.save(f'{path}/Confidence/{name_method}.npy', gm.confidence_2D)
    np.save(f'{path}/Mean Clusters/{name_method}.npy', gm.cluster_means)


def get_means(name_method : str = 'Max', 
              path : str = r'src/Results TES'):
    try:
        means = np.load(f'{path}/Mean Clusters/{name_method}.npy') 
    except:
        means = None
    return means