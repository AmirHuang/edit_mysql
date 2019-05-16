# _*_ coding: utf-8 _*_
# @time     : 2019/05/16
# @Author   : Amir
# @Site     :
# @File     : 5_16_test_monihuaweidata.py
# @Software : PyCharm


from some_utils.MySQLDemo import MySQLDeMo

if __name__ == '__main__':
    m = MySQLDeMo(
        'localhost',
        3306,
        'root',
        '123456',
        'advmanager',
        'utf8'
    )

    # 去除某表中某几个字段的全部数据
    sql_alldata1 = 'SELECT machine_code, machine_soft_code,machine_area,machine_hotel FROM statement'
    alldatas1 = m.get_all(sql_alldata1)

    # 创建一个组的集合，得到多少个组
    groups1 = set()
    for onedata in alldatas1:
        groups1.add(onedata[1])

    # 创建一个字典  键为组名 值为组中对应的数据
    groups_dict1 = {}
    for item in groups1:
        groups_dict1[item] = set()

    # 添加数据
    for onedata in alldatas1:
        groups_dict1[onedata[1]].add(onedata[0])
    # print(groups_dict1)

    sql_alldata2 = 'SELECT machine_code, machine_soft_code,machine_area,machine_hotel FROM statement_copy'
    alldatas2 = m.get_all(sql_alldata2)
    groups2 = set()
    for onedata in alldatas2:
        groups2.add(onedata[1])

    groups_dict2 = {}
    for item in groups2:
        groups_dict2[item] = set()

    for onedata in alldatas2:
        groups_dict2[onedata[1]].add(onedata[0])

    # 对相同组-的集合  取差集
    cha_groupdata_dict = {}
    for key2 in groups_dict2.keys():
        if key2 in groups_dict1.keys():
            cha_groupdata_dict[key2] = groups_dict2[key2] ^ groups_dict1[key2]
        else:
            cha_groupdata_dict[key2] = groups_dict2[key2]

    # 空集合的键 的 list
    key_cha_list = []
    for key_cha in cha_groupdata_dict:
        if cha_groupdata_dict[key_cha] == set():
            key_cha_list.append(key_cha)
    print(key_cha_list)
    print(cha_groupdata_dict)

    # 差集中去掉空集合的字典
    for key_cha in key_cha_list:
        del cha_groupdata_dict[key_cha]
    print(cha_groupdata_dict)