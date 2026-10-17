from p1_d2_engine.validators import consecutive_annual_periods, is_annual_duration


def test_annual_duration():
    assert is_annual_duration("2024-01-01", "2024-12-31")
    assert not is_annual_duration("2024-10-01", "2024-12-31")


def test_consecutive_years():
    assert consecutive_annual_periods("2023-12-31", "2024-12-31")
