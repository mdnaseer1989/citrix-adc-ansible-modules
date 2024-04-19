# NetScaler Ansible Collection `version2` - netscaler.adc

[![ansible-lint](https://github.com/netscaler/ansible-collection-netscaleradc/actions/workflows/lint.yml/badge.svg)](https://github.com/netscaler/ansible-collection-netscaleradc/actions)
[![ansible-test](https://github.com/netscaler/ansible-collection-netscaleradc/actions/workflows/test.yml/badge.svg)](https://github.com/netscaler/ansible-collection-netscaleradc/actions)
[![collection-release](https://github.com/netscaler/ansible-collection-netscaleradc/actions/workflows/release.yml/badge.svg)](https://github.com/netscaler/ansible-collection-netscaleradc/actions)
[![ah-token-refresh](https://github.com/netscaler/ansible-collection-netscaleradc/actions/workflows/ah_token_refresh.yml/badge.svg)](https://github.com/netscaler/ansible-collection-netscaleradc/actions)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/netscaler/ansible-collection-netscaleradc/badge)](https://securityscorecards.dev/viewer/?uri=github.com/netscaler/ansible-collection-netscaleradc)

> ⚠️ Note:
> The earlier `citrix.adc` ansible collection is replaced with the new `netscaler.adc` ansible collection.

> The `citrix.adc` ansible collection is backed up by a separate branch [citrix.adc](https://github.com/netscaler/ansible-collection-netscaleradc/tree/citrix.adc)


## Vision

The vision of the `netscaler.adc` collection is to provide a complete declarative interface to configure and manage NetScaler ADC.

If you need any feature or flexibility that is not available in the collection at the moment, please raise issues/enhancement-requests/recommendations at <https://github.com/netscaler/ansible-collection-netscaleradc/issues>

> :envelope: For any immediate issues or help , reach out to us at <NetScaler-AutomationToolkit@cloud.com> !

## About `version1` and `version2` of the collection

We refer the earlier `citrix.adc` ansible collection as `version1` and the new `netscaler.adc` as `version2`.

This is the `version2` of the NetScaler Ansible Collection. It is a complete rewrite of the collection. The collection is not backward compatible with the `version1` of the collection.

`citrix.adc` collection will be deprecated soon and will not be maintained further. It is recommended to migrate to the `netscaler.adc` collection.

## About the `netscaler.adc` collection (version2)

The collection provides Ansible modules to configure and manage NetScaler ADC appliances. The modules are written using the NITRO API. The modules are idempotent and can be used to configure the NetScaler ADC appliances in declarative manner.

## Installation

### ansible-galaxy

```bash
ansible-galaxy collection install netscaler.adc
```

### via github (to have the latest updated which are yet to be released in ansible-galaxy)


```bash
ansible-galaxy collection install "git+https://github.com/netscaler/ansible-collection-netscaleradc.git" [--force]
```

> `--force` option is required if you have already installed the collection via ansible-galaxy. This will overwrite the existing collection with the latest collection from github.

### Verify the installation

```bash
ansible-galaxy collection list netscaler.adc
```

The above command should display the following output:

```text

# /Users/netscaleruser/.ansible/collections/ansible_collections
Collection    Version
------------- -------
netscaler.adc 2.0.x
```

## Collection Modules Documentation

<https://netscaler.github.io/ansible-collection-netscaleradc/>

> You can also click on the desired module name in the [supported_modules_matrix.md](supported_modules_matrix.md) file to go to the specific module documentation

## Examples

Refer to the [examples](examples) directory for the sample playbooks.

Also refer [playbook_anatomy.md](playbook_anatomy.md) for the anatomy of a playbook.

## :key: Authentication

### Authenticate to NetScaler via username and password

Every module in the collection requires the user to authenticate to the NetScaler ADC appliance. The authentication can be done using the `nitro_user` and `nitro_pass` parameters. These parameters can also be passed as environment variables `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`.

Refer to the [playbook_anatomy.md](playbook_anatomy.md) and [examples](examples) directory for the sample playbooks.

### Authenticate to NetScaler

#### Password based authentication

Every task in the collection requires the user to authenticate to the NetScaler ADC appliance. The authentication can be done using the `nsip`, `nitro_user` and `nitro_pass` parameters. These parameters can also be passed as environment variables `NETSCALER_NSIP`, `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`.

#### Using `netscaler.adc.module_defaults` group

To avoid having to specify common parameters for all the modules in every task, you can use the `netscaler.adc.module_defaults` [module defaults](https://docs.ansible.com/ansible/devel/playbook_guide/playbooks_module_defaults.html#module-defaults-groups) group:

> Refer [examples/module_default_args_action_group.yaml](./examples/module_default_args_action_group.yaml) for an example playbook.

#### Passwordless via `nitro_auth_token` parameter (SESSIONID based authentication)

The collection also supports authentication to NetScaler ADC appliance via token. The token can be generated using the `login` module. The token can be passed to other modules using the `nitro_auth_token` parameter. The `nitro_token` parameter can also be passed as environment variable `NETSCALER_NITRO_AUTH_TOKEN`.

Refer to the [playbook_anatomy.md](playbook_anatomy.md) and [sessionid_based_authentication_via_login_logout.yaml](examples/sessionid_based_authentication_via_login_logout.yaml) example playbook.

> `login` module requres `username` and `password` parameters to be passed. If you do not wish to pass the username and password, refer below.

You can use the below `curl` command to generate the token. The token can be passed to other modules using the `nitro_auth_token` parameter. The `nitro_auth_token` parameter can also be passed as environment variable `NETSCALER_NITRO_AUTH_TOKEN`. The token is valid for 60 minutes.

The below command also uses `jq` to parse the JSON output and store the `sessionid` in the `NETSCALER_NITRO_AUTH_TOKEN` environment variable, so that it can be used by other modules.

> change the `NETSCALER_NSIP`, `NETSCALER_NITRO_USER` and `NETSCALER_NITRO_PASS`

> Install `jq` util if not already installed.

```bash
export NETSCALER_NITRO_AUTH_TOKEN=$(curl -X POST -H "Content-Type:application/json" --insecure --silent https://NETSCALER_NSIP/nitro/v1/config/login -d '{"login":{"username":"NETSCALER_NITRO_USER", "password":"NETSCALER_NITRO_PASS"}}' | jq .sessionid)
echo $NETSCALER_NITRO_AUTH_TOKEN
```

## NetScaler Console (ADM) as a Proxy Server

Refer to the [NetScaler ADM as an API proxy server](https://docs.netscaler.com/en-us/citrix-application-delivery-management-software/current-release/adm-as-api-proxy-server.html) for more details.

The collection supports configuring NetScaler Console as a proxy server. This is useful when you have multiple NetScaler ADC appliances and you want to manage them using a single NetScaler Console.

An example can be found in [examples/netscaler_console_as_proxy_server.yaml](examples/netscaler_console_as_proxy_server.yaml)

Also, refer to the [playbook_anatomy.md](playbook_anatomy.md#netscaler-console-as-an-api-proxy-server) for more details.

### Steps to configure NetScaler Console as a proxy server

1. Login to NetScaler Console and get the session ID
2. Use the session ID in the subsequent tasks to configure the managed NetScalers via the NetScaler Console as a proxy server
3. Logout from the NetScaler Console (optional)

## Supported Ansible Versions

This collection is tested for Ansible version 2.14 and above.

> Please raise issues at <https://github.com/netscaler/ansible-collection-netscaleradc/issues> if you face any issues with the collection.

## Features of `netscaler.adc` collection

Refer to the [features_v2.md](features_v2.md) file for the features of the `netscaler.adc` collection.

## Migrating from `citrix.adc` collection to `netscaler.adc` collection

> Both `citrix.adc` and `netscaler.adc` can be used in the same Ansible playbook. However, it is recommended to migrate to `netscaler.adc` collection.

Refer to the [migrating_from_v1_v2.md](migrating_from_v1_v2.md) file for the migration steps.

## Supported Modules in `netscaler.adc` collection

Refer to the [supported_modules_matrix.md](supported_modules_matrix.md) file for the list of supported modules in `netscaler.adc` collection.

## Todo list for `netscaler.adc` collection

- [x] Support for `nitro_auth_token` parameter in all modules.
- [x] Update supported matrix to have documentation links
- [x] Add appropriate license to the collection.
- [x] Upload the collection to Ansible Galaxy.
- [ ] Support configuring ADC with ADM as proxy. Refer to [NetScaler ADM as an API proxy server](https://docs.netscaler.com/en-us/citrix-application-delivery-management-software/current-release/adm-as-api-proxy-server.html) for more details.
- [ ] Implement SSH connection module
- [ ] Support for generic modules similar to `citrix.adc.nitro_request` and `citrix.adc.nitro_resource`?
- [ ] migration tool to convert `citrix.adc` playbooks (including generic `citrix.adc.nitro_request` and `citrix.adc.nitro_resource` modules) to `netscaler.adc` modules
- [ ] Add more examples
- [ ] Write a python script which converts examples/playbook.yaml to module's EXAMPLE documentation
- [ ] Test modules against all NetScaler ADC versions.
- [x] Test modules againsts ansible versions 2.9+
- [x] Configure GitHub Actions to automate the collection build and release process.
- [ ] Configure GitHub Actions to automate the collection testing process.
- [x] Configure GitHub Actions to automate the collection linting process.
- [x] Collect NetScaler info (version, etc) and store it in the `facts` dictionary
