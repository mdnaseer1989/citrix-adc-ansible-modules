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
module: gslbservicegroup
short_description: Configuration for GSLB service group resource.
description: Configuration for GSLB service group resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  appflowlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable logging of AppFlow information for the specified GSLB service group.
    type: str
    default: ENABLED
  autoscale:
    choices:
      - DISABLED
      - DNS
    description:
      - Auto scale option for a GSLB servicegroup
    type: str
    default: DISABLED
  cip:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Insert the Client IP header in requests forwarded to the GSLB service.
    type: str
  cipheader:
    description:
      - Name of the HTTP header whose value must be set to the IP address of the client.
        Used with the Client IP parameter. If client IP insertion is enabled, and
        the client IP header is not specified, the value of Client IP Header parameter
        or the value set by the set ns config command is used as client's IP header
        name.
    type: str
  clttimeout:
    description:
      - Time, in seconds, after which to terminate an idle client connection.
    type: int
  comment:
    description:
      - Any information about the GSLB service group.
    type: str
  delay:
    description:
      - The time allowed (in seconds) for a graceful shutdown. During this period,
        new connections or requests will continue to be sent to this service for clients
        who already have a persistent session on the system. Connections or requests
        from fresh or new clients who do not yet have a persistence sessions on the
        system will not be sent to the service. Instead, they will be load balanced
        among other available services. After the delay time expires, no new requests
        or connections will be sent to the service.
    type: int
  downstateflush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with all the services in the GSLB
        service group whose state transitions from UP to DOWN. Do not enable this
        option for applications that must complete their transactions.
    type: str
    default: ENABLED
  dup_weight:
    description:
      - weight of the monitor that is bound to GSLB servicegroup.
    type: int
  graceful:
    choices:
      - true
      - false
    description:
      - Wait for all existing connections to the service to terminate before shutting
        down the service.
    type: str
  hashid:
    description:
      - The hash identifier for the service. This must be unique for each service.
        This parameter is used by hash based load balancing methods.
    type: int
  healthmonitor:
    choices:
      - true
      - false
    description:
      - 'Monitor the health of this GSLB service.Available settings function are as
        follows:'
      - YES - Send probes to check the health of the GSLB service.
      - NO - Do not send probes to check the health of the GSLB service. With the
        NO option, the appliance shows the service as UP at all times.
    type: str
    default: true
  includemembers:
    description:
      - Display the members of the listed GSLB service groups in addition to their
        settings. Can be specified when no service group name is provided in the command.
        In that case, the details displayed for each service group are identical to
        the details displayed when a service group name is provided, except that bound
        monitors are not displayed.
    type: bool
  maxbandwidth:
    description:
      - Maximum bandwidth, in Kbps, allocated for all the services in the GSLB service
        group.
    type: int
  maxclient:
    description:
      - Maximum number of simultaneous open connections for the GSLB service group.
    type: int
  monitor_name_svc:
    description:
      - Name of the monitor bound to the GSLB service group. Used to assign a weight
        to the monitor.
    type: str
  monthreshold:
    description:
      - Minimum sum of weights of the monitors that are bound to this GSLB service.
        Used to determine whether to mark a GSLB service as UP or DOWN.
    type: int
  newname:
    description:
      - New name for the GSLB service group.
    type: str
  order:
    description:
      - Order number to be assigned to the gslb servicegroup member
    type: int
  port:
    description:
      - Server port number.
    type: int
  publicip:
    description:
      - The public IP address that a NAT device translates to the GSLB service's private
        IP address. Optional.
    type: str
  publicport:
    description:
      - The public port associated with the GSLB service's public IP address. The
        port is mapped to the service's private port number. Applicable to the local
        GSLB service. Optional.
    type: int
  servername:
    description:
      - Name of the server to which to bind the service group.
    type: str
  servicegroupname:
    description:
      - Name of the GSLB service group. Must begin with an ASCII alphabetic or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.
        Can be changed after the name is created.
    type: str
  servicetype:
    choices:
      - HTTP
      - FTP
      - TCP
      - UDP
      - SSL
      - SSL_BRIDGE
      - SSL_TCP
      - NNTP
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - RADIUS
      - RDP
      - RTSP
      - MYSQL
      - MSSQL
      - ORACLE
    description:
      - Protocol used to exchange data with the GSLB service.
    type: str
  sitename:
    description:
      - Name of the GSLB site to which the service group belongs.
    type: str
  sitepersistence:
    choices:
      - ConnectionProxy
      - HTTPRedirect
      - NONE
    description:
      - Use cookie-based site persistence. Applicable only to HTTP and SSL non-autoscale
        enabled GSLB servicegroups.
    type: str
  siteprefix:
    description:
      - The site's prefix string. When the GSLB service group is bound to a GSLB virtual
        server, a GSLB site domain is generated internally for each bound serviceitem-domain
        pair by concatenating the site prefix of the service item and the name of
        the domain. If the special string NONE is specified, the site-prefix string
        is unset. When implementing HTTP redirect site persistence, the Citrix ADC
        redirects GSLB requests to GSLB services by using their site domains.
    type: str
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Initial state of the GSLB service group.
    type: str
    default: ENABLED
  svrtimeout:
    description:
      - Time, in seconds, after which to terminate an idle server connection.
    type: int
  weight:
    description:
      - Weight to assign to the servers in the service group. Specifies the capacity
        of the servers relative to the other servers in the load balancing configuration.
        The higher the weight, the higher the percentage of requests sent to the service.
    type: int
  gslbservicegroup_gslbservicegroupmember_binding:
    type: dict
    description: Bindings for gslbservicegroup_gslbservicegroupmember_binding resource
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
  gslbservicegroup_lbmonitor_binding:
    type: dict
    description: Bindings for gslbservicegroup_lbmonitor_binding resource
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