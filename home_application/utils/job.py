# -*- coding: utf-8 -*-
import base64
import time

from blueking.component.shortcuts import get_client_by_request


def execute_script_by_id(request, bk_biz_id, script_id, ip_list, script_param=''):
    """
    快速执行作业平台给定ID的脚本
    :param script_param: string 脚本参数(非必填)
    :param ip_list: array 执行脚本的服务器列表,格式为:[{"bk_cloud_id": x, "ip": x.x.x.x}...]
    :param script_id: int 要执行的作业平台上的脚本的ID
    :param bk_biz_id: int 执行脚本的服务器所属业务ID
    :param request: http请求
    :return: 执行成功时返回脚本执行结果。失败时抛出一个异常。
    """
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": bk_biz_id,
        "script_id": script_id,
        "script_param": base64.b64encode(script_param),
        "account": "root",
        "ip_list": ip_list,
        "script_timeout": 1000,
    }
    res = client.job.fast_execute_script(params)
    if res['result']:
        # 默认返回脚本执行结果，若获取出错可将下行代码改成 return res['data']['job_instance_id']来返回执行ID后再手动查询执行结果。
        return get_job_instance_log(request, bk_biz_id, res['data']['job_instance_id'])
    else:
        raise Exception(u'执行脚本失败: {}'.format(res['message']))


def execute_script_by_content(request, bk_biz_id, script_content, ip_list, script_param=''):
    """
    快速执行给定内容的脚本
    :param script_param: string 脚本参数
    :param ip_list: array 执行脚本的服务器列表,格式为:[{"bk_cloud_id": x, "ip": x.x.x.x}...]
    :param script_content: string 要执行的脚本内容字符串
    :param request: http请求
    :param bk_biz_id: int 执行脚本的服务器所属业务ID
    :return: 执行成功时返回脚本执行结果。失败时抛出一个异常。
    """
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": bk_biz_id,
        "script_content": base64.b64encode(script_content),
        "script_param": base64.b64encode(script_param),
        "account": "root",
        "ip_list": ip_list,
        "script_timeout": 1000,
    }
    res = client.job.fast_execute_script(params)
    if res['result']:
        # 默认返回脚本执行结果，若获取出错可将下行代码改成 return res['data']['job_instance_id']来返回执行ID后再手动查询执行结果。
        return get_job_instance_log(request, bk_biz_id, res['data']['job_instance_id'])
    else:
        raise Exception(u'执行脚本失败: {}'.format(res['message']))


def get_job_detail(request, bk_biz_id, bk_job_id):
    """
    获取作业模板信息
    :param request: http请求
    :param bk_biz_id: int 作业模板所属业务ID
    :param bk_job_id: int 作业模板ID
    :return: 返回示例
    {
        "message": "success",
        "code": 0,
        "data": {
            "bk_biz_id": 2,
            "name": "测试作业",
            "creator": "admin",
            "tag_id": "1",
            "last_modify_time": "2019-10-28 16:13:50 +0800",
            "global_vars": [
                {
                    "category": 3,
                    "description": "",
                    "type": 2,
                    "id": 24,
                    "name": "id-2019102816333875"
                }
            ],
            "bk_job_id": 1016,
            "create_time": "2019-10-28 15:20:44 +0800",
            "steps": [
                {
                    "account": "root",
                    "pause": 0,
                    "is_param_sensitive": 0,
                    "creator": "admin",
                    "script_timeout": 1000,
                    "last_modify_user": "admin",
                    "block_order": 1,
                    "name": "step1",
                    "script_content": "#!/bin/bash\necho '无参数步骤测试'\n\n\n\n",
                    "block_name": "无参数",
                    "create_time": "2019-10-28 15:20:44 +0800",
                    "last_modify_time": "2019-10-28 16:13:50 +0800",
                    "ip_list": [
                        {
                            "ip": "192.168.240.43",
                            "bk_cloud_id": 0
                        },
                        {
                            "ip": "192.168.240.44",
                            "bk_cloud_id": 0
                        }
                    ],
                    "step_id": 1032,
                    "script_id": 1094,
                    "script_param": "",
                    "type": 1,
                    "order": 1,
                    "script_type": 1
                },
                {
                    "account": "root",
                    "pause": 0,
                    "is_param_sensitive": 0,
                    "creator": "admin",
                    "script_timeout": 1000,
                    "last_modify_user": "admin",
                    "block_order": 2,
                    "name": "step2",
                    "script_content": "#!/bin/bash\necho \"参数1: $1, 参数2: $2\"\n\n\n\n",
                    "block_name": "有参数",
                    "create_time": "2019-10-28 15:20:44 +0800",
                    "last_modify_time": "2019-10-28 16:13:50 +0800",
                    "ip_list": [
                        {
                            "ip": "192.168.240.43",
                            "bk_cloud_id": 0
                        },
                        {
                            "ip": "192.168.240.44",
                            "bk_cloud_id": 0
                        }
                    ],
                    "step_id": 1033,
                    "script_id": 1095,
                    "script_param": "",
                    "type": 1,
                    "order": 2,
                    "script_type": 1
                }
            ],
            "last_modify_user": "admin",
            "step_num": 2
        },
        "result": true,
        "request_id": "75222dbac700446faab0aa2542be4479"
    }
    """
    client = get_client_by_request(request)
    params = {
        'bk_biz_id': bk_biz_id,
        'bk_job_id': bk_job_id
    }
    res = client.job.get_job_detail(params)
    return res


def get_script_detail(request, bk_biz_id, script_id):
    """
    获取脚本详情
    :param request:
    :param bk_biz_id:
    :param script_id:
    :return:
    """
    client = get_client_by_request(request)
    params = {
        'bk_biz_id': bk_biz_id,
        'id': script_id
    }
    res = client.job.get_script_detail(params)
    return res


def execute_job(request, bk_biz_id, bk_job_id, steps):
    """
    执行不带全局变量的作业
    :param request: http请求
    :param bk_biz_id: int 要执行作业的服务器所属业务ID
    :param bk_job_id: int 要执行的作业的ID
    :param steps: array 作业步骤参数,示例如下:
    执行的作业为上面的get_job_detail接口返回示例的作业
    该作业有两个步骤，第一个步骤不需要参数，第二个步骤需要两个参数，两个步骤都已经预先指定了在两台服务器上执行。
    "steps": [
        {
        	"step_id": 1032 // 执行第一个步骤(不传该参数将不会执行第一个步骤)，没有其它参数代表第一个步骤将会在预先指定的两台服务器上执行，如果作业没有预先指定服务器则需要传入ip_list参数。
        },
        {
        	"step_id": 1033, // 执行第二个步骤
            "ip_list": [ // 有ip_list参数，代表将不会在预先指定的两台服务器上执行，而是会在下面的两台服务器上执行。
                {   // 服务器1
                    "bk_cloud_id": 0,
                    "ip": "192.168.240.51"
                },
                {   // 服务器2
                    "bk_cloud_id": 0,
                    "ip": "192.168.240.52"
                }
            ],
            "script_param": "参数1 参数2" // 此处传入了步骤2要执行的脚本的两个参数，参数间以空格分隔。
        }
    ]
    :return: 执行成功时返回作业执行结果。失败时抛出一个异常。
    """
    client = get_client_by_request(request)
    s = map(handle_steps, steps)
    params = {
        "bk_biz_id": bk_biz_id,
        "bk_job_id": bk_job_id,
        "steps": s
    }
    res = client.job.execute_job(params)
    if res['result']:
        # 默认返回脚本执行结果，若获取出错可将下行代码改成 return res['data']['job_instance_id']来返回执行ID后再手动查询执行结果。
        return get_job_instance_log(request, bk_biz_id, res['data']['job_instance_id'])
    else:
        raise Exception(u'执行脚本失败: {}'.format(res['message']))


def get_job_instance_log(request, bk_biz_id, job_instance_id):
    """
    获取作业(脚本)执行结果
    :param request: http请求
    :param bk_biz_id: 作业所属业务ID
    :param job_instance_id: 执行作业(脚本)作业实例ID
    :return: 成功时返回执行完毕的结果，失败时抛出异常。
    返回示例:
{
    "message": "success",
    "code": 0,
    "data": [
        {
            "status": 3,
            "step_results": [
                {
                    "tag": "",
                    "ip_logs": [
                        {
                            "total_time": 0.129,
                            "ip": "192.168.240.43",
                            "start_time": "1970-01-01 08:00:00 +0800",
                            "log_content": "[2019-10-28 16:00:31][PID:22014] job_start\n无参数步骤测试\n",
                            "exit_code": 0,
                            "bk_cloud_id": 0,
                            "retry_count": 0,
                            "end_time": "1970-01-01 08:00:00 +0800",
                            "error_code": 0
                        },
                        {
                            "total_time": 0.123,
                            "ip": "192.168.240.44",
                            "start_time": "1970-01-01 08:00:00 +0800",
                            "log_content": "[2019-10-28 16:00:31][PID:65565] job_start\n无参数步骤测试\n",
                            "exit_code": 0,
                            "bk_cloud_id": 0,
                            "retry_count": 0,
                            "end_time": "1970-01-01 08:00:00 +0800",
                            "error_code": 0
                        }
                    ],
                    "ip_status": 9
                }
            ],
            "is_finished": true,
            "step_instance_id": 1091406,
            "name": "step1"
        },
        {
            "status": 3,
            "step_results": [
                {
                    "tag": "",
                    "ip_logs": [
                        {
                            "total_time": 0.123,
                            "ip": "192.168.240.51",
                            "start_time": "1970-01-01 08:00:00 +0800",
                            "log_content": "[2019-10-28 16:00:32][PID:61674] job_start\n参数1: xike, 参数2: 123\n",
                            "exit_code": 0,
                            "bk_cloud_id": 0,
                            "retry_count": 0,
                            "end_time": "1970-01-01 08:00:00 +0800",
                            "error_code": 0
                        },
                        {
                            "total_time": 0.19,
                            "ip": "192.168.240.52",
                            "start_time": "1970-01-01 08:00:00 +0800",
                            "log_content": "[2019-10-28 16:00:33][PID:94162] job_start\n参数1: xike, 参数2: 123\n",
                            "exit_code": 0,
                            "bk_cloud_id": 0,
                            "retry_count": 0,
                            "end_time": "1970-01-01 08:00:00 +0800",
                            "error_code": 0
                        }
                    ],
                    "ip_status": 9
                }
            ],
            "is_finished": true,
            "step_instance_id": 1091407,
            "name": "step2"
        }
    ],
    "result": true,
    "request_id": "4e0bf025b71f45a8bd707adac2953b8a"
}
    """
    client = get_client_by_request(request)
    params = {
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_instance_id,
    }
    flag = 10
    while flag > 0:
        res = client.job.get_job_instance_log(params)
        if res['result']:
            unfinished_steps = filter(lambda x: not x['is_finished'], res['data'])
            if len(unfinished_steps) > 0:
                time.sleep(2)
                flag -= 1
            else:
                return res
        else:
            raise Exception(u'获取脚本结果失败: {}'.format(res['message']))
    raise Exception(u'获取脚本结果时超出接口设定的最大重试次数，请手动获取脚本执行结果')


def handle_steps(step):
    """
    转换steps中的参数
    :param step:
    :return:
    """
    if 'script_param' in step:
        step['script_param'] = base64.b64encode(step['script_param'])
    return step