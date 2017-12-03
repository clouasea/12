#/usr/bin/env python
# -*- coding:utf-8 -*-
from django import  forms
from django.forms import widgets

class registform(forms.Form):
    username = forms.CharField(min_length=6,max_length=30,required=True,strip=True,
                               error_messages={'required':'不能为空',
                                               'min_length':'用户名最少为6个字符',
                                               'max_length':'用户名最大为30个字符'},)
    password = forms.CharField(required=True,min_length=6,max_length=20,strip=True,
                               widget=widgets.PasswordInput(attrs={'class':"form-control",'placeholder':"请输入密码"}),
                               error_messages={'required':"密码不能为空",
                                               'min_length':"密码最少6个字符",
                                               'max_length':"最大为20个字符"},)

    age = forms.CharField(required=False,strip=True,
                          widget=widgets.TextInput(attrs={'class':"form-control",'placeholder':"请输入你的年龄"}),
                          )
    city = forms.CharField(required=False,strip=True,
                           widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': "请输入你的城市"}),
                           )
    email = forms.EmailField(required=True,strip=True,
                             widget=widgets.TextInput(attrs={'class':"form-control",'placeholder':"请输入你的邮箱"}),
                             error_messages={'required':"邮箱不能为空",'invalid':"请输入正确的邮箱格式"},
                             )
    text = forms.Textarea(required=True,widget=widgets.TextInput(attrs={'placeholder':"请输入你的内容"},)
                          )


class loginform(forms.Form):
    username = forms.CharField(required=True,
                               strip=True,
                               min_length=6,
                               max_length=12,
                               widget=widgets.TextInput(attrs={'class':"form-control",'placeholder':'请输入用户名'}),
                               error_messages={'required':"用户名不能为空"},)
    pwd = forms.CharField(widgets.PasswordInput(attrs={'class':"form-control",'placeholder':'请输入密码'}),
                          required=True,
                          strip=True,
                          min_length=6,
                          max_length=12,
                          error_messages={'required':"密码不能为空"})


