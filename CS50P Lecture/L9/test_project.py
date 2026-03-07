import pytest
import sys
from project import check_csv, get_funds, calculate

def test_check_csv(monkeypatch):
    #用户什么都没输入就回车了
    monkeypatch.setattr(sys, 'argv', ['project.py'])
    with pytest.raises(SystemExit):
        check_csv()
        
    #用户输了一个不是 csv 的文件
    monkeypatch.setattr(sys, 'argv', ['project.py', 'wrong_file.txt'])
    with pytest.raises(SystemExit):
        check_csv()

def test_calculate():
    #假账本
    mock_funds_list = [
        {"fund_code": "000001", "shares": 100.0, "total_cost": 100.0, "current_price": 1.5, "pnl": 0.0},
        {"fund_code": "110011", "shares": 200.0, "total_cost": 300.0, "current_price": 2.0, "pnl": 0.0}
    ]
    
    # 基金1：(100 * 1.5) - 100 = 50.0 盈利
    # 基金2：(200 * 2.0) - 300 = 100.0 盈利
    # 总计等于 150.0
    assert calculate(mock_funds_list) == 150.0

def test_get_funds_invalid():
    # 传给一个不存在的假代码
    # 触发 except requests.RequestException 并执行 sys.exit 退出
    with pytest.raises(SystemExit):
        get_funds("invalid_code_999999")