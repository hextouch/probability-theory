"""
Mutual information between two discrete variables
"""
import numpy as np

def mutual_information(joint, px, py):
    mi = 0.0
    for i in range(len(px)):
        for j in range(len(py)):
            if joint[i, j] > 0:
                mi += joint[i, j] * np.log2(joint[i, j] / (px[i] * py[j]))
    return mi

joint = np.array([[0.25, 0.25], [0.25, 0.25]])
px = np.sum(joint, axis=1)
py = np.sum(joint, axis=0)
print(f"Mutual information: {mutual_information(joint, px, py):.3f} bits")
