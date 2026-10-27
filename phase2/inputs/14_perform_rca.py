import os

from causallearn.search.FCMBased import lingam
from causallearn.search.FCMBased.lingam.utils import make_dot
from dowhy import CausalModel

from src.config import Config

def perform_rca(self, df, treatments):
    effects = []
    for treatment in treatments:
        model = CausalModel(data=df, treatment=treatment, outcome="revenue")
        identified_estimand = model.identify_effect()
      