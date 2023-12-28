# ожидается "1 failed, 1 skipped, 1 xfailed"

import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail()
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False