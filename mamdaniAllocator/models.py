from __future__ import unicode_literals

from django.db import models

# class VirtualMachine(models.Model):
#     machine_name = models.CharField(max_length=100)
#     machine_cpu = models.IntegerField(default=0)
#     machine_ram = models.IntegerField(default=0)
#     machine_disk = models.IntegerField(default=0)


class cpuset(models.Model):
    SMALL = models.FloatField(default=0)
    MEDIUM = models.FloatField(default=0)
    LARGE = models.FloatField(default=0)

class ramset(models.Model):
    SMALL = models.FloatField(default=0)
    MEDIUM = models.FloatField(default=0)
    LARGE = models.FloatField(default=0)

class diskset(models.Model):
    SMALL = models.FloatField(default=0)
    MEDIUM = models.FloatField(default=0)
    LARGE = models.FloatField(default=0)

class outputset(models.Model):
    EMPTY = models.FloatField(default=0)
    ALMOSTEMPTY = models.FloatField(default=0)
    MEDIUM = models.FloatField(default=0)
    ALMOSTFULL = models.FloatField(default=0)
    FULL = models.FloatField(default=0)

class outputfunction(models.Model):
    server_index = models.FloatField(default=0)
    EMPTY = models.FloatField(default=0)
    ALMOSTEMPTY = models.FloatField(default=0)
    MEDIUM = models.FloatField(default=0)
    ALMOSTFULL = models.FloatField(default=0)
    FULL = models.FloatField(default=0)
class Ramusage(models.Model):
    usage = models.IntegerField()
    SMALL = models.IntegerField(default=0)
    MEDIUM = models.IntegerField(default=0)
    LARGE = models.IntegerField(default=0)

class CPUusage(models.Model):
    usage = models.IntegerField()
    SMALL = models.IntegerField(default=0)
    MEDIUM = models.IntegerField(default=0)
    LARGE = models.IntegerField(default=0)

class Diskusage(models.Model):
    usage = models.IntegerField()
    SMALL = models.IntegerField(default=0)
    MEDIUM = models.IntegerField(default=0)
    LARGE = models.IntegerField(default=0)

#
# class Server(models.Model):
#     virtual_machine = models.ForeignKey(VirtualMachine, null=True)
#     server_name = models.CharField(max_length=100)
#     server_cpu = models.IntegerField(default=100)
#     server_ram = models.IntegerField(default=100)
#     server_disk = models.IntegerField(default=100)
#
#
#     def updateServer(self, virtualmachine):
#         self.server_cpu -= virtualmachine.machine_cpu
#         self.server_ram -= virtualmachine.machine_ram
#         self.server_disk -= virtualmachine.machine_disk


from django.db import models
