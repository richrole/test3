# -*- coding: utf-8 -*-
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from common.mymako import render_mako_context
from home_application.utils.cc import login_search_users, cc_search_biz, cc_search_set, cc_search_biz_topo, \
    cc_search_host, cc_search_module
from home_application.utils.job import (execute_script_by_id, execute_script_by_content, execute_job, get_job_detail,
                                        get_script_detail)
from home_application.utils.response import ErrorResponse, SuccessResponse


def table(request):
    """
    表格页面
    """
    return render_mako_context(request, '/home_application/table.html')


def tree(request):
    """
    树形页面
    """
    return render_mako_context(request, '/home_application/tree.html')


def charts(request):
    """
    图表页面
    """
    return render_mako_context(request, '/home_application/charts.html')


@csrf_exempt
def test_get_job_detail(request):
    """
    测试获取作业模板详情
    :param request:
    示例参数:
{
  "bk_biz_id": 2,
  "bk_job_id": 1016
}
    :return:
    """
    payload = json.loads(request.body)
    try:
        res = get_job_detail(
            request, payload['bk_biz_id'],
            payload['bk_job_id']
        )
        return SuccessResponse(res['data'])
    except Exception as e:
        return ErrorResponse(e.message)


@csrf_exempt
def test_get_script_detail(request):
    """
    测试获取脚本详情
    :param request:
    示例参数:
{
  "bk_biz_id": 2,
  "id": 1091
}
    :return:
    """
    payload = json.loads(request.body)
    try:
        res = get_script_detail(
            request, payload['bk_biz_id'],
            payload['id']
        )
        return SuccessResponse(res['data'])
    except Exception as e:
        return ErrorResponse(e.message)


@csrf_exempt
def test_execute_script_by_id(request):
    """
    测试执行指定脚本
    :param request:
    示例参数:
{
  "bk_biz_id": 2,
  "script_id": 1091,
  "script_param": "zhang san",
  "ip_list": [
        {
            "bk_cloud_id": 0,
            "ip": "192.168.240.43"
        }
  ]
}
    :return:
    """
    payload = json.loads(request.body)
    try:
        res = execute_script_by_id(
            request, payload['bk_biz_id'],
            payload['script_id'],
            payload['ip_list'],
            script_param=payload.get('script_param')
        )
        return SuccessResponse(res['data'])
    except Exception as e:
        return ErrorResponse(e.message)


@csrf_exempt
def test_execute_script_by_content(request):
    """
    测试执行给定内容的脚本
    :param request:
    参数示例:
{
  "bk_biz_id": 2,
  "script_content": "echo \"first name:$1 second name:$2\"",
  "script_param": "zhang san",
  "ip_list": [
        {
            "bk_cloud_id": 0,
            "ip": "192.168.240.43"
        }
  ]
}
    :return:
    """
    payload = json.loads(request.body)
    try:
        res = execute_script_by_content(
            request,
            payload['bk_biz_id'],
            payload['script_content'],
            payload['ip_list'],
            script_param=payload.get('script_param')
        )
        return SuccessResponse(res['data'])
    except Exception as e:
        return ErrorResponse(e.message)


@csrf_exempt
def test_execute_job(request):
    """
    测试执行作业
    :param request:
    参数示例:
{
  "bk_biz_id": 2,
  "bk_job_id": 1016,
  "steps": [
        {
        	"step_id": 1032
        },
        {
        	"step_id": 1033,
            "ip_list": [
                {
                    "bk_cloud_id": 0,
                    "ip": "192.168.240.51"
                },
                {
                    "bk_cloud_id": 0,
                    "ip": "192.168.240.52"
                }
            ],
            "script_param": "zhang san"
        }
    ]
}
    :return:
    """
    payload = json.loads(request.body)
    try:
        res = execute_job(
            request,
            payload['bk_biz_id'],
            payload['bk_job_id'],
            payload['steps']
        )
        return SuccessResponse(res['data'])
    except Exception as e:
        return ErrorResponse(e.message)


# 查蓝鲸用户
def search_all_user(request):
    try:
        data = login_search_users(request)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


# 查业务
def search_biz(request):
    try:
        data = cc_search_biz(request)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


# 查集群
def search_set(request):
    """
    传递参数
    :param 业务id   biz_id
    :param request:
    :return:
    """
    try:
        biz_id = request.GET.get('biz_id')
        data = cc_search_set(biz_id, request)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


# 查模块
def search_module(request):
    """
    传递参数
    :param 业务id   biz_id
    :param 集群id   set_id
    :param request:
    :return:
    """
    try:
        biz_id = request.GET.get('biz_id')
        set_id = request.GET.get('set_id')
        data = cc_search_module(biz_id, set_id, request)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


# 查业务拓扑
def search_biz_topo(request):
    """
    传递参数
    :param 业务id   biz_id
    :param request:
    :return:
    """
    try:
        biz_id = request.GET.get('biz_id')
        data = cc_search_biz_topo(biz_id, request)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


# 查主机
def search_host(request):
    """
    :param request:
    传递参数
    :param 业务id   biz_id,
    biz_id,ip_list = ['10.92.190.214','10.92.190.215']
    get请求获取的ip_list，转换成列表，请调用get_host_ip_list
    :return:
    """
    try:
        biz_id = request.GET.get('biz_id')
        ip_list = []
        set_id = 0
        if 'set_id' in request.GET:
            set_id = request.GET.get('set_id')
        if 'ip' in request.GET:
            ip = request.GET.get('ip')
            ip_list = get_host_ip_list(ip)
        res = cc_search_host(biz_id, set_id, ip_list, request)

        count = res['data']['count']
        host_data = []
        for item in res['data']['info']:
            # 根据需求返回给前端的字段
            data = {
                'bk_host_innerip': item['host']['bk_host_innerip'],
                'bk_os_name': item['host']['bk_os_name'],
                'bk_host_name': item['host']['bk_host_name'],
                'area': item['host']['bk_cloud_id'][0]['bk_inst_name'],
                'bk_cloud_id': item['host']['bk_cloud_id'][0]['bk_inst_id'],
                'bk_os_type': item['host']['bk_os_type'],
                'bk_biz_id': item['biz'][0]['bk_biz_id'],
                'bk_biz_name': item['biz'][0]['bk_biz_name']
            }
            host_data.append(data)

        return JsonResponse({'data': {'count': count, 'info': host_data}, 'result': True})
    except Exception as e:
        return JsonResponse({'result': False, 'message': repr(e), 'data': None})


def get_host_ip_list(ip):
    ip_list = ip.split(',')
    return ip_list
