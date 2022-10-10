import numpy as np
import os
import pandas as pd


def print_hi(name):
    x_offsets = np.sort(np.concatenate((np.arange(-(12 - 1), 1, 1),)))
    y_offsets = np.sort(np.arange(1, (12 + 1), 1))
    print(x_offsets.shape)
    print(x_offsets)
    print(y_offsets.shape)
    print(y_offsets)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
