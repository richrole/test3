# -*- coding: utf-8 -*-

from django.conf.urls import patterns

urlpatterns = patterns(
    'home_application.views',
    (r'^$', 'table'),
    (r'^tree/$', 'tree'),
    (r'^charts/$', 'charts'),
)

urlpatterns += patterns(
    'home_application.views',
    (r'^test/test_get_script_detail$', 'test_get_script_detail'),
    (r'^test/test_get_job_detail$', 'test_get_job_detail'),
    (r'^test/execute_script_by_id$', 'test_execute_script_by_id'),
    (r'^test/execute_script_by_content$', 'test_execute_script_by_content'),
    (r'^test/execute_job$', 'test_execute_job'),
    (r'^test/search_all_user', 'search_all_user'),
    (r'^test/search_biz_topo', 'search_biz_topo'),
    (r'^test/search_biz', 'search_biz'),
    (r'^test/search_set', 'search_set'),
    (r'^test/search_module', 'search_module'),
    (r'^test/search_host', 'search_host'),
)
