import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size / feature_size

    anchor_boxes = []
    for i in range(feature_size):
        for j in range(feature_size):
            cx = stride * (j + 0.5)
            cy = stride * (i + 0.5)
            for scale in scales:
                for aspect_ratio in aspect_ratios:
                    w = scale * np.sqrt(aspect_ratio)
                    h = scale / np.sqrt(aspect_ratio)
                    anchor_boxes.append([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2])

    return anchor_boxes