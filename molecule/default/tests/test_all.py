import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package(host):
    """ check if packages are installed
    """
    assert host.package('icinga2').is_installed


def test_icinga_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('icinga2').is_enabled
    assert host.service('icinga2').is_running
