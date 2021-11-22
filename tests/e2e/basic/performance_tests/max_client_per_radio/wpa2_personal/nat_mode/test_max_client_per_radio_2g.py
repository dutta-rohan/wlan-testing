import os
import allure
import pytest

pytestmark = [pytest.mark.regression,pytest.mark.max_client_per_radio]  # pytest.mark.usefixtures("setup_test_run")

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_personal_2g", "appliedRadios": ["2G"], "security_key": "something"}]},

    "rf": {
        "band": "2G",
        "country": "US",
        # "channel-mode": "HE",
        "channel-width": 40,
        # "channel": 11
        "maximum-clients": 4
    },
    "radius": False
}


@pytest.mark.parametrize(
    "setup_profiles",
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestMaxClientPerradio(object):

    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @allure.testcase(name="test_max_client_per_radio_wpa2_nat_twog",
                     url="https://telecominfraproject.atlassian.net/browse/WIFI-5757")
    def test_max_client_per_radio_wpa2_nat_twog(self, get_vif_state, lf_tools,
                                                create_lanforge_chamberview_dut, lf_test, get_configuration):
        '''
            pytest -m "max_client_per_radio and wpa2_personal and twog
        '''

        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"]
        ssid = profile_data[0]["ssid_name"]
        mode = setup_params_general["mode"]
        vlan = 1
        num_sta_max = setup_params_general["rf"]["maximum-clients"]
        print(lf_tools.dut_idx_mapping)
        lf_tools.add_stations(band="2G", num_stations=int(num_sta_max) + 1, dut=lf_tools.dut_name, ssid_name=ssid)
        lf_tools.Chamber_View()
        wct_obj = lf_test.wifi_capacity(instance_name="test_max_client_per_radio_wpa2_nat_twog",
                                        batch_size="%d" % (int(num_sta_max) + 1),
                                        mode=mode, vlan_id=vlan, download_rate="10M",
                                        upload_rate="10M", protocol="TCP-IPv4", duration="60000")

        report_name = wct_obj.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]

        lf_tools.attach_report_graphs(report_name=report_name)
        print("Test Completed...")
        assert True
