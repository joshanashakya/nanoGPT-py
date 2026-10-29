from __future__ import annotations

import os

import numpy as np
import pandas as pd
import torch
from loguru import logger
from sklearn.metrics import accuracy_score
from torch import nn
from torch.utils.data import DataLoader

from src.configs import classification_config
from src.configs import settings
from src.models.nlp.classification_engine import classification_utils
from src.models.nlp.classification_engine.architecture.net import FeedbackClassifier
from src.models.nlp.classification_engine.data_loader import FeedbackDataset
from src.utils import common_utils


class SoftEvaluation:
    """
    Class to perform soft evaluation of the model.
    Note: To run the methods of this class make sure that the property "multi_tag" in config.json is set to true.
    Args:
        labels_map (dict): A mapping of label index to labels.
        config (dict): A configuration of the model.
        checkpoint_path (str): A checkpoint path.
        model_id (str): ID of the model which will be used to create reports directory.
        model (src.models.nlp.classification_engine.architecture.net.FeedbackClassifier): A FeedbackClassifier model
        to evaluate.
    """

    def __init__(self, labels_map, config, checkpoint_path=None, model_id=None, model=None):
        """
        Initializes the variables.
        Args:
            labels_map (dict): A mapping of label index to labels.
            config (dict): A configuration of the model.
            checkpoint_path (str): A checkpoint path.
            model_id (str): ID of the model which will be used to create reports directory.
            model (src.models.nlp.classification_engine.architecture.net.FeedbackClassifier): A FeedbackClassifier model
            to evaluate.
        """
        self.classes_map = classes_map
        self.classes_map = classes_map
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.model_id = model_id
        self.
