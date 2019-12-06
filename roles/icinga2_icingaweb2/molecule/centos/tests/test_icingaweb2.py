import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_icingaweb(host):
    """ test icingaweb installation """
    with host.sudo():

        res = host.file('/etc/icingaweb2/resources.ini')
        assert res.exists
        assert res.user == 'apache'
        assert res.group == 'icingaweb2'
        assert res.contains('dbname = "icingaweb"')
        assert res.contains('username = "icingaweb"')
        assert res.contains('password = "webdbpass"')

        groups = host.file('/etc/icingaweb2/roles.ini')
        assert groups.contains('[Testrole]')
        assert groups.contains('groups = "Testgroup"')
        assert groups.contains(r'permissions = "module/grafana, module/monitoring, monitoring/command/schedule-check, monitoring/command/acknowledge-problem, monitoring/command/remove-acknowledgement, monitoring/command/comment/\*, monitoring/command/comment/add, monitoring/command/downtime/\*, monitoring/command/downtime/schedule, monitoring/command/downtime/delete"')
        assert groups.contains(r'monitoring/filter/objects = "(host_name=\*test\*|host_name=test\*)"')

        curl = host.run('curl http://localhost/icingaweb2/ --head')
        assert 'Location: /icingaweb2/authentication/login' in curl.stdout
