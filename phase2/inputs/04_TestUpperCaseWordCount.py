import numpy as np
import pandas as pd

from featuretools.primitives import UpperCaseWordCount


class TestUpperCaseWordCount:
    primitive = UpperCaseWordCount

    def test_strings(self):
        x = pd.Series(
            [
                "This IS a STRING.",
                "Testing AAA",
                "Testing AAA BBB",
                "Testing TEsTIng AA3 AA_33 HELLO",
                "AAA $@()#$@@#$",
            ],
            dtype="string",
        )

