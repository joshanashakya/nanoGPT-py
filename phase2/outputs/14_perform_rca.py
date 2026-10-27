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
       summary = causal.summary(
            data=df, treatment=outcome, graph=data["df"], graph=data["treatment_names"][treatment_name]
        )
        all_observed_observed = [
            n
                for n in treatments[treatment[treatment_name]].sum()
            for n in treatments
            for n in treatments[treatment_name]
        ]

        all_observed_observed = [
            n
                for n in treatments[treatment_name]
                for n in treatments[treatment_name]
            ]

            all_observed_observed = [
                n
                for n in treatments[treatment_name]
                for n in treatments[treatment_name]
                for n in treatments[target_units].sum()
            ]

            if treatment_name not in all
