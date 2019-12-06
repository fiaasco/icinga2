import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('pkg', ['monitoring-plugins', 'monitoring-plugins-basic', 'monitoring-plugins-common', 'monitoring-plugins-standard'])
def test_monitoring_plugins(host, pkg):
    """ check if packages are install
    """
    assert host.package(pkg).is_installed


def test_event_handler(host):
    with host.sudo():
        eventhandler = host.file("/usr/lib/nagios/plugins/eventhandlers/restart_service")
        assert eventhandler.exists
        assert eventhandler.mode == 0o775
        assert eventhandler.user == 'root'
        assert eventhandler.group == 'root'

        sudoers = host.file("/etc/sudoers.d/nagios")
        assert sudoers.user == 'root'
        assert sudoers.group == 'root'
        assert sudoers.mode == 0o440
        assert sudoers.contains('nagios ALL=(ALL) NOPASSWD:')
