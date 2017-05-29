import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_lldpad_service(host):
    s = host.service("lldpad")
    assert s.is_enabled
    assert s.is_running


def test_lldpad_adminstatus(host):
    cmd = "/usr/sbin/lldptool get-lldp -i eth0 adminStatus"
    with host.sudo():
        assert host.run_expect([0], cmd)
        assert "adminStatus=rxtx" in host.check_output(cmd)


@pytest.mark.parametrize("tlvid", ["sysName", "portDesc"])
def test_lldpad_get_tlvs(host, tlvid):
    cmd = "/usr/sbin/lldptool get-tlv -i eth0 -c enableTx -V " + tlvid
    with host.sudo():
        assert host.run_expect([0], cmd)
        assert "enableTx=yes" in host.check_output(cmd)
