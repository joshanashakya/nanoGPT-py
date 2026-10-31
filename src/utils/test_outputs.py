import argparse
import json
import subprocess
import sys
from pathlib import Path

from src.config import Config

# (output file, function to call, arguments, expected result). A function of None means the file is a script:
# it only has to run without an error. `_prepare_data` is a method that needs a class, so it is only run as a script.
CASES = [
    ("ordinary/01_tuple2str.py", "tuple2str", [["fly", "NN"]], "fly/NN"),
    ("ordinary/02_prepare_data.py", None, [], None),
    ("ordinary/03_below_zero.py", "below_zero", [[1, 2, -4, 5]], True),
    ("ordinary/04_convert_to_line_delimits.py", "convert_to_line_delimits", ['[{"a":1},{"b":2}]'], ['{"a":1}', '{"b":2}']),
    ("misleading/01_tuple2str.py", "tuple2str", [["fly", "NN"]], "fly/NN"),
    ("misleading/02_prepare_data.py", None, [], None),
    ("misleading/03_below_zero.py", "below_zero", [[1, 2, -4, 5]], True),
    ("misleading/04_convert_to_line_delimits.py", "convert_to_line_delimits", ['[{"a":1},{"b":2}]'], ['{"a":1}', '{"b":2}']),
    ("security/02_parse_xml.py", "parse_xml", ["<a><b/></a>"], None),
    ("training/02_binary_distance.py", "binary_distance", [1, 3], 1.0),
    ("training/03_log_base2.py", "log_base2", [8], 3.0),
    ("long_context/01_soft_evaluate.py", None, [], None),
    ("long_context/02_ridge_plot.py", None, [], None),
    ("long_context/03_TestToPeriod.py", None, [], None),
    ("long_context/04_effectsize_oneway.py", None, [], None),
    ("prompt_variations/01_lemma_base.py", None, [], None),
    ("prompt_variations/02_lemma_reword.py", None, [], None),
    ("prompt_variations/03_lemma_w_code.py", None, [], None),
    ("prompt_variations/04_lemma_pos.py", None, [], None),
    ("security/01_yaml_load.py", None, [], None),
    ("security/03_profile.py", None, [], None),
    ("security/04_profile.py", None, [], None),
    ("training/01_num2date.py", None, [], None),
    ("training/04_optimize_qap.py", None, [], None),
]

# Runs in a separate process, so a crash or an endless loop in generated code cannot stop the test run.
DRIVER = """
import json, sys
path, name, args, expected = sys.argv[1], sys.argv[2], json.loads(sys.argv[3]), json.loads(sys.argv[4])
namespace = {"__name__": "generated"}
exec(compile(open(path, encoding="utf-8").read(), path, "exec"), namespace)
if name != "None":
    result = namespace[name](*args)
    if isinstance(result, str) and isinstance(expected, list):
        result = result.strip().splitlines()
    assert result == expected, f"got {result!r}, expected {expected!r}"
"""


def run_case(path, name, args, expected, timeout):
    """Returns ('pass', '') or ('fail', error type and message)."""
    command = [sys.executable, "-I", "-c", DRIVER, str(path), str(name), json.dumps(args), json.dumps(expected)]
    try:
        done = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return "fail", f"timeout after {timeout}s"
    if done.returncode == 0:
        return "pass", ""
    last_line = done.stderr.strip().splitlines()[-1] if done.stderr.strip() else "no error message"
    return "fail", last_line


def parse_args():
    parser = argparse.ArgumentParser(description="Run simple tests on the Phase 3 outputs.")
    parser.add_argument("--outputs-dir", default=f"{Config.ROOT_DIR}/phase3/outputs")
    parser.add_argument("--timeout", type=int, default=20)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    passed = 0

    for file_name, function, arguments, expected in CASES:
        status, message = run_case(Path(args.outputs_dir) / file_name, function, arguments, expected, args.timeout)
        passed += status == "pass"
        print(f"{status:4}  {file_name}  {message}")

    print(f"\n{passed} of {len(CASES)} pass")
