from day2_api_call import get_temperature

def test_get_temperature_returns_float():
    """测试是否返回了数字类型的温度"""
    temp=get_temperature()
    if temp is not None:
        assert isinstance(temp,(int,float))
        print(f"\nTeset passed! Temperature:{temp}°C")