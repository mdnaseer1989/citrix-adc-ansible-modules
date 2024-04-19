# `netscaler.adc` collection playbook anatomy


## Anatomy of a playbook

This is how a typical playbook for `netscaler.adc` collection looks like:

```yaml
- name: Name of the playbook
  hosts: demo_netscalers

  gather_facts: false # Since the module runs on localhost, we don't need to gather facts

  module_defaults: # If we are using `module_defaults`, then these common arguments (`nsip`, `nitro_user`, etc) can be skipped from the tasks below.
    group/netscaler.adc.default_args:
      nsip: 10.10.10.10
      nitro_user: nsroot
      nitro_pass: verysecretpassword
      nitro_protocol: http
      validate_certs: false
      save_config: false
      netscaler_console_as_proxy_server: true
      managed_netscaler_instance_name: my_instance
      managed_netscaler_instance_id: 1234
      managed_netscaler_instance_ip: 1.1.1.1
      managed_netscaler_instance_username: my_user
      managed_netscaler_instance_password: my_password

  tasks:
    - name: Name of the task
      delegate_to: localhost # Since the module runs on localhost, we need to delegate the task to localhost
      netscaler.adc.service: # Name of the module. We recommend to use the fully qualified name of the module
        # The following are the NITRO authentication parameters. Refer to the module documentation for the list of supported parameters.
        nsip: 10.0.0.1 # This can also be given via NETSCALER_NSIP environment variable
        nitro_user: nitrouser # This can also be given via NETSCALER_NITRO_USER environment variable
        nitro_pass: verysecretpassword # This can also be given via NETSCALER_NITRO_PASS environment variable
        # nitro_auth_token: "098765456789098765456789"
        nitro_protocol: https # This can also be given via NETSCALER_NITRO_PROTOCOL environment variable
        validate_certs: false # This can also be given via NETSCALER_VALIDATE_CERTS environment variable

        # NetScaler Console as an API Proxy Server. This is optional. Default is false.
        # Refer: https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software/current-release/adm-as-api-proxy-server.html
        netscaler_console_as_proxy_server: true # This can also be given via NETSCALER_CONSOLE_AS_PROXY_SERVER environment variable
        # When you want NetScaler Console to forward a request to a managed netscaler instance, add ANY ONE of the below parameters.
        managed_netscaler_instance_name: my_instance # This can also be given via NETSCALER_MANAGED_NETSCALER_INSTANCE_NAME environment variable
        managed_netscaler_instance_id: 1234 # This can also be given via NETSCALER_MANAGED_NETSCALER_INSTANCE_ID environment variable
        managed_netscaler_instance_ip: 1.1.1.1 # This can also be given via NETSCALER_MANAGED_NETSCALER_INSTANCE_IP environment variable
        # In Settings > Administration > System Configurations > Basic Settings, if you select Prompt Credentials for Instance Login, ensure to configure user name and password of a managed instance. Alternatively, you can also specify the instance session ID.
        managed_netscaler_instance_username: my_user # This can also be given via NETSCALER_MANAGED_NETSCALER_INSTANCE_USERNAME environment variable
        managed_netscaler_instance_password: my_password # This can also be given via NETSCALER_MANAGED_NETSCALER_INSTANCE_PASSWORD environment variable

        # Should the module save the config after making the changes. This is optional. Default is false.
        save_config: false # This can also be given via NETSCALER_SAVE_CONFIG environment variable

        state: present # This is the desired state of the resource. The module will make sure that the resource is in this state. Valid values are `present`, `absent`, `enabled`, `disabled`, `imported`, `unset`, `created`, `flushed`, `switched`. However, not all modules support all the states. Refer to the module documentation for the supported states.

        # The following are the module parameters. Refer to the module documentation for the list of supported parameters.
        name: s1
        ipaddress: 10.10.10.10
        servicetype: HTTP
        port: 80
```

## Nitro authentication parameters

- `nitro_user` and `nitro_pass` should be given together. If one of them is missing, the module will try to read the value from the environment variable `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS` respectively. If the environment variable is not set, the module will fail.
- `nitro_auth_token` is optional. If it is not given, the module will try to read the value from the environment variable `NETSCALER_NITRO_AUTH_TOKEN`. If the environment variable is not set, the module will try to authenticate using `nitro_user` and `nitro_pass`. If `nitro_user` and `nitro_pass` are also not given, the module will fail.
- `nitro_protocol` is optional. If it is not given, the module will try to read the value from the environment variable `NETSCALER_NITRO_PROTOCOL`. If the environment variable is not set, the module will use `https`.
- `validate_certs` is optional. If it is not given, the module will try to read the value from the environment variable `NETSCALER_VALIDATE_CERTS`. If the environment variable is not set, the module will use `true`.
- `nsip` is required. If it is not given, the module will try to read the value from the environment variable `NETSCALER_NSIP`. If the environment variable is not set, the module will fail.
- `module_defaults`: Refer [`netscaler.adc.module_defaults` group](https://github.com/netscaler/ansible-collection-netscaleradc/tree/main?tab=readme-ov-file#using-netscaleradcmodule_defaults-group) for more details

## NetScaler Console as an API Proxy Server

- `netscaler_console_as_proxy_server`: This is optional. Default is `false`. Refer [NetScaler Console as an API Proxy Server](https://docs.netscaler.com/en-us/netscaler-application-delivery-management-software/current-release/adm-as-api-proxy-server.html) for more details.
- `managed_netscaler_instance_name`, `managed_netscaler_instance_id`, `managed_netscaler_instance_ip`: When you want NetScaler Console to forward a request to a managed netscaler instance, add ANY ONE of these parameters.
- `managed_netscaler_instance_username`, `managed_netscaler_instance_password`: In **Settings > Administration > System Configurations > Basic Settings**, if you select **Prompt Credentials for Instance Login**, ensure to configure username and password of a managed instance.

## State parameter

- `state`: Refer [modes of operation](https://github.com/netscaler/ansible-collection-netscaleradc/blob/main/features_v2.md#modes-of-operation-state-option-in-the-module-task) for more details

## Module parameters

Click on the resource in [the supported module matrix table](./supported_modules_matrix.md#matrix) for the module parameters.
