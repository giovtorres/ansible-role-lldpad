Ansible Role: lldpad
====================

Installs and starts the Link Layer Discover Protocol (LLDP) agent daemon
(lldpad).  Supported and tested on EL6 and EL7.

Requirements
------------

None.

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
