import json
import random
AT = 0
DO = 1

class I:
    def gen(self):
        key = random.randint(0,1)
        ret = '我'
        if key == 0:
            try:
                dic = json.load(open("do.json",'r',encoding='utf-8'))
                ret = ret + dic['key'] + dic['do'][random.randint(0, len(dic['do'])-1)]
            except (FileNotFoundError,FileExistsError):
                print("File do.json is not founded,please get the newest verson at:https://github.com/DengHaoyu/Rude")
                exit()
            except (Exception) as e:
                print(e)
                # print("Exceptrion has occurred,please retry or get the newest version
                # at:https://github.com/DengHaoyu/Rude")
                exit()
            try:
                dic = json.load(open("dosometing.json", 'r',encoding='utf-8'))
                ret = ret + dic['thing'][random.randint(0,len(dic['thing'])-1)]
            except (FileNotFoundError, FileExistsError):
                print("File dosomething.json is not founded,please get the newest verson "
                      "at:https://github.com/DengHaoyu/Rude")
                exit()
            except (Exception) as e:
                print(e)
                # print("Exceptrion has occurred,please retry or get the newest version
                # at:https://github.com/DengHaoyu/Rude")
                exit()
        else:
            try:
                dic = json.load(open("at.json",'r',encoding='utf-8'))
                ret = ret + dic['key'] + dic['place'][random.randint(0, len(dic['place']))-1]
            except (FileNotFoundError,FileExistsError):
                print("File at.json is not founded,please get the newest verson at:https://github.com/DengHaoyu/Rude")
                exit()
            except (Exception) as e:
                print(e)
                print("Exceptrion has occurred,please retry or get the newest version at:https://github.com/DengHaoyu/Rude")
                exit()
            try:
                dic = json.load(open("dosometing.json", 'r',encoding='utf-8'))
                ret = ret + dic['thing'][random.randint(0,len(dic['thing'])-1)]
            except (FileNotFoundError, FileExistsError):
                print("File dosomething.json is not founded,please get the newest verson "
                      "at:https://github.com/DengHaoyu/Rude")
                exit()
            except (Exception) as e:
                print(e)
                # print("Exceptrion has occurred,please retry or get the newest version
                # at:https://github.com/DengHaoyu/Rude")
                exit()
        return ret
class YourMather:
    #NOT SUPPORTED NOW
    def __init__(self,file):
        self.file = file
    def gen(self):
        return ""

print("输入生成句子数：")
num = int(input())
me = I()
for i in range(1,num+1):
    print(me.gen())