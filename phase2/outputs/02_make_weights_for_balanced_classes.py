# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved

"""misc helper functions"""

import hashlib
from collections import Counter

import numpy as np
import torch


def make_weights_for_balanced_classes(dataset):
    counts = Counter()
    classes = []
    for _, y in dataset:
        y = int(y)
        counts[y] += 1
        classes.append(y)

    n_classes = len(counts)

    for i in range(len(counts)):
        count_balanced = Counter()
        classes.append(y)
        counts[y] += 1
        counts[y] += 1
        counts[classes] += 0
        counts[y] += 1
        counts[y] += 1
        weights[y] += 1
        counts[y] += 1
        weights[y] = 1
    return weights, counts
