import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pass

    position_encodings = []
    for pos in range(seq_len):
        current_position = []
        for d in range(d_model):
            i = d // 2
            frequency = 1 / np.power(base, (2 * i) / d_model)
            encoding = np.cos(pos * frequency) if (d & 1) else np.sin(pos * frequency)
            current_position.append(encoding)
        position_encodings.append(current_position)
            
    return np.array(position_encodings, dtype = float)

    # dim i, i + 1 have same w
    # pe(pos, dim) 
print(positional_encoding(4, 4))