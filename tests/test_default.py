import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_lldpad_service(Service):
    s = Service("lldpad")
    assert s.is_enabled
    assert s.is_running
