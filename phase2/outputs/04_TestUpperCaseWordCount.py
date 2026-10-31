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

        result = build("df", expand=False)
        expected = test_case(x)
        assert len(result) == 4 and (len(result) == 2) == 2
        # The test below gives a shorthand; we should raise it
        # asked and the test below gives the expected value.
        self.assertIn().check_utils().convert_container(x)

        # Denote: the test below will raise the invalid warning when the
        # test fails.
        with self.assertRaises(ValueError, match="damping a long integer"):
            build(x)

        # Denote. Denote is already beness than the test above.
        test_case(x)
