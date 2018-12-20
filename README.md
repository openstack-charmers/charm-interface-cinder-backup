# Overview

Basic interface for sending Cinder-Backup external Swift subordinate backend configuration to Cinder-backup-swift charm.

# Usage

## Requires

This interface layer will set the following state:

  * `{relation_name}.connected` The relation is established, but the charm may
    not have provided any backend information.