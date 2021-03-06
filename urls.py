"""定义learning_logs的url模式"""

from django.conf.urls import  url

from . import views
app_name = 'learning_logs'
urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),

    #显示说有的主题

    url(r'^topics/$', views.topics,name='topics'),

    #特定主体的详细页
    url(r'^topics/(?P<topic_id>\d+)$', views.topic, name='topic'),

    #用户添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # url(r'^new_topic/$', views.new_topic, name='new_topic'),

    #用于添加新条目的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

]