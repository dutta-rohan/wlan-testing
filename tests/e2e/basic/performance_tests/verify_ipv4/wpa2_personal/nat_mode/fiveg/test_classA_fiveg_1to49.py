"""

    Class A IP Address: NAT Mode
    pytest -m "verify_classA_ip and wpa2_personal and nat and fiveg"

"""

import os
import allure
import pytest

pytestmark = [pytest.mark.regression,pytest.mark.dhcp, pytest.mark.verify_classA_ip, pytest.mark.wpa2_personal, pytest.mark.nat,
              pytest.mark.fiveg]

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something"}]},
    "rf": {},
    "ipv4": {"addressing": "static", "subnet": "10.168.1.1/8",
             "dhcp": {"lease-first": 10, "lease-count": 100, "lease-time": "6h"}
             },
    "radius": False
}

@allure.suite("regression")
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestClassAIP(object):

    @pytest.mark.wpa2_personal
    @pytest.mark.fiveg
    @allure.testcase(name="test_classA_ip_fiveg",
                     url="https://telecominfraproject.atlassian.net/browse/WIFI-4874")
    def test_classA_ip_fiveg(self, get_vif_state, lf_tools,
                       create_lanforge_chamberview_dut, lf_test, station_names_fiveg, get_configuration):
        """
        pytest -m "verify_classA_ip and wpa2_personal and nat and fiveg"

        """
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"]
        ssid_5G = profile_data[0]["ssid_name"]
        security_key_5G = profile_data[0]["security_key"]
        security = "wpa2"
        band = "fiveg"
        mode = "NAT"
        vlan = 1
        print(lf_tools.dut_idx_mapping)
        upstream_port = lf_tools.upstream_port
        print(upstream_port)
        port_resources = upstream_port.split(".")

        if ssid_5G not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        station = lf_test.Client_Connect(ssid=ssid_5G, security=security,
                                         passkey=security_key_5G, mode=mode, band=band,
                                         station_name=station_names_fiveg, vlan_id=vlan)
        print(station)
    
        if station:
            station_ip = lf_tools.json_get("/port/" + port_resources[0] + "/" + port_resources[1] + "/" +
                                           station_names_fiveg[0])["interface"]["ip"]

            station_ip = station_ip.split(".")
            config_ip = setup_params_general["ipv4"]["subnet"].split(".")

            print(station_ip[0], config_ip[0])
            if station_ip[0] != config_ip[0]:
                print("station didn't got ip as per ClassA subnet")
                assert False
            else:
                print("station got ip as per ClassA subnet")
                assert True
        else:
            print("station didn't got ip")
            assert False
        allure.attach("applied subnet to AP...%s"%(setup_params_general["ipv4"]["subnet"]))
        allure.attach("Received subnet from station....%s" %('.'.join(station_ip)))
