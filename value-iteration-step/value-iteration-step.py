import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here

    value = np.asarray(values, dtype = float)
    transition = np.asarray(transitions, dtype = float)
    reward = np.asarray(rewards, dtype = float)

    Qvals = reward + gamma * np.dot(transition, value) 
    output = np.max(Qvals, axis = 1)

    return list(output)      