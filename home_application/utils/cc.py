# -*- coding: utf-8 -*-
import json

import requests

from blueking.component.shortcuts import get_client_by_request
from conf.default import BK_PAAS_HOST, APP_ID, APP_TOKEN


def login_search_users(request):
    """
    查询蓝鲸用户列表
    """
    url = BK_PAAS_HOST + '/api/c/compapi/v2/bk_login/get_all_users/'

    #region 请求json数据
    content = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
    }

    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.bk_login.get_all_users()
    return result


def cc_search_biz(request):
    """
    查询业务
    """
    url = BK_PAAS_HOST + '/api/c/compapi/v2/cc/search_business/'

    #region 请求json数据
    content = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
        "bk_supplier_id": 0,
        "fields": [
            "bk_biz_id",
            "bk_biz_name"
        ],
        "page": {
            "start": 0,
            "limit": 100,
            "sort":  ""
        }
    }

    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.cc.search_business(content)
    return result


def cc_search_host(biz_id, set_id, ip_list, request):
    '''
    查询主机
    :param biz_id: 业务ID，int
    :param set_id: 集群ID，int
    :param ips: 过滤ip
    :return: 查询主机结果
    '''
    url = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_host/"

    # region  请求json数据
    content = {
            "bk_app_code": APP_ID,
            "bk_app_secret": APP_TOKEN,
            "bk_username": request.user.username,
            "bk_biz_id": int(biz_id),
            "ip": {
                "data": ip_list,                         # ip数组
                "exact": 1,                              # 是否根据精确搜索，1为精确搜索，0为模糊搜索
                "flag": "bk_host_innerip|bk_host_outerip"
            },
            "condition": [
                {
                    "bk_obj_id": "host",
                    "fields": [],
                    "condition": [
                        # {
                            # "field": "",                 # 根据主机字段查询主机
                            # "operator": "",              # 操作符, $eq为相等，$neq为不等，$in为属于，$nin为不属于
                            # "value": ""                  # 字段对应的值
                        # }
                    ]
                },
                {
                    "bk_obj_id": "biz",
                    "fields": ['bk_biz_id', 'bk_biz_name'],
                    "condition": []
                }
            ],
            "page": {
                "start": 0,
                "limit": 10,
                "sort": "bk_host_id"
            },
            "pattern": ""
        }
    if set_id != 0:
        content['condition'].append(
            {
                "bk_obj_id": "set",  # 根据主机所属集合查询主机
                "fields": ["bk_set_id", "bk_set_name"],
                "condition": [
                    {
                        "field": "bk_set_id",           # 根据集群id查询主机
                        "operator": "$eq",              # 操作符, $eq为相等，$neq为不等，$in为属于，$nin为不属于
                        "value": int(set_id)            # 集群id
                    }
                ]
            })

    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.cc.search_host(content)

    return result


def cc_search_set(biz_id, request):
    '''
    查询集群
    :param biz_id: 业务ID，int
    :return: 查询集群结果
    '''
    url = BK_PAAS_HOST + '/api/c/compapi/v2/cc/search_set/'
    content = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_token": "",
        "bk_username": request.user.username,
        "bk_biz_id": int(biz_id),
        "fields": [
            "bk_set_id", "bk_set_name"
        ],
        "condition": {},
        "page": {
            "start": 0,
            "limit": 100,
            "sort": "bk_set_name"
        }

    }
    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.cc.search_set(content)
    return result


def cc_search_module(biz_id, set_id, request):
    '''
    查询模块
    :param biz_id: 业务ID，int
    :param set_id: 集群ID，int
    :return: 查询模块结果
    '''
    url = BK_PAAS_HOST + '/api/c/compapi/v2/cc/search_module/'
    content = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_token": "",
        "bk_username": request.user.username,
        "bk_biz_id": int(biz_id),
        "bk_set_id": int(set_id),
        "fields": [
            "bk_module_id", "bk_module_name"
        ],
        "condition": {},
        "page": {
            "start": 0,
            "limit": 100,
            "sort": "bk_module_name"
        }

    }
    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.cc.search_module(content)
    return result


def cc_search_biz_topo(biz_id, request):
    """
    查询业务拓扑
    :param biz_id: 业务ID，int
    :return: 查询业务拓扑结果
    """
    url = BK_PAAS_HOST + '/api/c/compapi/v2/cc/search_biz_inst_topo/'

    #region 请求json数据
    content = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
        "bk_supplier_id": 0,
        "bk_biz_id": int(biz_id)
    }

    # 掉API网关的方法，要加入白名单
    response = requests.post(url, json.dumps(content), verify=False)
    result = json.loads(response.content)

    # 调APP开发框架中的SDK包的方法，不需要加入白名单
    # client = get_client_by_request(request)
    # result = client.cc.search_biz_inst_topo(content)
    return result
