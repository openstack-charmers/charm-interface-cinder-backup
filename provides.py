# Copyright 2018 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from charms.reactive import (
    Endpoint,
    clear_flag,
    set_flag,
    when,
    when_any,
)


class CinderBackupProvides(Endpoint):

    @when('endpoint.{endpoint_name}.joined')
    def joined(self):
        set_flag(self.expand_name('{endpoint_name}.connected'))

    @when('endpoint.{endpoint_name}.changed')
    def changed(self):
        set_flag(self.expand_name('{endpoint_name}.available'))
        clear_flag(self.expand_name('endpoint.{endpoint_name}.changed'))

    @when_any('endpoint.{endpoint_name}.broken',
              'endpoint.{endpoint_name}.departed')
    def departed(self):
        flags = (
            self.expand_name('{endpoint_name}.available'),
            self.expand_name('{endpoint_name}.connected'),
        )
        for flag in flags:
            clear_flag(flag)

    def publish(self, name, configuration):
        for relation in self.relations:
            relation.to_publish['backend_name'] = name
            relation.to_publish['subordinate_configuration'] = configuration
