"""

    Isolate Clients per ssid: NAT Mode
    pytest -m "isolate_clients and wpa2_personal and nat and twog"

"""

import os
import allure
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.isolate_clients, pytest.mark.wpa2_personal, pytest.mark.nat,
              pytest.mark.twog]

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something",
             "isolate-clients": "true"},
        ]},
    "rf": {},
    "radius": False
}


@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestIsolateClientsSSID(object):

    @pytest.mark.wpa2_personal
    @pytest.mark.twog
    @allure.testcase(name="test_isolate_clients_2g",
                     url="https://telecominfraproject.atlassian.net/browse/WIFI-4871")
    def test_isolate_clients_2g(self, get_vif_state, lf_tools,
                                create_lanforge_chamberview_dut, lf_test, station_names_twog, get_configuration):
        """
        pytest -m "isolate_clients and wpa2_personal and nat and twog"

        """
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"]
        ssid = profile_data[0]["ssid_name"]

        security_key = profile_data[0]["security_key"]

        security = "wpa2"
        band = "twog"
        dut_name = create_lanforge_chamberview_dut
        mode = "NAT"
        vlan = 1
        print(lf_tools.dut_idx_mapping)
        upstream_port = lf_tools.upstream_port
        print(upstream_port)
        port_resources = upstream_port.split(".")

        if ssid not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID's NOT AVAILABLE IN VIF STATE")

        station = lf_test.Client_Connect(ssid=ssid, security=security,
                                         passkey=security_key, mode=mode, band=band,
                                         station_name=station_names_twog, vlan_id=vlan)
        if station:
            station_ip = lf_tools.json_get("/port/" + port_resources[0] + "/" + port_resources[1] + "/" +
                                           station_names_twog[1])["interface"]["ip"]
            lf_test.gen_test(station_names_twog[0], station_ip)

            gen_results = lf_tools.json_get(_req_url="generic/list?fields=name,last+results")
            if gen_results['endpoints'] is not None:
                for name in gen_results['endpoints']:
                    for k, v in name.items():
                        if v['name'] in self.created_endp and not v['name'].endswith('1'):
                            if v['last results'] != "" and "Unreachable" not in v['last results']:
                                assert True
                                print(v['name'])
                            else:
                                print(v['name'])
                                assert False

        assert True
