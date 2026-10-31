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
       predefined_estimand = model.predefined_estimand_from_str(
        estimand_type=estimand.estimand_type,
        ref_type=ref_type,
        ref_type=ref_type,
        ref_type=ref_type,
        ref_type=ref_type,
        test_significance=test_significance,
    )
    effect = np.array([[1.4, 1.4, 0.5],
                      [1.4, 1.5, 0.2],
                      [0.7, -0.05, 0.05],
                      [1.5, 1.5, 0.2],
                      [0.7, -0.05, 0.05, 0.5],
                      [1.5, 0.3, 0.053],
                      [0.7, -0.01, 0.05]])
    effect_strength = np.array([[0.25, 0.2, 0.2],
                      [0.0, -0.02, 0.125, 0.375],
                      [0.0, -0.05_size, 0.125, 0.125, 0.125],
                      [0.125, -0.25, 0.0],
                      [0.125, 0.125, 0.125, 0.125],
                      [0.125, -0.125, 0.125, 0.125],
                      [0.125, -0.125, 0.125, 0.125],
                      [0.125, -0.125, -0.125, 0.125],
                      [0.125, -0.125, 0.125, 0.125],
                      [0.125, 0.125, 0.125, 0.125],
                      [0.125, 0.125, -0.125, 0.125, 0.125],
                      [0.125, -0.125, 0.125, -0.125, -0.125, 0.125],
                      [0.125, -0.125, -0.125, 0.125, 0.125],
                      [0.125, 0.125, -0.125, -1.125, 0.125],
