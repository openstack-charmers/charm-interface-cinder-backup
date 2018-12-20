#!/usr/bin/python

from charms.reactive import hook
from charms.reactive import RelationBase
from charms.reactive import scopes

class CinderBackupSwiftClient(RelationBase):
    scope = scopes.GLOBAL

    @hook('{provides:cinder-backup-swift}-relation-{joined,changed}')
    def cinder_backup_swift_joined(self):
        conv = self.conversation()
        conv.set_state('{relation_name}.joined')
        self.set_state('{relation_name}.connected')
        self.set_state('{relation_name}.available')

    @hook('{provides:cinder-backup-swift}-relation-{broken, departed}')
    def cinder_backup_swift_departed(self):
        conv = self.conversation()
        conv.remove_state('{relation_name}.joined')
        self.remove_state('{relation_name}.available')
        self.remove_state('{relation_name}.connected')
        conv.set_state('{relation_name}.departing')

    def configure_principal(self, configuration):
        """Send principal cinder-backup-swift-backend information"""
        conv = self.conversation()
        conv.set_remote(subordinate_configuration = configuration)