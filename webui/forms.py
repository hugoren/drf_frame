# encoding: utf-8

"""
Definition of forms.
"""

from django import forms


class SearchLog(forms.Form):
    app = forms.CharField(max_length=255, widget=forms.TextInput({'class': 'form-control', 'placeholder': '应用系统名称'}))
    operater = forms.CharField(max_length=255, widget=forms.TextInput({'class': 'form-control', 'placeholder': '操作人'}))






