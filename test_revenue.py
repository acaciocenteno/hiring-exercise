import pytest as pytest

from revenue import calculate_totals


@pytest.mark.parametrize(
    'filename, period_start_as_str, period_end_as_str, expected_result',
    [
        (
            'small.data',
            '2021-01-01',
            '2021-12-31',
            [
                (1, 20.),
                (2, 10.),
            ],
        ),
    ]
)
def test_calculate_totals(filename,
                          period_start_as_str,
                          period_end_as_str,
                          expected_result):
    result = calculate_totals(filename, period_start_as_str, period_end_as_str)
    assert result == expected_result
