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
module: lbvserver
short_description: Configuration for Load Balancing Virtual Server resource.
description: Configuration for Load Balancing Virtual Server resource.
version_added: 2.0.0
author:
  - Sumanth Lingappa (@sumanth-lingappa)
options:
  adfsproxyprofile:
    description:
      - Name of the adfsProxy profile to be used to support ADFSPIP protocol for ADFS
        servers.
    type: str
  appflowlog:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Apply AppFlow logging to the virtual server.
    type: str
    default: ENABLED
  authentication:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable user authentication.
    type: str
    default: 'OFF'
  authenticationhost:
    description:
      - Fully qualified domain name (FQDN) of the authentication virtual server to
        which the user must be redirected for authentication. Make sure that the Authentication
        parameter is set to ENABLED.
    type: str
  authn401:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Enable or disable user authentication with HTTP 401 responses.
    type: str
    default: 'OFF'
  authnprofile:
    description:
      - Name of the authentication profile to be used when authentication is turned
        on.
    type: str
  authnvsname:
    description:
      - Name of an authentication virtual server with which to authenticate users.
    type: str
  backuplbmethod:
    choices:
      - ROUNDROBIN
      - LEASTCONNECTION
      - LEASTRESPONSETIME
      - SOURCEIPHASH
      - LEASTBANDWIDTH
      - LEASTPACKETS
      - CUSTOMLOAD
    description:
      - Backup load balancing method. Becomes operational if the primary load balancing
        me
      - thod fails or cannot be used.
      - '                       Valid only if the primary method is based on static
        proximity.'
    type: str
    default: ROUNDROBIN
  backuppersistencetimeout:
    description:
      - Time period for which backup persistence is in effect.
    type: float
    default: 2
  backupvserver:
    description:
      - Name of the backup virtual server to which to forward requests if the primary
        virtual server goes DOWN or reaches its spillover threshold.
    type: str
  bypassaaaa:
    choices:
      - 'YES'
      - 'NO'
    description:
      - If this option is enabled while resolving DNS64 query AAAA queries are not
        sent to back end dns server
    type: str
    default: 'NO'
  cacheable:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Route cacheable requests to a cache redirection virtual server. The load balancing
        virtual server can forward requests only to a transparent cache redirection
        virtual server that has an IP address and port combination of *:80, so such
        a cache redirection virtual server must be configured on the appliance.
    type: str
    default: 'NO'
  clttimeout:
    description:
      - Idle time, in seconds, after which a client connection is terminated.
    type: float
  comment:
    description:
      - Any comments that you might want to associate with the virtual server.
    type: str
  connfailover:
    choices:
      - DISABLED
      - STATEFUL
      - STATELESS
    description:
      - 'Mode in which the connection failover feature must operate for the virtual
        server. After a failover, established TCP connections and UDP packet flows
        are kept active and resumed on the secondary appliance. Clients remain connected
        to the same servers. Available settings function as follows:'
      - '* C(STATEFUL) - The primary appliance shares state information with the secondary
        appliance, in real time, resulting in some runtime processing overhead. '
      - '* C(STATELESS) - State information is not shared, and the new primary appliance
        tries to re-create the packet flow on the basis of the information contained
        in the packets it receives. '
      - '* C(DISABLED) - Connection failover does not occur.'
    type: str
    default: DISABLED
  cookiename:
    description:
      - Use this parameter to specify the cookie name for COOKIE peristence type.
        It specifies the name of cookie with a maximum of 32 characters. If not specified,
        cookie name is internally generated.
    type: str
  datalength:
    description:
      - Length of the token to be extracted from the data segment of an incoming packet,
        for use in the token method of load balancing. The length of the token, specified
        in bytes, must not be greater than 24 KB. Applicable to virtual servers of
        type TCP.
    type: float
  dataoffset:
    description:
      - Offset to be considered when extracting a token from the TCP payload. Applicable
        to virtual servers, of type TCP, using the token method of load balancing.
        Must be within the first 24 KB of the TCP payload.
    type: float
  dbprofilename:
    description:
      - Name of the DB profile whose settings are to be applied to the virtual server.
    type: str
  dbslb:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Enable database specific load balancing for MySQL and MSSQL service types.
    type: str
    default: DISABLED
  disableprimaryondown:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If the primary virtual server goes down, do not allow it to return to primary
        status until manually enabled.
    type: str
    default: DISABLED
  dns64:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This argument is for enabling/disabling the dns64 on lbvserver
    type: str
  dnsprofilename:
    description:
      - Name of the DNS profile to be associated with the VServer. DNS profile properties
        will be applied to the transactions processed by a VServer. This parameter
        is valid only for DNS and DNS-TCP VServers.
    type: str
  downstateflush:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Flush all active transactions associated with a virtual server whose state
        transitions from UP to DOWN. Do not enable this option for applications that
        must complete their transactions.
    type: str
    default: ENABLED
  hashlength:
    description:
      - Number of bytes to consider for the hash value used in the URLHASH and DOMAINHASH
        load balancing methods.
    type: float
    default: 80
  healththreshold:
    description:
      - Threshold in percent of active services below which vserver state is made
        down. If this threshold is 0, vserver state will be up even if one bound service
        is up.
    type: float
  httpprofilename:
    description:
      - Name of the HTTP profile whose settings are to be applied to the virtual server.
    type: str
  httpsredirecturl:
    description:
      - URL to which all HTTP traffic received on the port specified in the -redirectFromPort
        parameter is redirected.
    type: str
  icmpvsrresponse:
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - 'How the Citrix ADC responds to ping requests received for an IP address that
        is common to one or more virtual servers. Available settings function as follows:'
      - '* If set to C(PASSIVE) on all the virtual servers that share the IP address,
        the appliance always responds to the ping requests.'
      - '* If set to C(ACTIVE) on all the virtual servers that share the IP address,
        the appliance responds to the ping requests if at least one of the virtual
        servers is UP. Otherwise, the appliance does not respond.'
      - '* If set to C(ACTIVE) on some virtual servers and C(PASSIVE) on the others,
        the appliance responds if at least one virtual server with the C(ACTIVE) setting
        is UP. Otherwise, the appliance does not respond.'
      - 'Note: This parameter is available at the virtual server level. A similar
        parameter, ICMP Response, is available at the IP address level, for IPv4 addresses
        of type VIP. To set that parameter, use the add ip command in the CLI or the
        Create IP dialog box in the GUI.'
    type: str
    default: PASSIVE
  insertvserveripport:
    choices:
      - 'OFF'
      - VIPADDR
      - V6TOV4MAPPING
    description:
      - 'Insert an HTTP header, whose value is the IP address and port number of the
        virtual server, before forwarding a request to the server. The format of the
        header is <vipHeader>: <virtual server IP address>_<port number >, where vipHeader
        is the name that you specify for the header. If the virtual server has an
        IPv6 address, the address in the header is enclosed in brackets ([ and ])
        to separate it from the port number. If you have mapped an IPv4 address to
        a virtual server''s IPv6 address, the value of this parameter determines which
        IP address is inserted in the header, as follows:'
      - '* C(VIPADDR) - Insert the IP address of the virtual server in the HTTP header
        regardless of whether the virtual server has an IPv4 address or an IPv6 address.
        A mapped IPv4 address, if configured, is ignored.'
      - '* C(V6TOV4MAPPING) - Insert the IPv4 address that is mapped to the virtual
        server''s IPv6 address. If a mapped IPv4 address is not configured, insert
        the IPv6 address.'
      - '* C(OFF) - Disable header insertion.'
    type: str
  ipmask:
    description:
      - IP mask, in dotted decimal notation, for the IP Pattern parameter. Can have
        leading or trailing non-zero octets (for example, 255.255.240.0 or 0.0.255.255).
        Accordingly, the mask specifies whether the first n bits or the last n bits
        of the destination IP address in a client request are to be matched with the
        corresponding bits in the IP pattern. The former is called a forward mask.
        The latter is called a reverse mask.
    type: str
  ippattern:
    description:
      - 'IP address pattern, in dotted decimal notation, for identifying packets to
        be accepted by the virtual server. The IP Mask parameter specifies which part
        of the destination IP address is matched against the pattern.  Mutually exclusive
        with the IP Address parameter. '
      - For example, if the IP pattern assigned to the virtual server is 198.51.100.0
        and the IP mask is 255.255.240.0 (a forward mask), the first 20 bits in the
        destination IP addresses are matched with the first 20 bits in the pattern.
        The virtual server accepts requests with IP addresses that range from 198.51.96.1
        to 198.51.111.254.  You can also use a pattern such as 0.0.2.2 and a mask
        such as 0.0.255.255 (a reverse mask).
      - If a destination IP address matches more than one IP pattern, the pattern
        with the longest match is selected, and the associated virtual server processes
        the request. For example, if virtual servers vs1 and vs2 have the same IP
        pattern, 0.0.100.128, but different IP masks of 0.0.255.255 and 0.0.224.255,
        a destination IP address of 198.51.100.128 has the longest match with the
        IP pattern of vs1. If a destination IP address matches two or more virtual
        servers to the same extent, the request is processed by the virtual server
        whose port number matches the port number in the request.
    type: str
  ipset:
    description:
      - The list of IPv4/IPv6 addresses bound to ipset would form a part of listening
        service on the current lb vserver
    type: str
  ipv46:
    description:
      - IPv4 or IPv6 address to assign to the virtual server.
    type: str
  l2conn:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use Layer 2 parameters (channel number, MAC address, and VLAN ID) in addition
        to the 4-tuple (<source IP>:<source port>::<destination IP>:<destination port>)
        that is used to identify a connection. Allows multiple TCP and non-TCP connections
        with the same 4-tuple to co-exist on the Citrix ADC.
    type: str
  lbmethod:
    choices:
      - ROUNDROBIN
      - LEASTCONNECTION
      - LEASTRESPONSETIME
      - URLHASH
      - DOMAINHASH
      - DESTINATIONIPHASH
      - SOURCEIPHASH
      - SRCIPDESTIPHASH
      - LEASTBANDWIDTH
      - LEASTPACKETS
      - TOKEN
      - SRCIPSRCPORTHASH
      - LRTM
      - CALLIDHASH
      - CUSTOMLOAD
      - LEASTREQUEST
      - AUDITLOGHASH
      - STATICPROXIMITY
      - USER_TOKEN
    description:
      - 'Load balancing method.  The available settings function as follows:'
      - '* C(ROUNDROBIN) - Distribute requests in rotation, regardless of the load.
        Weights can be assigned to services to enforce weighted round robin distribution.'
      - '* C(LEASTCONNECTION) (default) - Select the service with the fewest connections. '
      - '* C(LEASTRESPONSETIME) - Select the service with the lowest average response
        time. '
      - '* C(LEASTBANDWIDTH) - Select the service currently handling the least traffic.'
      - '* C(LEASTPACKETS) - Select the service currently serving the lowest number
        of packets per second.'
      - '* C(CUSTOMLOAD) - Base service selection on the SNMP metrics obtained by
        custom load monitors.'
      - '* C(LRTM) - Select the service with the lowest response time. Response times
        are learned through monitoring probes. This method also takes the number of
        active connections into account.'
      - 'Also available are a number of hashing methods, in which the appliance extracts
        a predetermined portion of the request, creates a hash of the portion, and
        then checks whether any previous requests had the same hash value. If it finds
        a match, it forwards the request to the service that served those previous
        requests. Following are the hashing methods: '
      - '* C(URLHASH) - Create a hash of the request URL (or part of the URL).'
      - '* C(DOMAINHASH) - Create a hash of the domain name in the request (or part
        of the domain name). The domain name is taken from either the URL or the Host
        header. If the domain name appears in both locations, the URL is preferred.
        If the request does not contain a domain name, the load balancing method defaults
        to C(LEASTCONNECTION).'
      - '* C(DESTINATIONIPHASH) - Create a hash of the destination IP address in the
        IP header. '
      - '* C(SOURCEIPHASH) - Create a hash of the source IP address in the IP header.  '
      - '* C(TOKEN) - Extract a token from the request, create a hash of the token,
        and then select the service to which any previous requests with the same token
        hash value were sent. '
      - '* C(SRCIPDESTIPHASH) - Create a hash of the string obtained by concatenating
        the source IP address and destination IP address in the IP header.  '
      - '* C(SRCIPSRCPORTHASH) - Create a hash of the source IP address and source
        port in the IP header.  '
      - '* C(CALLIDHASH) - Create a hash of the SIP Call-ID header.'
      - '* C(USER_TOKEN) - Same as C(TOKEN) LB method but token needs to be provided
        from an extension.'
    type: str
    default: LEASTCONNECTION
  lbprofilename:
    description:
      - Name of the LB profile which is associated to the vserver
    type: str
  listenpolicy:
    description:
      - Expression identifying traffic accepted by the virtual server. Can be either
        an expression (for example, CLIENT.IP.DST.IN_SUBNET(192.0.2.0/24) or the name
        of a named expression. In the above example, the virtual server accepts all
        requests whose destination IP address is in the 192.0.2.0/24 subnet.
    type: str
    default: '"NONE"'
  listenpriority:
    description:
      - Integer specifying the priority of the listen policy. A higher number specifies
        a lower priority. If a request matches the listen policies of more than one
        virtual server the virtual server whose listen policy has the highest priority
        (the lowest priority number) accepts the request.
    type: float
    default: 101
  m:
    choices:
      - IP
      - MAC
      - IPTUNNEL
      - TOS
    description:
      - 'Redirection mode for load balancing. Available settings function as follows:'
      - '* C(IP) - Before forwarding a request to a server, change the destination
        C(IP) address to the server''s C(IP) address. '
      - '* C(MAC) - Before forwarding a request to a server, change the destination
        C(MAC) address to the server''s C(MAC) address.  The destination C(IP) address
        is not changed. C(MAC)-based redirection mode is used mostly in firewall load
        balancing deployments. '
      - '* C(IPTUNNEL) - Perform C(IP)-in-C(IP) encapsulation for client C(IP) packets.
        In the outer C(IP) headers, set the destination C(IP) address to the C(IP)
        address of the server and the source C(IP) address to the subnet C(IP) (SNIP).
        The client C(IP) packets are not modified. Applicable to both IPv4 and IPv6
        packets. '
      - '* C(TOS) - Encode the virtual server''s C(TOS) ID in the C(TOS) field of
        the C(IP) header. '
      - You can use either the C(IPTUNNEL) or the C(TOS) option to implement Direct
        Server Return (DSR).
    type: str
    default: IP
  macmoderetainvlan:
    choices:
      - ENABLED
      - DISABLED
    description:
      - This option is used to retain vlan information of incoming packet when macmode
        is enabled
    type: str
    default: DISABLED
  maxautoscalemembers:
    description:
      - Maximum number of members expected to be present when vserver is used in Autoscale.
    type: float
  minautoscalemembers:
    description:
      - Minimum number of members expected to be present when vserver is used in Autoscale.
    type: float
  mssqlserverversion:
    choices:
      - 70
      - 2000
      - 2000SP1
      - 2005
      - 2008
      - 2008R2
      - 2012
      - 2014
    description:
      - For a load balancing virtual server of type MSSQL, the Microsoft SQL Server
        version. Set this parameter if you expect some clients to run a version different
        from the version of the database. This setting provides compatibility between
        the client-side and server-side connections by ensuring that all communication
        conforms to the server's version.
    type: str
    default: 2008R2
  mysqlcharacterset:
    description:
      - Character set that the virtual server advertises to clients.
    type: float
  mysqlprotocolversion:
    description:
      - MySQL protocol version that the virtual server advertises to clients.
    type: float
  mysqlservercapabilities:
    description:
      - Server capabilities that the virtual server advertises to clients.
    type: float
  mysqlserverversion:
    description:
      - MySQL server version string that the virtual server advertises to clients.
    type: str
  name:
    description:
      - Name for the virtual server. Must begin with an ASCII alphanumeric or underscore
        (_) character, and must contain only ASCII alphanumeric, underscore, hash
        (#), period (.), space, colon (:), at sign (@), equal sign (=), and hyphen
        (-) characters. Can be changed after the virtual server is created.
      - ''
      - 'CLI Users: If the name includes one or more spaces, enclose the name in double
        or single quotation marks (for example, "my vserver" or ''my vserver'').'
    type: str
  netmask:
    description:
      - IPv4 subnet mask to apply to the destination IP address or source IP address
        when the load balancing method is DESTINATIONIPHASH or SOURCEIPHASH.
    type: str
  netprofile:
    description:
      - Name of the network profile to associate with the virtual server. If you set
        this parameter, the virtual server uses only the IP addresses in the network
        profile as source IP addresses when initiating connections with servers.
    type: str
  newname:
    description:
      - New name for the virtual server.
    type: str
  newservicerequest:
    description:
      - Number of requests, or percentage of the load on existing services, by which
        to increase the load on a new service at each interval in slow-start mode.
        A non-zero value indicates that slow-start is applicable. A zero value indicates
        that the global RR startup parameter is applied. Changing the value to zero
        will cause services currently in slow start to take the full traffic as determined
        by the LB method. Subsequently, any new services added will use the global
        RR factor.
    type: float
  newservicerequestincrementinterval:
    description:
      - Interval, in seconds, between successive increments in the load on a new service
        or a service whose state has just changed from DOWN to UP. A value of 0 (zero)
        specifies manual slow start.
    type: float
  newservicerequestunit:
    choices:
      - PER_SECOND
      - PERCENT
    description:
      - Units in which to increment load at each interval in slow-start mode.
    type: str
    default: PER_SECOND
  oracleserverversion:
    choices:
      - 10G
      - 11G
    description:
      - Oracle server version
    type: str
    default: 10G
  order:
    description:
      - Order number to be assigned to the service when it is bound to the lb vserver.
    type: float
  orderthreshold:
    description:
      - This option is used to to specify the threshold of minimum number of services
        to be UP in an order, for it to be considered in Lb decision.
    type: float
  persistavpno:
    description:
      - 'Persist AVP number for Diameter Persistency. '
      - '            In case this AVP is not defined in Base RFC 3588 and it is nested
        inside a Grouped AVP, '
      - '            define a sequence of AVP numbers (max 3) in order of parent to
        child. So say persist AVP number X '
      - '            is nested inside AVP Y which is nested in Z, then define the
        list as  Z Y X'
    type: list
  persistencebackup:
    choices:
      - SOURCEIP
      - NONE
    description:
      - Backup persistence type for the virtual server. Becomes operational if the
        primary persistence mechanism fails.
    type: str
  persistencetype:
    choices:
      - SOURCEIP
      - COOKIEINSERT
      - SSLSESSION
      - RULE
      - URLPASSIVE
      - CUSTOMSERVERID
      - DESTIP
      - SRCIPDESTIP
      - CALLID
      - RTSPSID
      - DIAMETER
      - FIXSESSION
      - USERSESSION
      - NONE
    description:
      - 'Type of persistence for the virtual server. Available settings function as
        follows:'
      - '* C(SOURCEIP) - Connections from the same client IP address belong to the
        same persistence session.'
      - '* C(COOKIEINSERT) - Connections that have the same HTTP Cookie, inserted
        by a Set-Cookie directive from a server, belong to the same persistence session. '
      - '* C(SSLSESSION) - Connections that have the same SSL Session ID belong to
        the same persistence session.'
      - '* C(CUSTOMSERVERID) - Connections with the same server ID form part of the
        same session. For this persistence type, set the Server ID (CustomServerID)
        parameter for each service and configure the Rule parameter to identify the
        server ID in a request.'
      - '* C(RULE) - All connections that match a user defined rule belong to the
        same persistence session. '
      - '* C(URLPASSIVE) - Requests that have the same server ID in the URL query
        belong to the same persistence session. The server ID is the hexadecimal representation
        of the IP address and port of the service to which the request must be forwarded.
        This persistence type requires a rule to identify the server ID in the request. '
      - '* C(DESTIP) - Connections to the same destination IP address belong to the
        same persistence session.'
      - '* C(SRCIPDESTIP) - Connections that have the same source IP address and destination
        IP address belong to the same persistence session.'
      - '* C(CALLID) - Connections that have the same CALL-ID SIP header belong to
        the same persistence session.'
      - '* C(RTSPSID) - Connections that have the same RTSP Session ID belong to the
        same persistence session.'
      - '* C(FIXSESSION) - Connections that have the same SenderCompID and TargetCompID
        values belong to the same persistence session.'
      - '* C(USERSESSION) - Persistence session is created based on the persistence
        parameter value provided from an extension.'
    type: str
  persistmask:
    description:
      - Persistence mask for IP based persistence types, for IPv4 virtual servers.
    type: str
  port:
    description:
      - Port number for the virtual server.
    type: int
  probeport:
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select port for HTTP/TCP monitring
    type: int
  probeprotocol:
    choices:
      - TCP
      - HTTP
    description:
      - Citrix ADC provides support for external health check of the vserver status.
        Select C(HTTP) or C(TCP) probes for healthcheck
    type: str
  probesuccessresponsecode:
    description:
      - HTTP code to return in SUCCESS case.
    type: str
    default: '"200 OK"'
  processlocal:
    choices:
      - ENABLED
      - DISABLED
    description:
      - By turning on this option packets destined to a vserver in a cluster will
        not under go any steering. Turn this option for single packet request response
        mode or when the upstream device is performing a proper RSS for connection
        based distribution.
    type: str
    default: DISABLED
  push:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Process traffic with the push virtual server that is bound to this load balancing
        virtual server.
    type: str
    default: DISABLED
  pushlabel:
    description:
      - Expression for extracting a label from the server's response. Can be either
        an expression or the name of a named expression.
    type: str
    default: '"none"'
  pushmulticlients:
    choices:
      - 'YES'
      - 'NO'
    description:
      - Allow multiple Web 2.0 connections from the same client to connect to the
        virtual server and expect updates.
    type: str
    default: 'NO'
  pushvserver:
    description:
      - Name of the load balancing virtual server, of type PUSH or SSL_PUSH, to which
        the server pushes updates received on the load balancing virtual server that
        you are configuring.
    type: str
  quicbridgeprofilename:
    description:
      - Name of the QUIC Bridge profile whose settings are to be applied to the virtual
        server.
    type: str
  quicprofilename:
    description:
      - Name of QUIC profile which will be attached to the VServer.
    type: str
  range:
    description:
      - 'Number of IP addresses that the appliance must generate and assign to the
        virtual server. The virtual server then functions as a network virtual server,
        accepting traffic on any of the generated IP addresses. The IP addresses are
        generated automatically, as follows: '
      - '* For a range of n, the last octet of the address specified by the IP Address
        parameter increments n-1 times. '
      - '* If the last octet exceeds 255, it rolls over to 0 and the third octet increments
        by 1.'
      - 'Note: The Range parameter assigns multiple IP addresses to one virtual server.
        To generate an array of virtual servers, each of which owns only one IP address,
        use brackets in the IP Address and Name parameters to specify the range. For
        example:'
      - add lb vserver my_vserver[1-3] HTTP 192.0.2.[1-3] 80
    type: float
    default: 1
  recursionavailable:
    choices:
      - 'YES'
      - 'NO'
    description:
      - When set to C(YES), this option causes the DNS replies from this vserver to
        have the RA bit turned on. Typically one would set this option to C(YES),
        when the vserver is load balancing a set of DNS servers thatsupport recursive
        queries.
    type: str
    default: 'NO'
  redirectfromport:
    description:
      - Port number for the virtual server, from which we absorb the traffic for http
        redirect
    type: int
  redirectportrewrite:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Rewrite the port and change the protocol to ensure successful HTTP redirects
        from services.
    type: str
    default: DISABLED
  redirurl:
    description:
      - 'URL to which to redirect traffic if the virtual server becomes unavailable. '
      - WARNING! Make sure that the domain in the URL does not match the domain specified
        for a content switching policy. If it does, requests are continuously redirected
        to the unavailable virtual server.
    type: str
  redirurlflags:
    description:
      - The redirect URL to be unset.
    type: bool
  resrule:
    description:
      - Expression specifying which part of a server's response to use for creating
        rule based persistence sessions (persistence type RULE). Can be either an
        expression or the name of a named expression.
      - 'Example:'
      - HTTP.RES.HEADER("setcookie").VALUE(0).TYPECAST_NVLIST_T('=',';').VALUE("server1").
    type: str
    default: '"none"'
  retainconnectionsoncluster:
    choices:
      - 'YES'
      - 'NO'
    description:
      - This option enables you to retain existing connections on a node joining a
        Cluster system or when a node is being configured for passive timeout. By
        default, this option is disabled.
    type: str
    default: 'NO'
  rhistate:
    choices:
      - PASSIVE
      - ACTIVE
    description:
      - 'Route Health Injection (RHI) functionality of the NetSaler appliance for
        advertising the route of the VIP address associated with the virtual server.
        When Vserver RHI Level (RHI) parameter is set to VSVR_CNTRLD, the following
        are different RHI behaviors for the VIP address on the basis of RHIstate (RHI
        STATE) settings on the virtual servers associated with the VIP address:'
      - '* If you set RHI STATE to C(PASSIVE) on all virtual servers, the Citrix ADC
        always advertises the route for the VIP address.'
      - '* If you set RHI STATE to C(ACTIVE) on all virtual servers, the Citrix ADC
        advertises the route for the VIP address if at least one of the associated
        virtual servers is in UP state.'
      - '* If you set RHI STATE to C(ACTIVE) on some and C(PASSIVE) on others, the
        Citrix ADC advertises the route for the VIP address if at least one of the
        associated virtual servers, whose RHI STATE set to C(ACTIVE), is in UP state.'
    type: str
    default: PASSIVE
  rtspnat:
    choices:
      - 'ON'
      - 'OFF'
    description:
      - Use network address translation (NAT) for RTSP data connections.
    type: str
    default: 'OFF'
  rule:
    description:
      - Expression, or name of a named expression, against which traffic is evaluated.
      - 'The following requirements apply only to the Citrix ADC CLI:'
      - '* If the expression includes one or more spaces, enclose the entire expression
        in double quotation marks.'
      - '* If the expression itself includes double quotation marks, escape the quotations
        by using the \ character. '
      - '* Alternatively, you can use single quotation marks to enclose the rule,
        in which case you do not have to escape the double quotation marks.'
    type: str
    default: '"none"'
  servicename:
    description:
      - Service to bind to the virtual server.
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
      - DTLS
      - NNTP
      - DNS
      - DHCPRA
      - ANY
      - SIP_UDP
      - SIP_TCP
      - SIP_SSL
      - DNS_TCP
      - RTSP
      - PUSH
      - SSL_PUSH
      - RADIUS
      - RDP
      - MYSQL
      - MSSQL
      - DIAMETER
      - SSL_DIAMETER
      - TFTP
      - ORACLE
      - SMPP
      - SYSLOGTCP
      - SYSLOGUDP
      - FIX
      - SSL_FIX
      - PROXY
      - USER_TCP
      - USER_SSL_TCP
      - QUIC
      - IPFIX
      - LOGSTREAM
      - MONGO
      - MONGO_TLS
      - MQTT
      - MQTT_TLS
      - QUIC_BRIDGE
      - HTTP_QUIC
    description:
      - Protocol used by the service (also called the service type).
    type: str
  sessionless:
    choices:
      - ENABLED
      - DISABLED
    description:
      - Perform load balancing on a per-packet basis, without establishing sessions.
        Recommended for load balancing of intrusion detection system (IDS) servers
        and scenarios involving direct server return (DSR), where session information
        is unnecessary.
    type: str
    default: DISABLED
  skippersistency:
    choices:
      - Bypass
      - ReLb
      - None
    description:
      - This argument decides the behavior incase the service which is selected from
        an existing persistence session has reached threshold.
    type: str
    default: None
  sobackupaction:
    choices:
      - DROP
      - ACCEPT
      - REDIRECT
    description:
      - Action to be performed if spillover is to take effect, but no backup chain
        to spillover is usable or exists
    type: str
  somethod:
    choices:
      - CONNECTION
      - DYNAMICCONNECTION
      - BANDWIDTH
      - HEALTH
      - NONE
    description:
      - 'Type of threshold that, when exceeded, triggers spillover. Available settings
        function as follows:'
      - '* C(CONNECTION) - Spillover occurs when the number of client connections
        exceeds the threshold.'
      - '* C(DYNAMICCONNECTION) - Spillover occurs when the number of client connections
        at the virtual server exceeds the sum of the maximum client (Max Clients)
        settings for bound services. Do not specify a spillover threshold for this
        setting, because the threshold is implied by the Max Clients settings of bound
        services.'
      - '* C(BANDWIDTH) - Spillover occurs when the bandwidth consumed by the virtual
        server''s incoming and outgoing traffic exceeds the threshold. '
      - '* C(HEALTH) - Spillover occurs when the percentage of weights of the services
        that are UP drops below the threshold. For example, if services svc1, svc2,
        and svc3 are bound to a virtual server, with weights 1, 2, and 3, and the
        spillover threshold is 50%, spillover occurs if svc1 and svc3 or svc2 and
        svc3 transition to DOWN. '
      - '* C(NONE) - Spillover does not occur.'
    type: str
  sopersistence:
    choices:
      - ENABLED
      - DISABLED
    description:
      - If spillover occurs, maintain source IP address based persistence for both
        primary and backup virtual servers.
    type: str
    default: DISABLED
  sopersistencetimeout:
    description:
      - Timeout for spillover persistence, in minutes.
    type: float
    default: 2
  sothreshold:
    description:
      - Threshold at which spillover occurs. Specify an integer for the CONNECTION
        spillover method, a bandwidth value in kilobits per second for the BANDWIDTH
        method (do not enter the units), or a percentage for the HEALTH method (do
        not enter the percentage symbol).
    type: float
  state:
    choices:
      - ENABLED
      - DISABLED
    description:
      - State of the load balancing virtual server.
    type: str
    default: ENABLED
  tcpprobeport:
    description:
      - Port number for external TCP probe. NetScaler provides support for external
        TCP health check of the vserver status over the selected port. This option
        is only supported for vservers assigned with an IPAddress or ipset.
    type: int
  tcpprofilename:
    description:
      - Name of the TCP profile whose settings are to be applied to the virtual server.
    type: str
  td:
    description:
      - Integer value that uniquely identifies the traffic domain in which you want
        to configure the entity. If you do not specify an ID, the entity becomes part
        of the default traffic domain, which has an ID of 0.
    type: float
  timeout:
    description:
      - Time period for which a persistence session is in effect.
    type: float
    default: 2
  toggleorder:
    choices:
      - ASCENDING
      - DESCENDING
    description:
      - Configure this option to toggle order preference
    type: str
    default: ASCENDING
  tosid:
    description:
      - TOS ID of the virtual server. Applicable only when the load balancing redirection
        mode is set to TOS.
    type: float
  trofspersistence:
    choices:
      - ENABLED
      - DISABLED
    description:
      - When value is C(ENABLED), Trofs persistence is honored. When value is C(DISABLED),
        Trofs persistence is not honored.
    type: str
    default: ENABLED
  v6netmasklen:
    description:
      - Number of bits to consider in an IPv6 destination or source IP address, for
        creating the hash that is required by the DESTINATIONIPHASH and SOURCEIPHASH
        load balancing methods.
    type: float
    default: 128
  v6persistmasklen:
    description:
      - Persistence mask for IP based persistence types, for IPv6 virtual servers.
    type: float
    default: 128
  vipheader:
    description:
      - Name for the inserted header. The default name is vip-header.
    type: str
  weight:
    description:
      - Weight to assign to the specified service.
    type: float
  lbvserver_analyticsprofile_binding:
    type: dict
    description: Bindings for lbvserver_analyticsprofile_binding resource
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
  lbvserver_appflowpolicy_binding:
    type: dict
    description: Bindings for lbvserver_appflowpolicy_binding resource
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
  lbvserver_appfwpolicy_binding:
    type: dict
    description: Bindings for lbvserver_appfwpolicy_binding resource
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
  lbvserver_appqoepolicy_binding:
    type: dict
    description: Bindings for lbvserver_appqoepolicy_binding resource
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
  lbvserver_auditnslogpolicy_binding:
    type: dict
    description: Bindings for lbvserver_auditnslogpolicy_binding resource
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
  lbvserver_auditsyslogpolicy_binding:
    type: dict
    description: Bindings for lbvserver_auditsyslogpolicy_binding resource
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
  lbvserver_authorizationpolicy_binding:
    type: dict
    description: Bindings for lbvserver_authorizationpolicy_binding resource
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
  lbvserver_botpolicy_binding:
    type: dict
    description: Bindings for lbvserver_botpolicy_binding resource
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
  lbvserver_cachepolicy_binding:
    type: dict
    description: Bindings for lbvserver_cachepolicy_binding resource
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
  lbvserver_cmppolicy_binding:
    type: dict
    description: Bindings for lbvserver_cmppolicy_binding resource
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
  lbvserver_contentinspectionpolicy_binding:
    type: dict
    description: Bindings for lbvserver_contentinspectionpolicy_binding resource
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
  lbvserver_dnspolicy64_binding:
    type: dict
    description: Bindings for lbvserver_dnspolicy64_binding resource
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
  lbvserver_feopolicy_binding:
    type: dict
    description: Bindings for lbvserver_feopolicy_binding resource
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
  lbvserver_lbpolicy_binding:
    type: dict
    description: Bindings for lbvserver_lbpolicy_binding resource
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
  lbvserver_responderpolicy_binding:
    type: dict
    description: Bindings for lbvserver_responderpolicy_binding resource
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
  lbvserver_rewritepolicy_binding:
    type: dict
    description: Bindings for lbvserver_rewritepolicy_binding resource
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
  lbvserver_service_binding:
    type: dict
    description: Bindings for lbvserver_service_binding resource
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
  lbvserver_servicegroup_binding:
    type: dict
    description: Bindings for lbvserver_servicegroup_binding resource
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
  lbvserver_spilloverpolicy_binding:
    type: dict
    description: Bindings for lbvserver_spilloverpolicy_binding resource
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
  lbvserver_tmtrafficpolicy_binding:
    type: dict
    description: Bindings for lbvserver_tmtrafficpolicy_binding resource
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
  lbvserver_transformpolicy_binding:
    type: dict
    description: Bindings for lbvserver_transformpolicy_binding resource
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
  lbvserver_videooptimizationdetectionpolicy_binding:
    type: dict
    description: Bindings for lbvserver_videooptimizationdetectionpolicy_binding resource
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
  lbvserver_videooptimizationpacingpolicy_binding:
    type: dict
    description: Bindings for lbvserver_videooptimizationpacingpolicy_binding resource
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
