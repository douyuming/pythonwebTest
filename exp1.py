import requests


headers = {
            "Accept":"application/json;charset=UTF-8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US",
            "Connection":"keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Cookie":"",
            "Host": "zoj.pintia.cn",
            "Referer": "https://zoj.pintia.cn/problem-sets/91827364500/problems?page=2",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "X-Lollipop": "",
            "X-Marshmallow": ""
}
html = requests.get('https://zoj.pintia.cn/api/problem-sets/91827364500/problem-list?exam_id=0&page=2&limit=100&problem_type=PROGRAMMING',  headers=headers)
print(html.text)
