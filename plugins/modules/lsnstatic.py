#!/usr/bin/python

# -*- coding: utf-8 -*-

# TODO: Add license

from __future__ import absolute_import, division, print_function

__metaclass__ = type


ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = r"""
module: lsnstatic
short_description: Configuration for static mapping resource.
description: Configuration for static mapping resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  destip:
    description:
      - Destination IP address for the LSN mapping entry.
    type: str
  dsttd:
    description:
      - ID of the traffic domain through which the destination IP address for this
        LSN mapping entry is reachable from the Citrix ADC.
      - ''
      - If you do not specify an ID, the destination IP address is assumed to be reachable
        through the default traffic domain, which has an ID of 0.
    type: int
  name:
    description:
      - 'Name for the LSN static mapping entry. Must begin with an ASCII alphanumeric
        or underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the LSN group is created. The following
        requirement applies only to the Citrix ADC CLI: If the name includes one or
        more spaces, enclose the name in double or single quotation marks (for example,
        "lsn static1" or ''lsn static1'').'
    type: str
  natip:
    description:
      - IPv4 address, already existing on the Citrix ADC as type LSN, to be used as
        NAT IP address for this mapping entry.
    type: str
  natport:
    description:
      - NAT port for this LSN mapping entry. * represents all ports being used. Used
        in case of static wildcard
    type: int
  nattype:
    choices:
      - NAT44
      - DS-Lite
      - NAT64
    description:
      - Type of sessions to be displayed.
    type: str
  network6:
    description:
      - B4 address in DS-Lite setup
    type: str
  subscrip:
    description:
      - IPv4(NAT44 & DS-Lite)/IPv6(NAT64) address of an LSN subscriber for the LSN
        static mapping entry.
    type: str
  subscrport:
    description:
      - Port of the LSN subscriber for the LSN mapping entry. * represents all ports
        being used. Used in case of static wildcard
    type: int
  td:
    description:
      - 'ID of the traffic domain to which the subscriber belongs. '
      - ''
      - If you do not specify an ID, the subscriber is assumed to be a part of the
        default traffic domain.
    type: int
  transportprotocol:
    choices:
      - TCP
      - UDP
      - ICMP
      - ALL
    description:
      - Protocol for the LSN mapping entry.
    type: str
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