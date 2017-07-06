# -*- coding: utf-8 -*-

'''
  Ping++ Server SDK 说明：
  以下代码只是为了方便商户测试而提供的样例代码，商户可根据自己网站需求按照技术文档编写, 并非一定要使用该代码。
  接入查询流程参考开发者中心：https://www.pingxx.com/docs/server/charge ，文档可筛选后端语言和接入渠道。
  该代码仅供学习和研究 Ping++ SDK 使用，仅供参考。
'''
import pingpp

# api_key 获取方式：登录 [Dashboard](https://dashboard.pingxx.com)->点击管理平台右上角公司名称->开发信息-> Secret Key
pingpp.api_key = 'sk_test_Gm58iH4O4yzDvbrbHOyX5WrH'
# 通过 Charge 对象的 id 查询一个已创建的 Charge 对象
ch = pingpp.Charge.retrieve('app_rb9iz9WTCGWDjD8S')
print(ch)  # 输出 Ping++ 返回 Charge 对象
