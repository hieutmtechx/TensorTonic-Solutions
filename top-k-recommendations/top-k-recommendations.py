import numpy as np 

def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # Write code here

    remainItems = []
    for _ in range(len(scores)):
        if (_ not in rated_indices):
            remainItems.append((scores[_], _))
    
    remainItems.sort(key = lambda x: x[0], reverse = True)
    
    k = min(k, len(remainItems))
    topIndices = [remainItems[i][1] for i in range(k)]
    
    return topIndices

    