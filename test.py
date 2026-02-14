import requests






# 创建会话
session = requests.Session()
headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "http://foodieguide.com",
        "Pragma": "no-cache",
        "Referer": "http://foodieguide.com/iptvsearch/",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

r = session.get('http://foodieguide.com/iptvsearch/iptvmulticast.php?page=1&iphone16=&code=',headers=headers)
# 后续请求自动携带Cookie
print(r.text.find("直播"))
with open('test_y.txt', 'w', encoding='utf-8') as f:
    # 获取当前日期并格式化 # 输出示例：2026-02-06
    f.write(r.text + '\n' + r.text.find("直播"))
    print('write ok')
