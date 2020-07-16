

# 模型转字段
def model_to_dict(result):
    from collections import Iterable
    # 转换完成后，删除  '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result]
            for t in tmp:
                t.pop('_sa_instance_state')
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')


# 统一返回标准
def success(data=[], message='请求成功', code=200):
    return {
        'message': message,
        'code': code,
        'data': data
    }


# 统一返回标准
def error(data=[], message='请求错误', code=500):
    return {
        'message': message,
        'code': code,
        'data': data
    }


# 统一返回标准
def fail(data=[], message='请求失败', code=-1):
    return {
        'message': message,
        'code': code,
        'data': data
    }
