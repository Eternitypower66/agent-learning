import requests

def shici_api():
  url = "https://v1.jinrishici.com/all.json"
  try:
      r=requests.get(url,timeout=5)#timeout为请求超时时间,等待服务器相应最多5秒
      if r.status_code==200:
           data=r.json()

           print(f"{data['category']}\n{data['origin']}\n{data['author']}\n{data['content']}")
      else:
           print("调用错误")
  except:
            print("网络问题!")
def IP_api(): 
  url="http://ip-api.com/json/"
  try:
    r=requests.get(url,timeout=5)
   
    if r.status_code==200:
         data=r.json()
         if 'country' in data:
             print(f"query:{data['query']}")
    
  except:
    print("网络问题!")
while True:
     print("你想要什么服务:1.随机古诗词,2.随机IP")
     option=input()
     if option =='1':
          shici_api()
     elif option =='2':
          IP_api()
     break
# print(data) #展示数据结构
# print(r.text[:10])#{}json格式 r.text为str字符串类型,需要先json解析为字典更好输出