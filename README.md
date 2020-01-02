[![Build Status](https://travis-ci.com/fiaasco/icinga2.svg?branch=master)](https://travis-ci.com/fiaasco/icinga2)

# Ansible Collection - fiaasco.icinga2

This is a role collection for the complete management of Icinga2 master and clients.
A brief overview of the included roles:

* icinga2\_master: install and configure an Icinga2 master server
* icinga2\_icingaweb2: install and configure Icingaweb2
* icinga2\_checks: configures Icinga2 checks on the master server
* icinga2\_client: installs Icinga2 and configures it as a client
* icinga2\_hostconfig: puts the configuration of a monitored host on the Icinga2 master
* monitoring\_plugins: installs the monitoring "Nagios" plugins (used on both clients and master)

The collection is tested against different versions of Debian, Ubuntu and CentOS.

## Requirements

Deployment of the Icinga2 master server with Icingaweb 2 requires a LAMP stack with PHP >= 5.6.0. The LAMP stack is configured with the prepare-master.yml playbook and it's only supported on recent releases of the tested distro's in this collection:
* Debian 10
* Ubuntu 18.04
* CentOS 8

The master and Icingaweb can be deployed on older distro's too (eg CentOS 7 with php-scl), but you'll have to setup the LAMP stack with other roles in that case.

## Usage

All system roles are configured based on the Ansible inventory groups. An [example inventory is included in the molecule tests](https://github.com/fiaasco/icinga2/blob/master/molecule/default/molecule.yml). The minimum required variables are also listed in this inventory, make sure to change the ticketsalt and passwords. Other available variables are document in the role defaults.

Run the playbooks:

Configure the master first
* ansible-galaxy install -r requirements.yml (only required if you want to use the prepare-master playbook)
* prepare-master.yml
* icinga2-master.yml

A satellite is a special type of client that allows other clients to connect to it and send the results to the master. Make sure to configure satellites before the connected clients or the setup won't be able to complete:
* icinga2-satellite.yml

Afterwards, configure the normal clients:
* icinga2-client.yml


## License

MIT

## Further Reading

* [Icinga2 documentation](https://icinga.com/docs/)
