import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icingaweb2')


@pytest.mark.parametrize('package', ['icingaweb2', 'icingaweb2-common'])
def test_icingaweb2_packages(host, package):
    with host.sudo():
        # Check if package is installed
        pkg = host.package(package)
        assert pkg.is_installed


@pytest.mark.parametrize('config', ['roles', 'resources', 'authentication', 'groups', 'config'])
def test_icingaweb2_config(host, config):
    with host.sudo():
        # Check if configfile is present
        file = host.file('/etc/icingaweb2/%s.ini' % config)
        assert file.exists
        assert file.user == 'apache'
        assert file.group == 'icingaweb2'
        assert file.mode == 0o660


def test_icingaweb2_config_roles(host):
    with host.sudo():
        # Check if roles.ini is configured
        file = host.file('/etc/icingaweb2/roles.ini')
        assert file.exists
        assert file.user == 'apache'
        assert file.group == 'icingaweb2'
        assert file.mode == 0o660
        assert file.contains('module/grafana')
