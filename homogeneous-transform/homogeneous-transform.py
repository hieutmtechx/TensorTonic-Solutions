import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    pass

    inspect_points = np.asarray(points)

    if (np.ndim(inspect_points) == 1 and inspect_points.shape[0] == 3):
        print("hehe")
        points.append(1)
    else:
        for point in points:
            point.append(1)
            
    points = np.asarray(points, dtype = float)

    _points = np.dot(T, points.T)
    result = (_points[:3]).T
    return result