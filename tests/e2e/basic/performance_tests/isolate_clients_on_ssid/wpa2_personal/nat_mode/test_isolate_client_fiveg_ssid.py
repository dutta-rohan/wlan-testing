"""

    Isolate Clients per ssid: NAT Mode
    pytest -m "isolate_clients and wpa2_personal and nat and fiveg"

"""

import os
import allure
import pytest

pytestmark = [pytest.mark.regression, pytest.mark.isolate_clients, pytest.mark.wpa2_personal, pytest.mark.nat,
              pytest.mark.fiveg]

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"], "security_key": "something",
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
    @pytest.mark.fiveg
    @allure.testcase(name="test_isolate_clients_2g",
                     url="https://telecominfraproject.atlassian.net/browse/WIFI-4871")
    def test_isolate_clients_5g(self, get_vif_state, lf_tools,
                                create_lanforge_chamberview_dut, lf_test, station_names_fiveg, get_configuration):
        """
        pytest -m "isolate_clients and wpa2_personal and nat and fiveg"

        """
        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"]
        ssid = profile_data[0]["ssid_name"]

        security_key = profile_data[0]["security_key"]

        security = "wpa2"
        band = "fiveg"
        dut_name = create_lanforge_chamberview_dut
        mode = "NAT"
        vlan = 1
        station_list = []
        print(lf_tools.dut_idx_mapping)
        upstream_port = lf_tools.upstream_port
        print(upstream_port)
        port_resources = upstream_port.split(".")

        if ssid not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID's NOT AVAILABLE IN VIF STATE")
        for i in range(0, 2):
            station_list.append(port_resources[0] + "." + port_resources[1] + "." + lf_tools.fiveg_prefix + str(i))
        print(station_list)
        lf_test.Client_Connect(ssid=ssid, passkey=security_key, security=security, mode=mode, band=band,
                               vlan_id=1, station_name=station_list)
        station = True

        if station:
            station_ip = lf_tools.json_get("/port/" + port_resources[0] + "/" + port_resources[1] + "/" +
                                           station_names_fiveg[1])["interface"]["ip"]
            created_endp = lf_test.gen_test(station_names_fiveg[0], station_ip)

            gen_results = lf_tools.json_get(_req_url="generic/list?fields=name,last+results")
            if gen_results['endpoints'] is not None:
                for name in gen_results['endpoints']:
                    for k, v in name.items():
                        if v['name'] in created_endp and not v['name'].endswith('1'):
                            if v['last results'] != "" and "Unreachable" not in v['last results']:
                                assert True
                                print(v['name'])
                                allure.attach(v['name'])
                            else:
                                print(v['name'])
                                allure.attach(v['name'])
                                assert False

        assert True
