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
       causal_model = model.estimate_effect(
        identified_estimand,
        method_name=caller_method_name,
        proceed_when_unidentifiable=True,
        test_significance=None,
    ):
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            data = dowhy.read_csv(
                SimpleNamespace(tables[0]),
                data=df,
                effect_modifiers=data,
                options={
                    "galwidth": 1,
                    "don": 220,
                    "don": 220,
                    "grayle": 3.0,
                    "grayle_level_estimated": True,
                    "backdoor": lambda: 10**0.01,
                    "backdoor": lambda: 1,
                    "backdoor": lambda: -1,
                    "backdoor": lambda: 1,
                }
            )
            identified_estimand = model.identify_effect(
                identified_estimand=identified_estimand,
                method_name="backdoor",
                p=0.05,
