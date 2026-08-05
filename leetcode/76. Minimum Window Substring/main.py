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

neetcode = NeetCodeSolution()

# Normal test cases
test(
    "NC: Test case 1",
    neetcode.minWindow("OUZODYXAZV", "XYZ"),
    "YXAZ",
)

test(
    "NC: Test case 2",
    neetcode.minWindow("xyz", "xyz"),
    "xyz",
)

# Duplicate test cases
test(
    "NC: Test case 3",
    neetcode.minWindow("ABCDEFCE", "CE"),
    "CE",
)

test(
    "NC: Test case 4",
    neetcode.minWindow("ABCCEF", "CE"),
    "CE",
)

# Empty/Less than test cases
test(
    "NC: Test case 5",
    neetcode.minWindow("A", ""),
    "",
)

test(
    "NC: Test case 6",
    neetcode.minWindow("A", "AA"),
    "",
)
