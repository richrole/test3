# -*- coding: utf-8 -*-
from django.http import JsonResponse


def SuccessResponse(data=None):
    """
    成功返回
    :param data:
    :return:
    """
    return JsonResponse(
        {
            'result': True,
            'message': 'success',
            'data': data
        }
    )


def ErrorResponse(message=None):
    """
    错误返回
    :param message:
    :return:
    """
    return JsonResponse(
        {
            'result': False,
            'message': message,
            'data': None
        }
    )
