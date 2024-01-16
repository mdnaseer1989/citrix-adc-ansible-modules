#!/usr/bin/python

# -*- coding: utf-8 -*-

# Copyright (c) 2023 Cloud Software Group, Inc.
# MIT License (see LICENSE or https://opensource.org/licenses/MIT)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: ntpserver
short_description: Configuration for NTP server resource.
description: Configuration for NTP server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  state:
    choices:
      - present
      - absent
    default: present
    description:
      - The state of the resource being configured by the module on the NetScaler
        ADC node.
      - When C(present), the resource will be added/updated configured according to
        the module's parameters.
      - When C(absent), the resource will be deleted from the NetScaler ADC node.
    type: str
  autokey:
    type: bool
    description:
      - Use the Autokey protocol for key management for this server, with the cryptographic
        values (for example, symmetric key, host and public certificate files, and
        sign key) generated by the ntp-keygen utility. To require authentication for
        communication with the server, you must set either the value of this parameter
        or the key parameter.
  key:
    type: float
    description:
      - Key to use for encrypting authentication fields. All packets sent to and received
        from the server must include authentication fields encrypted by using this
        key. To require authentication for communication with the server, you must
        set either the value of this parameter or the autokey parameter.
  maxpoll:
    type: float
    description:
      - Maximum time after which the NTP server must poll the NTP messages. In seconds,
        expressed as a power of 2.
  minpoll:
    type: float
    description:
      - Minimum time after which the NTP server must poll the NTP messages. In seconds,
        expressed as a power of 2.
  preferredntpserver:
    type: str
    choices:
      - 'YES'
      - 'NO'
    description:
      - Preferred NTP server. The Citrix ADC chooses this NTP server for time synchronization
        among a set of correctly operating hosts.
  serverip:
    type: str
    description:
      - IP address of the NTP server.
  servername:
    type: str
    description:
      - Fully qualified domain name of the NTP server.
extends_documentation_fragment: netscaler.adc.netscaler_adc

"""

EXAMPLES = r"""
"""

RETURN = r"""
---
changed:
  description: Indicates if any change is made by the module
  returned: always
  type: bool
  sample: true
diff:
  description: Dictionary of before and after changes
  returned: always
  type: dict
  sample: {'before': {'key1': 'xyz'}, 'after': {'key2': 'pqr'}, 'prepared': 'changes
      done'}
diff_list:
  description: List of differences between the actual configured object and the configuration
    specified in the module
  returned: when changed
  type: list
  sample: ["Attribute `key1` differs. Desired: (<class 'str'>) XYZ. Existing: (<class
      'str'>) PQR"]
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
