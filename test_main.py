import pytest
from main import sums


@pytest.mark.parametrize(
    "array_input,target_input,expected",
    [
        pytest.param([1, 9, 5, 0, 20, -4, 12, 16, 7],
                     12, {5: 7, 0: 12, -4: 16}),
        pytest.param([1], 20, {}),
        pytest.param([1, -33], -32, {1: -33}),
        pytest.param([-64, -33], -97, {-64: -33}),
        pytest.param([], 0, {})
    ]
)
def test_sums(array_input, target_input, expected):
    assert sums(array_input, target_input) == expected
