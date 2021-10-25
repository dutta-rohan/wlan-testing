import pytest
import allure

pytestmark = [pytest.mark.multistation_perf, pytest.mark.bridge]


setup_params_general = {
    "mode": "BRIDGE",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_per", "appliedRadios": ["2G", "5G"], "security_key": "something"}
        ]
    },
    "rf": {},
    "radius": False
}

# @allure.feature("BRIDGE MODE Dataplane Throughput Test")
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class Test_Multistation_Performance_Bridge(object):

    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    def test_tcp_nss1_wpa2_personal_2g(self, setup_profiles, lf_tools, lf_test):

        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssid_name = profile_data["ssid_name"]
        print(ssid_name)
        mode = "BRIDGE"
        vlan = 1
        lf_tools.add_stations(band="2G", num_stations=3, dut=lf_tools.dut_name, ssid_name=ssid_name)
        lf_tools.Chamber_View()
        wct_obj = lf_test.wifi_capacity(instance_name="test_client_wpa2_BRIDGE_tcp_dl", mode=mode, vlan_id=vlan,
                                        download_rate="1Gbps", batch_size="1,5,10,20,40,64,128,256",
                                        upload_rate="0", protocol="TCP-IPv4", duration="60000")

        report_name = wct_obj.report_name[0]['LAST']["response"].split(":::")[1].split("/")[-1]

        lf_tools.attach_report_graphs(report_name=report_name)
        print("Test Completed... Cleaning up Stations")
        assert True
