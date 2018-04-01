# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
"""
实现在线翻译

"""
import json

if __name__ == "__main__":
    #对应上图的Request URL
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    #创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['i']='你好'
    Form_Data['from']='AUTO'
    Form_Data['to']='AUTO'
    Form_Data['smartresult']='dict'
    Form_Data['client']='fanyideskweb'
    Form_Data['salt']='1522550952455'
    Form_Data['sign']='13fcd8991503056244a7de7f53682746'
    Form_Data['doctype']='json'
    Form_Data['version']='2.1'
    Form_Data['keyfrom']='fanyi.web'
    Form_Data['action']='FY_BY_REALTIME'
    Form_Data['typoResult']='false'

    #使用urlencode方法转换标准格式
    def translate(what):
        Form_Data['i']=what
        try:
            dat = parse.urlencode(Form_Data)
        except:
           print('地址访问出错')
           return
           
        #传递Request对象和转换完格式的数据
        data=dat.encode('utf-8')
        response = request.urlopen(Request_URL,data)
        #读取信息并解码
        html = response.read().decode('utf-8')
        #使用JSON
        translate_results = json.loads(html)
        #找到翻译结果
        translate_results = translate_results['translateResult'][0][0]['tgt']
        #打印翻译信息
        print("翻译的结果是：%s" % translate_results)
    i=input('输入你要翻译内容:')
    while(i):
        translate(i)
        i=input('输入你要翻译内容:')
        
