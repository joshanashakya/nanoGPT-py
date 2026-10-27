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
        estimate = model.estimate_effect(identified_estimand, method_name="backdoor.linear_regression")
        value = round(estimate.value, 4)
        explanation = f"As the {treatment} increases, revenue decreases." if value < 1 else f"As the {treatment} increases, revenue also increases."
        effects.append({"variable": treatment, "impact": "-ve" if value < 1 else "+ve", "value": value,
                        "explanation": explanation})
    return effects