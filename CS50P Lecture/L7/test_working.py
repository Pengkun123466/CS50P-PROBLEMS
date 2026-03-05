import pytest
from working import convert

# 1. 核心业务逻辑测试（常规转换）
def test_valid_times():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"

# 2. 边缘场景测试（最容易翻车的时空陷阱 12 AM / 12 PM）
def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"

# 3. 恶意输入测试（格式错误，没有用 to 连接）
def test_invalid_format():
    # 使用 with pytest.raises(ValueError): 告诉质检员：“我预期下面这行代码会引发崩溃，如果它没崩溃，那就是代码写错了！”
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

# 4. 恶意输入测试（时间数值越界）
def test_invalid_time():
    # 分钟到了 60
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    # 小时写了 13
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")