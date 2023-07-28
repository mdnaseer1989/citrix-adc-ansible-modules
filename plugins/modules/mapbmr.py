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
module: mapbmr
short_description: Configuration for MAP-T Basic Mapping rule resource.
description: Configuration for MAP-T Basic Mapping rule resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  eabitlength:
    description:
      - 'The Embedded Address (EA) bit field encodes the CE-specific IPv4 address
        and port information.  The EA bit field, which is unique for a '
      - "\t\t\t          given Rule IPv6 prefix."
    type: int
    default: 16
  name:
    description:
      - 'Name for the Basic Mapping Rule. Must begin with an ASCII alphanumeric or
        underscore (_) character, and must contain only ASCII alphanumeric, underscore,
        hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-)
        characters. Cannot be changed after the  MAP Basic Mapping Rule is created.
        The following requirement applies only to the Citrix ADC CLI: If the name
        includes one or more spaces, enclose the name in double or single quotation
        marks (for example, "add network MapBmr bmr1 -natprefix 2005::/64 -EAbitLength
        16 -psidoffset 6 -portsharingratio 8" ).'
      - "\t\t\tThe Basic Mapping Rule information allows a MAP BR to determine source\
        \ IPv4 address from the IPv6 packet sent from MAP CE device."
      - "\t\t\tAlso it allows to determine destination IPv6 address of MAP CE before\
        \ sending packets to MAP CE"
    type: str
  psidlength:
    description:
      - Length of Port Set IdentifierPort Set Identifier(PSID) in Embedded Address
        (EA) bits
    type: int
    default: 8
  psidoffset:
    description:
      - Start bit position  of Port Set Identifier(PSID) value in Embedded Address
        (EA) bits.
    type: int
    default: 6
  ruleipv6prefix:
    description:
      - IPv6 prefix of Customer Edge(CE) device.MAP-T CE will send ipv6 packets with
        this ipv6 prefix as source ipv6 address prefix
    type: str
  mapbmr_bmrv4network_binding:
    type: dict
    description: Bindings for mapbmr_bmrv4network_binding resource
    suboptions:
      mode:
        default: desired
        description:
          - The mode in which to configure the bindings.
          - If mode is set to C(desired), the bindings will be added or removed from
            the target NetScaler ADCs as necessary to match the bindings specified
            in the state.
          - If mode is set to C(bind), the specified bindings will be added to the
            resource. The existing bindings in the target ADCs will not be modified.
          - If mode is set to C(unbind), the specified bindings will be removed from
            the resource. The existing bindings in the target ADCs will not be modified.
        choices:
          - desired
          - bind
          - unbind
      binding_members:
        type: list
        elements: dict
        description: List of binding members
        default: []
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
