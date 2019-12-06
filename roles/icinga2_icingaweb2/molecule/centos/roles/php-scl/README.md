# Ansible Role: php-scl

Install PHP(-fpm) from Red Hat Software Collections.

## Requirements

Currently the role only supports Apache httpd and a httpd with base config is
required. Configure this with the httpd role.

## Role Variables

Role variables are documented inline in the following files:
- Required variables in meta/main.yml
- Optional variables in defaults/main.yml
- Constants in vars/main.yml

Any variables that are read from other roles and/or the global scope
(ie. hostvars, group vars, etc.) should be mentioned here.

## Dependencies

Any dependencies (other roles, custom plugins) should be listed here,
organized by category (roles, modules, filters, tests, ...).

## Examples

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - role: php-scl

## Tags

No tags.

## License

MIT

## Further Reading


## Author Information

Luc Stroobant
