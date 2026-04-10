import numpy as np

def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    # Write code here

    outputs = []
    for s in range(len(rewards)):
        Qvals = []
        for a in range(len(transitions[s])):
            transition = np.asarray(transitions[s][a], dtype = float)
            Qval = rewards[s][a] + gamma * np.sum(transition * values)
            Qvals.append(Qval)
        outputs.append(np.max(Qvals))

    return outputs        