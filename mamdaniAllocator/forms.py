from django import forms
import datetime


class MonitorForm(forms.Form):
    cpu = forms.CharField(initial='', required=False)
    ram = forms.CharField(initial='', required=False)
    disk= forms.CharField(initial='', required=False)
