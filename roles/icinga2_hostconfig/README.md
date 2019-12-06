# Ansible Role: icinga2/hostconfig

This is an Icinga helper role that configures:
* the hostconfig for both the master and client.
* the Icinga groups file based on the Ansible inventory groups.

## Requirements

You need a configured Icinga master and clients to be able to use this role.


## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies



## Examples

Include the role in your playbook to have an installed client configured on the master:

```
    - hosts: servers
      roles:
         - role: icinga2-client
         - role: icinga2-hostconfig
```

## Tags

No tags available.

## License

MIT

## Further Reading

* (Icinga2 documentation)[https://icinga.com/docs/icinga2/latest/]

## Author Information

Luc Stroobant
