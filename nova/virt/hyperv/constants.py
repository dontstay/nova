# Copyright 2012 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Constants used in ops classes
"""

from nova.compute import arch
from nova.compute import power_state

HYPERV_VM_STATE_OTHER = 1
HYPERV_VM_STATE_ENABLED = 2
HYPERV_VM_STATE_DISABLED = 3
HYPERV_VM_STATE_SHUTTING_DOWN = 4
HYPERV_VM_STATE_REBOOT = 10
HYPERV_VM_STATE_PAUSED = 32768
HYPERV_VM_STATE_SUSPENDED = 32769

HYPERV_POWER_STATE = {
    HYPERV_VM_STATE_DISABLED: power_state.SHUTDOWN,
    HYPERV_VM_STATE_SHUTTING_DOWN: power_state.SHUTDOWN,
    HYPERV_VM_STATE_ENABLED: power_state.RUNNING,
    HYPERV_VM_STATE_PAUSED: power_state.PAUSED,
    HYPERV_VM_STATE_SUSPENDED: power_state.SUSPENDED
}

WMI_WIN32_PROCESSOR_ARCHITECTURE = {
    0: arch.I686,
    1: arch.MIPS,
    2: arch.ALPHA,
    3: arch.PPC,
    5: arch.ARMV7,
    6: arch.IA64,
    9: arch.X86_64,
}

PROCESSOR_FEATURE = {
    7: '3dnow',
    3: 'mmx',
    12: 'nx',
    9: 'pae',
    8: 'rdtsc',
    20: 'slat',
    13: 'sse3',
    21: 'vmx',
    6: 'sse',
    10: 'sse2',
    17: 'xsave',
}

WMI_JOB_STATUS_STARTED = 4096
WMI_JOB_STATE_RUNNING = 4
WMI_JOB_STATE_COMPLETED = 7

VM_SUMMARY_NUM_PROCS = 4
VM_SUMMARY_ENABLED_STATE = 100
VM_SUMMARY_MEMORY_USAGE = 103
VM_SUMMARY_UPTIME = 105

CTRL_TYPE_IDE = "IDE"
CTRL_TYPE_SCSI = "SCSI"

DISK = "VHD"
DISK_FORMAT = DISK
DVD = "DVD"
DVD_FORMAT = "ISO"

DISK_FORMAT_MAP = {
    DISK_FORMAT.lower(): DISK,
    DVD_FORMAT.lower(): DVD
}

DISK_FORMAT_VHD = "VHD"
DISK_FORMAT_VHDX = "VHDX"

VHD_TYPE_FIXED = 2
VHD_TYPE_DYNAMIC = 3

SCSI_CONTROLLER_SLOTS_NUMBER = 64

HOST_POWER_ACTION_SHUTDOWN = "shutdown"
HOST_POWER_ACTION_REBOOT = "reboot"
HOST_POWER_ACTION_STARTUP = "startup"

IMAGE_PROP_VM_GEN_1 = "hyperv-gen1"
IMAGE_PROP_VM_GEN_2 = "hyperv-gen2"

VM_GEN_1 = 1
VM_GEN_2 = 2
