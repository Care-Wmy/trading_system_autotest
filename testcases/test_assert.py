# 开发时间：2023/3/20 20:34

import pytest
from pytest_assume.plugin import assume


class TestAssert:
    def test_assert(self):
        with assume: assert 'aaa' in 'bbb'
        pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        print("完了")
        '''
        # == 、 != 、< 、> 、<= 、>=
        assert "aaa" == "aaa"
        assert "aaa" != "aaa"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7 - 2
        assert 4 > 1 + 2
        # 包含和不包含
        assert "aaa" in "aa自动化测试"
        assert "aaa" not in "自动化"
        # true和false
        assert 1
        assert (9 < 10) is True
        assert not False
        '''
