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
module: smppparam
short_description: Configuration for SMPP configuration parameters resource.
description: Configuration for SMPP configuration parameters resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  addrnpi:
    description:
      - Numbering Plan Indicator, such as landline, data, or WAP client, used in the
        ESME address sent in the bind request.
    type: int
  addrrange:
    description:
      - Set of SME addresses, sent in the bind request, serviced by the ESME.
    type: str
    default: '"\\d*"'
  addrton:
    description:
      - Type of Number, such as an international number or a national number, used
        in the ESME address sent in the bind request.
    type: int
  clientmode:
    choices:
      - TRANSCEIVER
      - TRANSMITTERONLY
      - RECEIVERONLY
    description:
      - 'Mode in which the client binds to the ADC. Applicable settings function as
        follows:'
      - '* C(TRANSCEIVER) - Client can send and receive messages to and from the message
        center.'
      - '* C(TRANSMITTERONLY) - Client can only send messages.'
      - '* C(RECEIVERONLY) - Client can only receive messages.'
    type: str
    default: TRANSCEIVER
  msgqueue:
    choices:
      - true
      - false
    description:
      - Queue SMPP messages if a client that is capable of receiving the destination
        address messages is not available.
    type: str
  msgqueuesize:
    description:
      - Maximum number of SMPP messages that can be queued. After the limit is reached,
        the Citrix ADC sends a deliver_sm_resp PDU, with an appropriate error message,
        to the message center.
    type: int
    default: 10000
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
