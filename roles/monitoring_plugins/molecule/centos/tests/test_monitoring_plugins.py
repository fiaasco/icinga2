import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['nagios-common', 'nagios-plugins', 'nagios-plugins-by_ssh', 'nagios-plugins-cluster', 'nagios-plugins-dhcp', 'nagios-plugins-dig', 'nagios-plugins-disk', 'nagios-plugins-dns', 'nagios-plugins-dummy', 'nagios-plugins-file_age', 'nagios-plugins-http', 'nagios-plugins-icmp', 'nagios-plugins-ldap', 'nagios-plugins-load', 'nagios-plugins-log', 'nagios-plugins-mailq', 'nagios-plugins-mysql', 'nagios-plugins-nrpe', 'nagios-plugins-nt', 'nagios-plugins-ntp', 'nagios-plugins-oracle', 'nagios-plugins-perl', 'nagios-plugins-pgsql', 'nagios-plugins-ping', 'nagios-plugins-procs', 'nagios-plugins-smtp', 'nagios-plugins-snmp', 'nagios-plugins-ssh', 'nagios-plugins-swap', 'nagios-plugins-tcp', 'nagios-plugins-time', 'nagios-plugins-users'])
def test_monitoring_plugins(host, pkg):
    """ check if packages are install
    """
    assert host.package(pkg).is_installed


def test_event_handler(host):
    with host.sudo():
        eventhandler = host.file("/usr/lib64/nagios/plugins/eventhandlers/restart_service")
        assert eventhandler.exists
        assert eventhandler.mode == 0o775
        assert eventhandler.user == 'root'
        assert eventhandler.group == 'root'

        sudoers = host.file("/etc/sudoers.d/icinga")
        assert sudoers.user == 'root'
        assert sudoers.group == 'root'
        assert sudoers.mode == 0o440
        assert sudoers.contains('icinga ALL=(ALL) NOPASSWD:')
