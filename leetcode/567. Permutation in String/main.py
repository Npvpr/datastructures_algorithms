GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"


def test(label, actual, expected):
    if actual == expected:
        print(f"{GREEN}✓ {label} passed{RESET}")
    else:
        print(
            f"{RED}✗ {label} failed: " f"expected {expected}, but got {actual}{RESET}"
        )


from neetcode import Solution as NeetCodeSolution
from collections_counter import Solution as CounterSolution

neetcode = NeetCodeSolution()
counter = CounterSolution()

test(
    "NC: Test case 1",
    neetcode.checkInclusion("ab", "eidbaooo"),
    True,
)

test(
    "NC: Test case 2",
    neetcode.checkInclusion("ab", "eidboaoo"),
    False,
)

test(
    "CC: Test case 1",
    counter.checkInclusion("ab", "eidbaooo"),
    True,
)

test(
    "CC: Test case 2",
    counter.checkInclusion("ab", "eidboaoo"),
    False,
)
