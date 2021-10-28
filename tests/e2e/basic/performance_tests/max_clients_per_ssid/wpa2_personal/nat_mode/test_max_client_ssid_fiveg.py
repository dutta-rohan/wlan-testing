import os
import allure
import pytest

pytestmark = [pytest.mark.max_client_per_ssid]  # pytest.mark.usefixtures("setup_test_run")

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_personal_2g", "appliedRadios": ["2G"], "security_key": "something",
             },
            {"ssid_name": "ssid_wpa2_personal_5g", "appliedRadios": ["5G"], "security_key": "something",
             "maximum-clients": 4}]},
    "rf": {},
    "radius": False
}


@pytest.mark.max_client_per_ssid
@pytest.mark.wifi5
@pytest.mark.wifi6
@pytest.mark.parametrize(
    "setup_profiles",
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestMaxClientPerssid(object):


    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    # @allure.testcase(name="test_max_client_wpa2_nat_fiveg",
    # url="https://telecominfraproject.atlassian.net/browse/WIFI-4974")
    def test_max_client_wpa2_nat_fiveg(self, get_vif_state, lf_tools,
                                      create_lanforge_chamberview_dut, lf_test, get_configuration):
        '''
            pytest -m "vlan_combination_test and valid and wpa2_personal and twog
        '''

        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"]
        ssid = profile_data[1]["ssid_name"]
        mode = setup_params_general["mode"]
        band = "fiveg"
        vlan = 1
        num_sta_max = int(profile_data[0]["maximum-clients"]) + 1
        print(lf_tools.dut_idx_mapping)
        lf_tools.add_stations(band="2G", num_stations=num_sta_max, dut=lf_tools.dut_name, ssid_name=ssid)
        lf_tools.Chamber_View()
        wct_obj = lf_test.wifi_capacity(instance_name="test_max_client_wpa2_nat_fiveg", batch_size=str(num_sta_max),
                                        mode=mode, vlan_id=vlan, download_rate="1Gbps",
                                        upload_rate="0", protocol="TCP-IPv4", duration="60000")

        report_name = wct_obj.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]

        lf_tools.attach_report_graphs(report_name=report_name)
        print("Test Completed... Cleaning up Stations")
        assert True
