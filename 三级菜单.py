menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

current_layer = menu  #给各层字典的key值赋一个变量
layer_record = [ ]    #用于存储上一级菜单记录
while True:
    for i in current_layer:   #进入之后打印这一级字典的key值
        print(i)
    choice = input('>>>').strip()
    if choice in current_layer:
        layer_record.append(current_layer)    #这级字典保存在layer_record中作为“b”的返回记录
        current_layer = current_layer[choice]  # 把即将进入的子菜单赋值给current_layer动态变量,去进行下一轮循环
    elif choice == 'b':
        if len(layer_record) != 0:
           current_layer = layer_record.pop()  #把layer_record中保存的上一级菜单取出来
        else:
           print('当前已是第一级菜单 ')
    elif choice == 'q':
        exit('bye')