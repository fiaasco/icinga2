# Ansible Role: monitoring-plugins

This role installs the monitoring (aka Nagios) plugins on a host.
The role currently supports CentOS, Redhat, Debian and Ubuntu.

## Requirements


## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml

## Dependencies

None

## Examples

Use the role in your playbook:

    - hosts: servers
      roles:
         - role: monitoring-plugins

## Tags

No tags available.

## License

* Ansible role: MIT
* check\_systemd\_service: no license in project, (original author patrikskrivanek)[https://github.com/patrikskrivanek/icinga2-check_systemd_service]



## Further Reading

* (The monitoring plugins project)[https://www.monitoring-plugins.org/]

## Author Information

Luc Stroobant
