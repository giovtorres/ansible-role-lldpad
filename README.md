Ansible Role: lldpad
====================

Installs the lldpad package, which provides the userspace daemong and
configuration tool for the Link Layer Discover Protocol (LLDP) agent.
Supported and tested on EL6 and EL7.

Requirements
------------

Useful on physical hosts to determining uplink switch/switchport connections.

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - ansible-role-lldpad
           when: ansible_virtualization_role == "host"

License
-------

BSD
