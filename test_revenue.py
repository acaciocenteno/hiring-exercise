import pytest as pytest

from revenue import calculate_totals


@pytest.mark.parametrize(
    'filename, period_start_as_str, period_end_as_str, expected_result',
    [
        (
            'tiny.data',
            '2021-01-01',
            '2021-12-31',
            [
                (1, 20.),
                (2, 10.),
            ],
        ),
        (
            'small.data',
            '2021-01-01',
            '2021-12-31',
            [
                (13, 210000.),
                (9, 64000.),
                (4, 30000.),
                (3, 5000.),
                (8, 3000.),
                (11, 2500.),
                (1, 1900.),
                (6, 400.),
                (2, 210.),
                (5, 150.),
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
