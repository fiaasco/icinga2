# Ansible Role: icingaweb2

This role deploys Icingaweb2 and configures it.
Icingaweb is supposed to be running on the Icinga master server. The role will configure the icingaadmin user with the same password as used for the Icinga master server.

## Requirements

Icingaweb requires:
* a LAMP stack to be configured and running (Icingaweb requires at least php 7.1).
* the Icinga master service configured and running.

## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies


## Examples

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: icinga2master
      roles:
         - role: icingaweb2

## Tags

No tags.

## License

MIT

## Further Reading

* [Icinga web2 installation](https://icinga.com/docs/icingaweb2/latest/doc/02-Installation/)

## Author Information

Luc Stroobant
