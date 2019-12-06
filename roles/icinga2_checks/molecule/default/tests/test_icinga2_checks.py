import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_icinga_service(host):
    """ Testing whether the service is running and enabled
    """
    assert host.service('icinga2').is_enabled
    assert host.service('icinga2').is_running


@pytest.mark.parametrize('chk', ['checks/linux/mailq.conf',
                                 'checks/linux/chronyd.conf',
                                 'checks/linux/swap.conf',
                                 'checks/linux/ntpd.conf',
                                 'checks/linux/ssh.conf',
                                 'checks/linux/time.conf',
                                 'checks/linux/disk.conf',
                                 'checks/linux/load.conf',
                                 'checks/all/procs.conf',
                                 'checks/all/cluster-health.conf',
                                 'checks/all/users.conf',
                                 'checks/all/ping.conf',
                                 'checks/all/icinga.conf'
                                 ])
def test_icinga_checks(host, chk):
    """ Test if check files exist
    """
    assert host.file('/etc/icinga2/zones.d/global-templates/{0}'.format(chk)).exists
