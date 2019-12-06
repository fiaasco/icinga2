import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('client')


def test_client(host):
    """ Verify config is not created on client """

    with host.sudo():

        zone = host.file('/etc/icinga2/zones.d/master/')
        assert not zone.exists
