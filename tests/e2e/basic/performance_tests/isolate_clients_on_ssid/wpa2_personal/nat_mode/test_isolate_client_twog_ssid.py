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
        station_list = []
        # if ssid not in get_vif_state:
        #     allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
        #     pytest.xfail("SSID's NOT AVAILABLE IN VIF STATE")

        for i in range(0, 2):
            station_list.append(port_resources[0] + "." + port_resources[1] + "." + lf_tools.twog_prefix + str(i))
        print(station_list)
        lf_test.Client_Connect(ssid=ssid, passkey=security_key, security=security, mode=mode, band=band,
                               vlan_id=1, station_name=station_list)

        station_ip = lf_tools.json_get("/port/" + port_resources[0] + "/" + port_resources[1] + "/" +
                                       station_list[1].split('.')[-1])["interface"]["ip"]
        print("station ip...", station_ip)
        created_endp = lf_test.gen_test([station_list[0]], station_ip)
        print("created endp...", created_endp)

        gen_results = lf_tools.json_get(_req_url="generic/list?fields=name,last+results")
        print("gen results...", gen_results)
        if gen_results['endpoints'] is not None:
            for name in gen_results['endpoints']:
                for k, v in name.items():
                    if v['name'] in created_endp and not v['name'].endswith('1'):
                        if v['last results'] != "" and "Unreachable" not in v['last results']:
                            print(v['name'])
                            allure.attach(v['name'])
                            assert False
                        else:
                            assert True
                            print(v['name'])
                            allure.attach(v['name'])
