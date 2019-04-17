# Overview

Basic interface for sending Cinder-Backup external subordinate backend configuration.

# Metadata

To consume this interface in your charm or layer, add the following to layer.yaml:

```
includes: ['interface:cinder-backup']
```

and add a provides interface of type backup-backend to your charm or layers metadata.yaml:

```
provides:
  backup-backend:
    interface: cinder-backup
    scope: container
```

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/openstack-charms/+filebug).

For development questions please refer to the OpenStack [Charm Guide](https://github.com/openstack/charm-guide).