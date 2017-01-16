from django.shortcuts import render, render_to_response
from django import http as django_http
from .models import Ramusage, CPUusage, Diskusage, cpuset, ramset, diskset, outputset, outputfunction
from .forms import MonitorForm
from .flc import ruletable
# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
import json
from chartit import DataPool, Chart

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def monitor(request):
    from_d = ""
    to_d = ""
    if request.method == "POST":

        form = MonitorForm(request.POST)
        print form.errors

        if form.is_valid():
            cpu = int(form.cleaned_data['cpu'])
            ram = int(form.cleaned_data['ram'])
            disk = int(form.cleaned_data['disk'])
            ruletable(cpu, ram, disk)
            return django_http.HttpResponseRedirect('/mamdaniAllocator/result')
    else:
        form = MonitorForm()

    return render(request, 'monitor.html', {'form': form})
def result(request):
    print "result amca"
    return render(request, 'result.html')
def ramfunction(request):
    queryset = Ramusage.objects.all().values('usage', 'SMALL', 'MEDIUM', 'LARGE')
    print queryset, "dayi"
    ramdata = \
        DataPool(
            series=
            [{'options': {
                'source': queryset},
                'terms': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE',
                    'usage']}
            ])
    cht = Chart(
        datasource=ramdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'usage': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE'
                ]
            }}],
        chart_options=
        {'title': {
            'text': 'Ram membership Funcion'},
            'xAxis': {
                'title': {
                    'text': 'RAM'
                }
            }
        }
    )
    return render_to_response('load_chart.html', {'staticchart': cht})
def Outputfunction(request):
    queryset = outputfunction.objects.all().values('server_index', 'EMPTY', 'ALMOSTEMPTY', 'MEDIUM', 'ALMOSTFULL', 'FULL')
    print queryset, "dayi"
    ramdata = \
        DataPool(
            series=
            [{'options': {
                'source': queryset},
                'terms': [
                    'server_index',
                    'EMPTY',
                    'ALMOSTEMPTY',
                    'MEDIUM',
                    'ALMOSTFULL',
                    'FULL']}
            ])
    cht = Chart(
        datasource=ramdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'server_index': [
                    'EMPTY',
                    'ALMOSTEMPTY',
                    'MEDIUM',
                    'ALMOSTFULL',
                    'FULL'
                ]
            }}],
        chart_options=
        {'title': {
            'text': 'Output Funcion'},
            'xAxis': {
                'title': {
                    'text': 'Server Index Variable'
                }
            }
        }
    )
    return render_to_response('load_CPU_chart.html', {'staticchart': cht})
def cpufunction(request):
    queryset = CPUusage.objects.all().values('usage', 'SMALL', 'MEDIUM', 'LARGE')
    print queryset, "dayi"
    ramdata = \
        DataPool(
            series=
            [{'options': {
                'source': queryset},
                'terms': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE',
                    'usage']}
            ])
    cht = Chart(
        datasource=ramdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'usage': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE'
                ]
            }}],
        chart_options=
        {'title': {
            'text': 'CPU membership Funcion'},
            'xAxis': {
                'title': {
                    'text': 'CPU'
                }
            }
        }
    )
    return render_to_response('load_CPU_chart.html', {'staticchart': cht})

def diskfunction(request):
    queryset = Diskusage.objects.all().values('usage', 'SMALL', 'MEDIUM', 'LARGE')
    print queryset, "dayi"
    ramdata = \
        DataPool(
            series=
            [{'options': {
                'source': queryset},
                'terms': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE',
                    'usage']}
            ])
    cht = Chart(
        datasource=ramdata,
        series_options=
        [{'options': {
            'type': 'line',
            'stacking': False},
            'terms': {
                'usage': [
                    'SMALL',
                    'MEDIUM',
                    'LARGE'
                ]
            }}],
        chart_options=
        {'title': {
            'text': 'Disc membership Funcion'},
            'xAxis': {
                'title': {
                    'text': 'Disc Space'
                }
            }
        }
    )
    return render_to_response('load_disk_chart.html', {'staticchart': cht})

def Cpuset(request):
    set = cpuset.objects.all().values('id', 'SMALL', 'MEDIUM', 'LARGE')
    print list(set)
    ds = DataPool(
        series=
        [{'options': {
            'source':set},
            'terms': [
                'id',
                'SMALL',
                'MEDIUM',
                'LARGE']}
        ])

    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': True,
            'stack': 0},
            'terms': {
                'id':[
                'SMALL',{'MEDIUM': { 'stack': 1}}, {'LARGE': {'stack': 2}},

                    ]
            }}],
        chart_options=
        {'title': {
            'text': 'cpu set'}})
    return render_to_response('load_cpuset_chart.html', {'staticchart': cht})
def Ramset(request):
    set = ramset.objects.all().values('id', 'SMALL', 'MEDIUM', 'LARGE')
    print list(set)
    ds = DataPool(
        series=
        [{'options': {
            'source':set},
            'terms': [
                'id',
                'SMALL',
                'MEDIUM',
                'LARGE']}
        ])

    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': True,
            'stack': 0},
            'terms': {
                'id':[
                'SMALL',{'MEDIUM': { 'stack': 1}}, {'LARGE': {'stack': 2}},

                    ]
            }}],
        chart_options=
        {'title': {
            'text': 'ram set'}})
    return render_to_response('load_cpuset_chart.html', {'staticchart': cht})
def Diskset(request):
    set = diskset.objects.all().values('id', 'SMALL', 'MEDIUM', 'LARGE')
    print list(set)
    ds = DataPool(
        series=
        [{'options': {
            'source':set},
            'terms': [
                'id',
                'SMALL',
                'MEDIUM',
                'LARGE']}
        ])

    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': True,
            'stack': 0},
            'terms': {
                'id':[
                'SMALL',{'MEDIUM': { 'stack': 1}}, {'LARGE': {'stack': 2}},

                    ]
            }}],
        chart_options=
        {'title': {
            'text': 'disk set'}})
    return render_to_response('load_cpuset_chart.html', {'staticchart': cht})
def Outputset(request):
    set = outputset.objects.all().values('id', 'EMPTY', 'ALMOSTEMPTY', 'MEDIUM', 'ALMOSTFULL', 'FULL')
    print list(set)
    ds = DataPool(
        series=
        [{'options': {
            'source':set},
            'terms': [
                'id',
                'EMPTY',
                'ALMOSTEMPTY',
                'MEDIUM',
                'ALMOSTFULL',
                 'FULL']}
        ])

    cht = Chart(
        datasource=ds,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': True,
            'stack': 0},
            'terms': {
                'id':[
                'EMPTY',{'ALMOSTEMPTY': { 'stack': 1}}, {'MEDIUM': {'stack': 2}},{'ALMOSTFULL': {'stack': 3}},{'FULL': {'stack': 4}},

                    ]
            }}],
        chart_options=
        {'title': {
            'text': 'output set'}})
    return render_to_response('load_cpuset_chart.html', {'staticchart': cht})