"""
About: It contains some Functional Unit Tests for CloudSDK and to run and test them on per unit level
"""

import pytest
import sys

if 'cloudsdk_tests' not in sys.path:
    sys.path.append(f'../../libs/cloudsdk')
from cloudsdk import CloudSDK


@pytest.mark.cloud
class TestLogin(object):

    @pytest.mark.bearer
    def test_token_login(self, get_customer_id, get_testbed_name):
        try:
            obj = CloudSDK(testbed=get_testbed_name, customer_id=get_customer_id)
            bearer = obj.get_bearer_token()
            value = bearer._access_token is None
        except:
            value = True
        assert value is False

    @pytest.mark.ping
    def test_ping(self, get_customer_id, get_testbed_name):
        try:
            obj = CloudSDK(testbed=get_testbed_name, customer_id=get_customer_id)
            value = obj.portal_ping() is None
        except:
            value = True
        assert value is False

#
# @pytest.mark.userfixtures('get_customer_id')
# @pytest.mark.userfixtures('get_testbed_name')
# @pytest.mark.ssid_profiles
# class TestSSIDProfiles(object):
#
#     @pytest.mark.ssid_open_bridge
#     def test_open_bridge(self):
#         pass
#
#     @pytest.mark.ssid_open_nat
#     def test_open_nat(self):
#         pass
#
#     @pytest.mark.ssid_open_vlan
#     def test_open_vlan(self):
#         pass
#
#     @pytest.mark.ssid_wpa_bridge
#     def test_wpa_bridge(self):
#         pass
#
#     @pytest.mark.ssid_wpa_nat
#     def test_wpa_nat(self):
#         pass
#
#     @pytest.mark.ssid_wpa_vlan
#     def test_wpa_vlan(self):
#         pass
#
#     @pytest.mark.ssid_wpa_personal_bridge
#     def test_wpa2_personal_bridge(self):
#         pass
#
#     @pytest.mark.ssid_wpa_personal_nat
#     def test_wpa2_personal_nat(self):
#         pass
#
#     @pytest.mark.ssid_wpa_personal_vlan
#     def test_wpa2_personal_vlan(self):
#         pass
#
#     @pytest.mark.ssid_wpa2_enterprise_bridge
#     def test_wpa2_enterprise_bridge(self):
#         pass
#
#     @pytest.mark.ssid_wpa2_enterprise_nat
#     def test_wpa2_enterprise_nat(self):
#         pass
#
#     @pytest.mark.ssid_wpa2_enterprise_vlan
#     def test_wpa2_enterprise_vlan(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_personal_bridge
#     def test_wpa3_personal_bridge(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_personal_nat
#     def test_wpa3_personal_nat(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_personal_vlan
#     def test_wpa3_personal_vlan(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_enterprise_bridge
#     def test_wpa3_enterprise_bridge(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_enterprise_nat
#     def test_wpa3_enterprise_nat(self):
#         pass
#
#     @pytest.mark.ssid_wpa3_enterprise_vlan
#     def test_wpa3_enterprise_vlan(self):
#         pass

#
# class TestEquipmentAPProfile(object):
#
#     def test_equipment_ap_profile_creation(self):
#         pass
