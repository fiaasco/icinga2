[![Build Status](https://travis-ci.com/fiaasco/icinga2-client.svg?branch=master)](https://travis-ci.com/fiaasco/icinga2-client)

# Ansible Role: icinga2-client

This role installs Icinga in satellite and client mode. (An Icinga satellite is an instance that serves as a monitoring proxy for other clients)
The role currently supports CentOS, RHEL, Debian and Ubuntu.

## Requirements

You need a running Icinga master server to be able to complete the client installation.
Monitoring plugins (monitoring-plugins)[https://github.com/stroobl/monitoring-plugins] installation is required on the client to execute most checks.


## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies



## Examples

Include the role in your playbook:

```
    - hosts: servers
      roles:
         - role: icinga2-client
```

**WARNING: it's NOT supported to rename a zone from an existing client with this role.
(This was not implemented due to some old open Icinga bugs where the removal of the initial zone name in the synced configuration fails, this breaks the remote instance.)**

## Tags

No tags available.

## License

MIT

## Further Reading

* (Icinga2 documentation)[https://icinga.com/docs/icinga2/latest/]

## Author Information

Luc Stroobant
