import numpy as np
def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    # Write code here

    rates = []
    for item in items:
        avg_rate, vote_count = item
        wr = vote_count / (vote_count + min_votes) * avg_rate + min_votes / (vote_count + min_votes) * global_mean
        rates.append(wr)

    return rates
