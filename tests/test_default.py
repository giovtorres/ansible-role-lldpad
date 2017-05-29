import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_lldpad_service(Service):
    s = Service("lldpad")
    assert s.is_enabled
    assert s.is_running


def test_lldpad_adminstatus(Command, Sudo):
    cmd = "/usr/sbin/lldptool get-lldp -i eth0 adminStatus"
    with Sudo():
        assert Command.run_expect([0], cmd)
        assert "adminStatus=rxtx" in Command.check_output(cmd)


@pytest.mark.parametrize("tlvid", ["sysName", "portDesc"])
def test_lldpad_get_tlvs(Command, Sudo, tlvid):
    cmd = "/usr/sbin/lldptool get-tlv -i eth0 -c enableTx -V " + tlvid
    with Sudo():
        assert Command.run_expect([0], cmd)
        assert "enableTx=yes" in Command.check_output(cmd)
