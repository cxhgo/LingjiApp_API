import re
import json
def changeheader(headers):
    """
         对头信息中有特殊符号传输解析会出问题的进行编码再返回
         :param header:接口的请求头信息
         :return sub_Authorizations: 进行编码后的请求头信息
    """
    # 找到需要重新编码的字符串内容：Authorization对应的值，以列表形式存储
    Authorization = re.findall(r'Authorization":"(.*?)","Connection"',headers)
    # 进行内容编码
    Authorizations=json.dumps(Authorization[0])
    # 替换原有headers中Authorization对应的值
    re_Authorization='"'+Authorization[0]+'"'
    sub_Authorizations = headers.replace(re_Authorization,Authorizations)
    # print(' Authorization:', re_Authorization)
    # print(' Authorizations:', Authorizations)
    # print('替换后的sub_Authorizations', sub_Authorizations)
    return sub_Authorizations