import allure
import pytest

pytestmark = [pytest.mark.client_connectivity, pytest.mark.bridge, pytest.mark.enterprise, pytest.mark.tls, pytest.mark.sanity,]
pytest.mark.usefixtures("setup_test_run")

setup_params_enterprise = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa_enterprise": [
            {"ssid_name": "ssid_wpa_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa_eap_5g", "appliedRadios": ["5G"]}],
        "wpa2_enterprise": [
            {"ssid_name": "ssid_wpa2_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa2_eap_5g", "appliedRadios": ["5G"]}],
        "wpa3_enterprise": [
            {"ssid_name": "ssid_wpa3_eap_2g", "appliedRadios": ["2G"]},
            {"ssid_name": "ssid_wpa3_eap_5g", "appliedRadios": ["5G"]}]},

    "rf": {},
    "radius": True
}


@pytest.mark.enterprise
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_enterprise],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestBridgeModeEnterpriseTLSSuiteOne(object):

    @pytest.mark.wpa2_enterprise
    @pytest.mark.twog
    def test_wpa2_enterprise_2g(self, station_names_twog, setup_profiles, lf_test, update_report,
                                test_cases, radius_info):
        profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][0]
        ssid_name = profile_data["ssid_name"]
        security = "wpa2"
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        tls_passwd = radius_info["password"]
        eap = "TLS"
        identity = radius_info['user']
        pk_pass = radius_info["pk_password"]
        passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
                                     mode=mode, band=band,
                                     eap=eap, ttls_passwd=tls_passwd, identity=identity,
                                     station_name=station_names_twog, vlan_id=vlan, private_key="/home/lanforge/client.p12", ca_cert="/home/lanforge/ca.pem" , pk_passwd=pk_pass)
        assert passes

    @pytest.mark.wpa_enterprise
    @pytest.mark.twog
    def test_wpa_enterprise_2g(self, station_names_twog, setup_profiles, get_lanforge_data, lf_test, update_report,
                               test_cases, radius_info):
        profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][0]
        ssid_name = profile_data["ssid_name"]
        security = "wpa"
        extra_secu = ["wpa2"]
        mode = "BRIDGE"
        band = "twog"
        vlan = 1
        ttls_passwd = radius_info["password"]
        eap = "TTLS"
        identity = radius_info['user']
        passes = lf_test.EAP_Connect(ssid=ssid_name, security=security, extra_securities=extra_secu,
                                     mode=mode, band=band,
                                     eap=eap, ttls_passwd=ttls_passwd, identity=identity,
                                     station_name=station_names_twog, vlan_id=vlan)
        assert passes
    #
    # @pytest.mark.wpa_enterprise
    # @pytest.mark.fiveg
    # def test_wpa_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                            test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa"
    #     extra_secu = ["wpa2"]
    #     mode = "BRIDGE"
    #     band = "twog"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security, extra_securities=extra_secu,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
    #
    #
    #
    # @pytest.mark.wpa2_enterprise
    # @pytest.mark.fiveg
    # def test_wpa2_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa2"
    #     mode = "BRIDGE"
    #     band = "fiveg"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
    #
    # @pytest.mark.wpa3_enterprise
    # @pytest.mark.twog
    # def test_wpa3_enterprise_2g(self, station_names_twog, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][0]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa3"
    #     mode = "BRIDGE"
    #     band = "twog"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_twog, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
    #
    # @pytest.mark.wpa3_enterprise
    # @pytest.mark.fiveg
    # def test_wpa3_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa3"
    #     mode = "BRIDGE"
    #     band = "fiveg"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes


# setup_params_enterprise_two = {
#     "mode": "BRIDGE",
#     "ssid_modes": {
#         "wpa_enterprise": [
#             {"ssid_name": "ssid_wpa_eap_2g", "appliedRadios": ["2G"]},
#             {"ssid_name": "ssid_wpa_eap_5g", "appliedRadios": ["5G"]}],
#         "wpa2_enterprise": [
#             {"ssid_name": "ssid_wpa2_eap_2g", "appliedRadios": ["2G"]},
#             {"ssid_name": "ssid_wpa2_eap_5g", "appliedRadios": ["5G"]}],
#         "wpa3_enterprise": [
#             {"ssid_name": "ssid_wpa3_eap_2g", "appliedRadios": ["2G"]},
#             {"ssid_name": "ssid_wpa3_eap_5g", "appliedRadios": ["5G"]}]},
#
#     "rf": {},
#     "radius": True
# }
#
#
# @pytest.mark.enterprise
# @pytest.mark.parametrize(
#     'setup_profiles',
#     [setup_params_enterprise],
#     indirect=True,
#     scope="class"
# )
# @pytest.mark.usefixtures("setup_profiles")
# class TestBridgeModeEnterpriseTLSSuiteTwo(object):
#
#     @pytest.mark.wpa2_enterprise
#     @pytest.mark.twog
#     def test_wpa2_enterprise_2g(self, station_names_twog, setup_profiles, get_lanforge_data, lf_test, update_report,
#                                 test_cases, radius_info):
#         profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][0]
#         ssid_name = profile_data["ssid_name"]
#         security = "wpa2"
#         mode = "BRIDGE"
#         band = "twog"
#         vlan = 1
#         ttls_passwd = radius_info["password"]
#         eap = "TTLS"
#         identity = radius_info['user']
#         passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
#                                      mode=mode, band=band,
#                                      eap=eap, ttls_passwd=ttls_passwd, identity=identity,
#                                      station_name=station_names_twog, vlan_id=vlan)
#
#         if passes:
#             update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
#                                           status_id=1,
#                                           msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
#                                               passes))
#         else:
#             update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
#                                           status_id=5,
#                                           msg='2G WPA Client Connectivity Failed - bridge mode' + str(
#                                               passes))
#         assert passes

    # @pytest.mark.wpa_enterprise
    # @pytest.mark.twog
    # def test_wpa_enterprise_2g(self, station_names_twog, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                            test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][0]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa"
    #     extra_secu = ["wpa2"]
    #     mode = "BRIDGE"
    #     band = "twog"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security, extra_securities=extra_secu,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_twog, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes

    # @pytest.mark.wpa_enterprise
    # @pytest.mark.fiveg
    # def test_wpa_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                            test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa"
    #     extra_secu = ["wpa2"]
    #     mode = "BRIDGE"
    #     band = "twog"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security, extra_securities=extra_secu,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes



    # @pytest.mark.wpa2_enterprise
    # @pytest.mark.fiveg
    # def test_wpa2_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa2_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa2"
    #     mode = "BRIDGE"
    #     band = "fiveg"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
    #
    # @pytest.mark.wpa3_enterprise
    # @pytest.mark.twog
    # def test_wpa3_enterprise_2g(self, station_names_twog, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][0]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa3"
    #     mode = "BRIDGE"
    #     band = "twog"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_twog, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
    #
    # @pytest.mark.wpa3_enterprise
    # @pytest.mark.fiveg
    # def test_wpa3_enterprise_5g(self, station_names_fiveg, setup_profiles, get_lanforge_data, lf_test, update_report,
    #                             test_cases, radius_info):
    #     profile_data = setup_params_enterprise["ssid_modes"]["wpa3_enterprise"][1]
    #     ssid_name = profile_data["ssid_name"]
    #     security = "wpa3"
    #     mode = "BRIDGE"
    #     band = "fiveg"
    #     vlan = 1
    #     ttls_passwd = radius_info["password"]
    #     eap = "TTLS"
    #     identity = radius_info['user']
    #     passes = lf_test.EAP_Connect(ssid=ssid_name, security=security,
    #                                  mode=mode, band=band,
    #                                  eap=eap, ttls_passwd=ttls_passwd, identity=identity,
    #                                  station_name=station_names_fiveg, vlan_id=vlan)
    #
    #     if passes:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=1,
    #                                       msg='2G WPA Client Connectivity Passed successfully - bridge mode' + str(
    #                                           passes))
    #     else:
    #         update_report.update_testrail(case_id=test_cases["2g_wpa_bridge"],
    #                                       status_id=5,
    #                                       msg='2G WPA Client Connectivity Failed - bridge mode' + str(
    #                                           passes))
    #     assert passes
