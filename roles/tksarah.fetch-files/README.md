fetch-files
=========

Ansible Role: fetch-file
------------

As executing the playbook, the role is copied from the target host in background and save it as a text file.
The role allows to get the list of specific files simply.

Install 
------------

```
# ansible-galaxy install --roles-path ./roles tksarah.fetch-files
```


Requirements
------------

* Ansible version 2.0 < 
* Perl 

Role Variables
--------------

Available variables are listed below,

**defaults/main.yml:**
```
savedir: "fetched"
```

**vars/files.yml:**

```
lists:
  - { filename: '/etc/ssh/sshd_config' }
  - { filename: '/var/log/syslog' }
  - { filename: '/etc/nsswitch.conf' }
```

This vars file will be created with automatic when you run a playbook.
All you have to do is create a text file as below.

**Ex) sample_filelist.txt:**
```
/etc/ssh/sshd_config
/var/log/syslog
/etc/nsswitch.conf
```

Dependencies
------------

None

Example Playbook
----------------

```
- name: Playbook for fetching files
  hosts: "{{ target }}"
  gather_facts: no

  become: true
  become_user: root

  vars_prompt:
    - { name: "target" , prompt: "Input target host" ,  default: all , private: no }
    - { name: "inputfile" , prompt: "Input your file list" , default: sample_filelist.txt , private: no }
    - { name: "savedir" , prompt: "Input a save directory" , default: fetched , private: no }

  pre_tasks:
    - block:
        - name: Pre setup (create lists for fetch)
          local_action: raw ./roles/tksarah.fetch-files/tools/create_vars.pl "{{ inputfile }}"
      become: false

  roles:
    - tksarah.fetch-files

```

License
-------

BSD

Author Information
------------------

fetch-file role was written by: T.Kuramochi
