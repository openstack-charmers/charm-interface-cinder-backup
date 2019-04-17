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
