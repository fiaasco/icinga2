# Ansible Collection - fiaasco.icinga2

This is a role collection for the complete management of Icinga2.
A brief overview of the included roles:

* icinga2\_master: install and configure an Icinga2 master server
* icinga2\_icingaweb2: install and configure Icingaweb2
* icinga2\_checks: configures Icinga2 checks on the master server
* icinga2\_client: installs Icinga2 and configures it as a client
* icinga2\_hostconfig: puts the configuration of a monitored host on the Icinga2 master
* monitoring\_plugins: installs the monitoring "Nagios" plugins (used on both clients and master)

## Requirements

The Icinga2 master needs a database if you want to enable idodb.
Icingaweb2 needs a full LAMP stack. In the included playbook Icingaweb2 is deployed on the master server and it's using fiaasco roles listed in galaxy.yml to setup the LAMP stack on Debian. Other options to create the LAMP stack are obviously possible.

## License

MIT

## Further Reading

* (Icinga2 documentation)[https://icinga.com/docs/]
