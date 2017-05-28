Ansible Role: lldpad
====================

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-lldpad.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-lldpad)

Installs the lldpad package, which provides the userspace daemong and
configuration tool for the Link Layer Discover Protocol (LLDP) agent.
Supported and tested on EL6 and EL7.

Requirements
------------

Useful on physical hosts for determining uplink switch/switchport connections.

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
         - giovtorres.lldpad
           when: ansible_virtualization_role == "host"

License
-------

BSD
