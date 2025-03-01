# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from nova.tests.functional.api_sample_tests import api_sample_base

CONF = cfg.CONF
CONF.import_opt('osapi_compute_extension',
                'nova.api.openstack.compute.legacy_v2.extensions')


class QuotaSetsSampleJsonTests(api_sample_base.ApiSampleTestBaseV3):
    ADMIN_API = True
    extension_name = "os-quota-sets"

    def _get_flags(self):
        f = super(QuotaSetsSampleJsonTests, self)._get_flags()
        f['osapi_compute_extension'] = CONF.osapi_compute_extension[:]
        f['osapi_compute_extension'].append('nova.api.openstack.compute.'
                                    'contrib.server_group_quotas.'
                                    'Server_group_quotas')
        f['osapi_compute_extension'].append('nova.api.openstack.compute.'
                                    'contrib.quotas.Quotas')
        f['osapi_compute_extension'].append('nova.api.openstack.compute.'
                                    'contrib.extended_quotas.Extended_quotas')
        f['osapi_compute_extension'].append('nova.api.openstack.compute.'
                                    'contrib.user_quotas.User_quotas')
        return f

    def test_show_quotas(self):
        # Get api sample to show quotas.
        response = self._do_get('os-quota-sets/fake_tenant')
        self._verify_response('quotas-show-get-resp', {}, response, 200)

    def test_show_quotas_defaults(self):
        # Get api sample to show quotas defaults.
        response = self._do_get('os-quota-sets/fake_tenant/defaults')
        self._verify_response('quotas-show-defaults-get-resp',
                              {}, response, 200)

    def test_update_quotas(self):
        # Get api sample to update quotas.
        response = self._do_put('os-quota-sets/fake_tenant',
                                'quotas-update-post-req',
                                {})
        self._verify_response('quotas-update-post-resp', {}, response, 200)

    def test_delete_quotas(self):
        # Get api sample to delete quota.
        response = self._do_delete('os-quota-sets/fake_tenant')
        self.assertEqual(202, response.status_code)
        self.assertEqual('', response.content)

    def test_update_quotas_force(self):
        # Get api sample to update quotas.
        response = self._do_put('os-quota-sets/fake_tenant',
                                'quotas-update-force-post-req',
                                {})
        return self._verify_response('quotas-update-force-post-resp', {},
                                     response, 200)

    def test_show_quotas_for_user(self):
        # Get api sample to show quotas for user.
        response = self._do_get('os-quota-sets/fake_tenant?user_id=1')
        self._verify_response('user-quotas-show-get-resp', {}, response, 200)

    def test_delete_quotas_for_user(self):
        response = self._do_delete('os-quota-sets/fake_tenant?user_id=1')
        self.assertEqual(202, response.status_code)
        self.assertEqual('', response.content)

    def test_update_quotas_for_user(self):
        # Get api sample to update quotas for user.
        response = self._do_put('os-quota-sets/fake_tenant?user_id=1',
                                'user-quotas-update-post-req',
                                {})
        return self._verify_response('user-quotas-update-post-resp', {},
                                     response, 200)
