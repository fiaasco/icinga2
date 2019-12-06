import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icinga2master')


def test_hostconfig_files(host):
    """ Check if configuration files exist on master """

    with host.sudo():

        master = host.file('/etc/icinga2/zones.d/master/debian-icinga2-hostconfig-master.conf')
        assert master.exists
        assert 'vars.icinga_zone = "master"' in master.content

        client = host.file('/etc/icinga2/zones.d/master/.debian-icinga2-hostconfig-client.conf')
        assert client.exists
        assert 'icinga2-hostconfig-client"' in client.content
        assert 'parent = "master"' in client.content
