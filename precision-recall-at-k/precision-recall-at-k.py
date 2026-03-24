def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here

    precision = 0
    recall = 0

    pairwise = 0
    
    for _ in range(k):
        if (recommended[_] in relevant):
            pairwise += 1  

    print(pairwise)
    precision = pairwise / k
    recall = pairwise / len(relevant)
    return [precision, recall]