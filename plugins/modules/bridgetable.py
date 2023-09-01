#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2020 Citrix Systems, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: bridgetable
short_description: Configuration for bridge table entry resource.
description: Configuration for bridge table entry resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  bridgeage:
    description:
      - Time-out value for the bridge table entries, in seconds. The new value applies
        only to the entries that are dynamically learned after the new value is set.
        Previously existing bridge table entries expire after the previously configured
        time-out value.
    type: float
    default: 300
  devicevlan:
    description:
      - The vlan on which to send multicast packets when the VXLAN tunnel endpoint
        is a muticast group address.
    type: float
  ifnum:
    description:
      - INTERFACE  whose entries are to be removed.
    type: str
  mac:
    description:
      - The MAC address of the target.
    type: str
  nodeid:
    description:
      - Unique number that identifies the cluster node.
    type: float
  vlan:
    description:
      - VLAN  whose entries are to be removed.
    type: float
  vni:
    description:
      - The VXLAN VNI Network Identifier (or VXLAN Segment ID) to use to connect to
        the remote VXLAN tunnel endpoint.  If omitted the value specified as vxlan
        will be used.
    type: float
  vtep:
    description:
      - The IP address of the destination VXLAN tunnel endpoint where the Ethernet
        MAC ADDRESS resides.
    type: str
  vxlan:
    description:
      - The VXLAN to which this address is associated.
    type: float
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
changed:
    description: Indicates if any change is made by the module
    returned: always
    type: bool
    sample: true
diff:
    description: Dictionary of before and after changes
    returned: always
    type: dict
    sample: { 'before': { 'key1': 'xyz' }, 'after': { 'key2': 'pqr' }, 'prepared': 'changes done' }
diff_list:
    description: List of differences between the actual configured object and the configuration specified in the module
    returned: when changed
    type: list
    sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class 'str'>) PQR"]
failed:
    description: Indicates if the module failed or not
    returned: always
    type: bool
    sample: false
loglines:
    description: list of logged messages by the module
    returned: always
    type: list
    sample: ['message 1', 'message 2']

"""


import os

from ..module_utils.module_executor import ModuleExecutor

RESOURCE_NAME = os.path.basename(__file__).replace(".py", "")


def main():
    executor = ModuleExecutor(RESOURCE_NAME)
    executor.main()


if __name__ == "__main__":
    main()
