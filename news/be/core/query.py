#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
from core.tool import isInt
from db import model
from config import PAGESIZE

session = model.DBSession()

# 将数据库查询数据变成字典型方法
def getDict(obj):
    d = {}
    for column in obj.__table__.columns:
        d[column.name] = getattr(obj, column.name)
    return d

# 根据字符串判断数据库是否包含该表
def hasClass(className):
    try:
        getattr(model, className)
        return True
    except Exception as e:
        return False

# 传入模型，获得该模型字段字典并赋空值，排除id和time，用于post方法
def getFieldDict(Obj):
    res = {}
    for i in dir(Obj):
        if i[0] != '_' and i != 'id' and i != 'time':
            res[i] = ''
    return res

# 传入模型，获得该模型字段列表, 用于 ls 方法
def getFieldList(Obj):
    res = []
    for i in dir(Obj):
        if i[0] != '_':
            res.append(i)
    return res

# 查询列表方法
def ls(className, request):
    if not hasClass(className):
        return 404
    try:
        # 从请求参数中获取非标准参数
        args = {}
        for i in request:
            i = i.lower()
            if not i in ['page', 'pagesize', 'sort']:
                args[i] = request[i]

        # 获得模型，以及支持的字段数组列表
        classModel = getattr(model, className)
        modelList = getFieldList(classModel)

        # 开始查询数据
        res = session.query(classModel)

        # 处理各种非标准参数查询
        for i in args:
            # 支持一个条件带多个参数，用英文逗号分割
            argVal = args[i].split(',')
            arg = i.split('-')
            argField = arg[0]
            argMethod = None if len(arg) == 1 else arg[1]
            field = getattr(classModel, argField)
            # 检查字段是否是模型支持的
            if not argField in modelList:
                return 400
            # 处理特殊查询条件
            if argMethod:
                # 模糊查询
                if argMethod == 'like':
                    for val in argVal:
                        res = res.filter(field.like('%' + val + '%'))
                # 不等于查询
                elif argMethod == 'neq':
                    for val in argVal:
                        res = res.filter(field != val)
                # in List 查询
                elif argMethod == 'in':
                    res = res.filter(field.in_(argVal))
                # not in List 查询
                elif argMethod == 'nin':
                    res = res.filter(~field.in_(argVal))
                # 其他不支持关键词返回参数错误
                else:
                    return 400
            # 处理普通相等查询条件
            else:
                for val in argVal:
                    res = res.filter(field == val)

        # 获取排序参数
        sort = 'id' if not 'sort' in request else request['sort']

        # 支持多重条件排序，用英文逗号分隔
        sortArr = sort.split(',')
        for i in sortArr:
            ## 根据排序参数第一个字符是否是中划线确定是正序还是倒序，为假倒序
            field = getattr(classModel, sortField)
            sortType = i[0] == '-'
            sortField = i[1:] if sortType else i
            if not sortField in modelList:
                return 400
            if sortType:
                res = res.order_by(field)
            else:
                res = res.order_by(field.desc())

        # 统计总条数
        total = res.count()

        # 获取分页序号参数
        page = 0 if not 'page' in request else request['page']
        if not isInt(page):
            return 400
        else:
            page = int(page)

        # 获取分页每页数量参数
        pagesize = PAGESIZE if not 'pagesize' in request else request['pagesize']
        if not isInt(pagesize):
            return 400
        else:
            pagesize = int(pagesize)

        # 处理分页和分页需要查询
        res = res.limit(pagesize).offset(page * pagesize)

        # 将结果整理成列表输出
        arr = []
        if res:
            for i in res:
                arr.append(getDict(i))
        return {'list': arr, 'total': total}

    except Exception as e:
        return 503

# 添加新数据方法
def post(className, Data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        modelDict = getFieldDict(classModel)
        for i in Data:
            if i in modelDict:
                modelDict[i] = Data[i]
            else:
                return 400

        newData = classModel(**modelDict)
        session.add(newData)
        session.commit()
        return 200
    except Exception as e:
        return 503

# 查询单挑数据方法
def get(className, oid):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        if oid == 'first':
            res = res.first()
            if res == None:
                return 4043
            else:
                return getDict(res)
        else:
            res = res.filter_by(id=oid)
            try:
                res = res.one()
                return getDict(res)
            except Exception as e:
                return 4042

    except Exception as e:
        return 503

# 修改单挑数据方法
def put(className, oid, data):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel)
        if oid == 'first':
            res = res.first()
            if res == None:
                return 4043
            else:
                return 200
        else:
            res = res.get(oid)
            if res:
                oldData = getDict(res)
                for i in data:
                    if i not in oldData:
                        return 400
                    setattr(res, i, data[i])

                session.add(res)
                session.commit()
                return 200
            else:
                return 4042
    except Exception as e:
        return 503

# 删除单挑数据方法
def delete(className, oid):
    if not hasClass(className):
        return 404
    try:
        classModel = getattr(model, className)
        res = session.query(classModel).get(oid)
        if res:
            session.delete(res)
            session.commit()
            return 200
        else:
            return 400
    except Exception as e:
        return 503
