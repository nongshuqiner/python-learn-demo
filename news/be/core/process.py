#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import ok
from core import rest
import json

import inspect
from config import PREFIX

async def process(app, name, request, url, method, oid=None):
    for i in PREFIX:
        if i in url:
            p = '_'.join(list(filter(None, PREFIX[i].split('/'))))
    
    bm = p + 'after' + name
    print(bm)

    if dir(app.process[bm]).count(method) == 1:
        #request = await getattr(app.process[p + 'before' + name], method)(request)
        #print(await getattr(app.process[p]['before'][name], method)({'a': 1}))
        #print(dir(app.process[bm]))
        #print(dir(app.pre_process.get(name)))
        #print(getattr(app.process.get(bm), method))
        #print(getattr(app.pre_process.get(name), method))
        #print(await getattr(app.pre_process.get(name), method)(request))
        pre = getattr(app.process.get(bm), method)
        #print(await pre(request))
        print(inspect.getsource(pre))
        # if not isinstance(request, dict):
        #     return request
    # 得到查询结果
    if oid == None:
        response = getattr(rest, method)(request, name)
    else:
        response = getattr(rest, method)(request, name, oid)
#     resBody = json.loads(response.body)
#     resStatus = response.status
#     # 根据返回结果判断是否需要后处理(错误状态就不处理了)
#     if resStatus == 200 and resBody['status'] == 0:
#         if dir(app.post_process.get(name)).count(method) == 1:
#             data = await getattr(app.post_process.get(name), method)(resBody['data'])
#             return ok(data)
#         else:
#             return response
#     else:
    return response

# async def process(app, name, request, method, oid=None):
#     # 对参数进行前处理
#     if dir(app.pre_process.get(name)).count(method) == 1:
#         request = await getattr(app.pre_process.get(name), method)(request)
#         # 如果返回的不是处理的字典参数，就直接return结果
#         if not isinstance(request, dict):
#             return request
#     # 得到查询结果
#     if oid == None:
#         response = getattr(rest, method)(request, name)
#     else:
#         response = getattr(rest, method)(request, name, oid)
#     resBody = json.loads(response.body)
#     resStatus = response.status
#     # 根据返回结果判断是否需要后处理(错误状态就不处理了)
#     if resStatus == 200 and resBody['status'] == 0:
#         if dir(app.post_process.get(name)).count(method) == 1:
#             data = await getattr(app.post_process.get(name), method)(resBody['data'])
#             return ok(data)
#         else:
#             return response
#     else:
#         return response


