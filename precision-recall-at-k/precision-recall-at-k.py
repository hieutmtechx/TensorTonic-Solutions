def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    if (k == 0): return [0.0, 0.0]
    
    pairwise = 0
    relevant = set(relevant)
    k = min(k, len(recommended))
    for _ in range(k):
        if (recommended[_] in relevant):
            pairwise += 1  

    print(pairwise)
    precision = pairwise / k
    recall = pairwise / len(relevant) if relevant else 0.0
    return [precision, recall]