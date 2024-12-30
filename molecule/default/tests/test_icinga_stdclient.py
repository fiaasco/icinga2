import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icinga2stdclient')


def test_std_client_config(host):
    """ basic configuration checks
    """
    with host.sudo():
        # Check if zone is configured
        file = host.file('/etc/icinga2/zones.conf')
        assert file.exists
        assert file.user == 'nagios'
        assert file.group == 'nagios'
        assert file.mode == 0o644
        assert file.contains('Generated by Icinga 2 node setup commands')

        # Generate cache file
        dump = host.run('icinga2 daemon -C --dump-objects')

        # Check if master endpoint is configured
        endpoints = host.run('icinga2 object list --type endpoint')
        assert "-icinga2-master' of type 'Endpoint':" in endpoints.stdout

        # Check if config from master is included
        zones = host.run('icinga2 object list --type zone')
        assert "Object 'global-templates' of type 'Zone'" in zones.stdout
        assert "Object 'director-global' of type 'Zone'" in zones.stdout
        assert "Object 'master' of type 'Zone'" in zones.stdout


def test_std_client_connection(host):
    """ Check if client is connected to icinga
    """
    with host.sudo():
        connections = list(host.socket('tcp://5665')._iter_sockets(False))
        # >>> print(connections)
        # [(u'tcp', u'10.244.3.219', 51716, u'10.244.5.174', 5665), (u'tcp', u'10.244.3.219', 22, u'10.244.4.0', 33686)]
        assert [x for x in connections if x[4] == 5665]
