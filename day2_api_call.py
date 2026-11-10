print("--- 脚本开始运行 ---")

import requests

def get_temperature():
    """从公开api获取一条随机冷知识"""
    url="https://api.open-meteo.com/v1/forecast?latitude=39.9&longitude=116.4&current=temperature_2m"

    try:
        # 发送get请求，设置5秒超时时间
        response =requests.get(url,timeout=5)
        response.raise_for_status()
        data = response.json()
        return data.get("current", {}).get("temperature_2m")
    except requests.exceptions.RequestException as e:
        print(f"请求出错：{e}")
        return None

if __name__=="__main__":
    temp = get_temperature()
    print("--- Script Started ---")
    if temp is not None:
        print(f"Current Temperature in Beijing: {temp}°C")
    else:
        print(f"获取失败，请检查网络")