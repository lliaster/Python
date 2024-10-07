info_dict = {
    "name": "chaibao2",
    "type": "2",
    "url": "",
    "range": "1-100",
}

def worker(name,type,url,range):
    print(f'name:{name},type:{type},rul:{url},range:{range}')
worker(**info_dict)


def get_info (url):
    print(url)

rul1 = 'www.baidu.com'
rul2  = 'www.google.com'
rul3 = 'www.sogou.com'

url_list = [get_info for _ in range(3)]
print(url_list)

for i in url_list:
    i(rul1)
    i(rul2)
    i(rul3)
print(get_info)