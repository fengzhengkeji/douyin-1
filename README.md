简介：

抖音设备注册， 阅读，点赞，日志上报加密/解密。
版本：3.6.0 或更新都可以

抖音机器人/爬虫必备， 服务器提供加解密服务，仅供学习，如有需求请联系ciscowu1990@gmail.com。



#douyin_client.py

  抖音加密算法接口
  
  适用于抖音设备注册：/service/2/device_register/
  
  反作弊日志接口： /service/2/app_log/
  
##抖音解密算法接口：

    把密加密的数据通过base64编码提交，可得到解密数据，帮助分析各字段含义
    
    ciphetext = base64.encdode(加密数据)
    
    decurl = "http://133.130.98.90/douyin/decrypt"，
    
    r = requests.post(decurl, data=ciphetext)
    
    
##抖音加密算法接口

    把数据通过base64编码提交， 返回加密结果
    
    r = requests.post(encurl, data= base64.b64encode(r.content))
    
    print(u"加密结果:")
    
    print(r.text)
