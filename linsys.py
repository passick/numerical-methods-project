import numpy as np

def solve_linear_system(A, y):
    '''
    Solve linear system Ax=y.
    Works for such A that A.shape[0] >= A.shape[1].
    '''
    wide_A = np.hstack((A.astype(float), np.array([y]).T.astype(float)))
    for i in range(min(A.shape[0], A.shape[1])):
        max_index = i + np.argmax(np.abs(wide_A[i:, i]))
        if wide_A[max_index, i] == 0:
            print('No solution.')
            raise ValueError()
        wide_A[[i, max_index], :] = wide_A[[max_index, i], :]
        for j in range(A.shape[0]):
            if j == i:
                continue
            wide_A[j] -= (wide_A[j, i] / wide_A[i, i]) * wide_A[i]
        wide_A[i] /= wide_A[i, i]
    return wide_A[:, -1]
