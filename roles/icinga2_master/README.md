[![Build Status](https://travis-ci.com/fiaasco/icinga2-master.svg?branch=master)](https://travis-ci.com/fiaasco/icinga2-master)

# Ansible Role: icinga2-master

This role installs an Icinga2 master server.
The role currently supports CentOS (and RHEL), Debian and Ubuntu.

## Requirements

The server needs a MySQL or MariaDB database.

## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml


## Dependencies

None

## Examples

    - hosts: servers
      roles:
         - role: icinga2-master

## Tags

No tags available.

## License

MIT

## Further Reading

* (Icinga2 documentation)[https://icinga.com/docs/]

## Author Information

Luc Stroobant
