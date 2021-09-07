from logging import exception
import unittest
import warnings
from perfecto.test import TestResultFactory
import pytest
import sys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException

import sys
import allure

if 'perfecto_libs' not in sys.path:
    sys.path.append(f'../libs/perfecto_libs')

pytestmark = [pytest.mark.sanity, pytest.mark.interop, pytest.mark.android, pytest.mark.interop_and, pytest.mark.client_connectivity
              ,pytest.mark.interop_uc_sanity, pytest.mark.NAT]

from android_lib import closeApp, set_APconnMobileDevice_android, Toggle_AirplaneMode_android, ForgetWifiConnection, openApp, get_ip_address_and,get_all_available_ssids

setup_params_general = {
    "mode": "NAT",
    "ssid_modes": {
        "wpa": [{"ssid_name": "ssid_wpa_2g", "appliedRadios": ["2G"], "security_key": "something"},
                {"ssid_name": "ssid_wpa_5g", "appliedRadios": ["5G"],
                 "security_key": "something"}],
        "open": [{"ssid_name": "ssid_open_2g", "appliedRadios": ["2G"]},
                 {"ssid_name": "ssid_open_5g", "appliedRadios": ["5G"]}],
        "wpa2_personal": [
            {"ssid_name": "ssid_wpa2_2g", "appliedRadios": ["2G"], "security_key": "something"},
            {"ssid_name": "ssid_wpa2_5g", "appliedRadios": ["5G"],
             "security_key": "something"}]},
    "rf": {},
    "radius": False
}

@allure.suite(suite_name="interop sanity")
@allure.sub_suite(sub_suite_name="Nat Mode Client Connectivity : Suite-A")
@pytest.mark.InteropsuiteA
@allure.feature("BRIDGE MODE CLIENT CONNECT")
@pytest.mark.parametrize(
    'setup_profiles',
    [setup_params_general],
    indirect=True,
    scope="class"
)
@pytest.mark.usefixtures("setup_profiles")
class TestClientConnectBridgeMode(object):
    """ Client Connect SuiteA
        pytest -m "client_connect and nat and InteropsuiteA"
    """

    @pytest.mark.fiveg
    @pytest.mark.wpa2_personal
    def test_ClientConnect_5g_WPA2_Personal(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = profile_data["security_key"]
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)

        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @pytest.mark.twog
    @pytest.mark.wpa2_personal
    def test_ClientConnect_2g_WPA2_Personal(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["wpa2_personal"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = profile_data["security_key"]
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)

        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @pytest.mark.fiveg
    @pytest.mark.wpa
    def test_ClientConnect_5g_WPA(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["wpa"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = profile_data["security_key"]
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)

        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @pytest.mark.twog
    @pytest.mark.wpa
    def test_ClientConnect_2g_WPA(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["wpa"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = profile_data["security_key"]
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)

        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data

        # Set Wifi/AP Mode
        ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

    @pytest.mark.fiveg
    @pytest.mark.open
    def test_ClientConnect_5g_Open(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["open"][1]
        ssidName = profile_data["ssid_name"]
        ssidPassword = "[BLANK]"
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)

        if ssidName not in get_vif_state:
            allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
            pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data

        #Set Wifi/AP Mode
        ip, is_internet =  get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)

        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False

        #Toggle AirplaneMode
        # assert Toggle_AirplaneMode_android(request, setup_perfectoMobile_android, connData)

        #ForgetWifi
        # ForgetWifiConnection(request, setup_perfectoMobile_android, ssidName, connData)

    @pytest.mark.twog
    @pytest.mark.open
    def test_ClientConnect_2g_Open(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):

        profile_data = setup_params_general["ssid_modes"]["open"][0]
        ssidName = profile_data["ssid_name"]
        ssidPassword = "[BLANK]"
        print ("SSID_NAME: " + ssidName)
        print ("SSID_PASS: " + ssidPassword)
        print(get_vif_state)

        # if ssidName not in get_vif_state:
        #     allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
        #     pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")

        # print(get_all_available_ssids)
        report = setup_perfectoMobile_android[1]
        driver = setup_perfectoMobile_android[0]
        connData = get_ToggleAirplaneMode_data



        ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
        #
        if ip:
            if is_internet:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
            else:
                text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
            print(text_body)
            allure.attach(name="Connection Status: ", body=str(text_body))
            assert True
        else:
            allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
            assert False


#
#
#
# setup_params_general_two = {
#     "mode": "NAT",
#     "ssid_modes": {
#         "wpa3_personal": [
#             {"ssid_name": "ssid_wpa3_p_2g", "appliedRadios": ["2G"], "security_key": "something"},
#             {"ssid_name": "ssid_wpa3_p_5g", "appliedRadios": ["5G"],
#              "security_key": "something"}],
#         "wpa3_personal_mixed": [
#             {"ssid_name": "ssid_wpa3_p_m_2g", "appliedRadios": ["2G"], "security_key": "something"},
#             {"ssid_name": "ssid_wpa3_p_m_5g", "appliedRadios": ["5G"],
#              "security_key": "something"}],
#         "wpa_wpa2_personal_mixed": [
#             {"ssid_name": "ssid_wpa_wpa2_p_m_2g", "appliedRadios": ["2G"], "security_key": "something"},
#             {"ssid_name": "ssid_wpa_wpa2_p_m_5g", "appliedRadios": ["5G"],
#              "security_key": "something"}]
#     },
#     "rf": {},
#     "radius": False
# }
#
#
# @allure.suite(suite_name="interop sanity")
# @allure.sub_suite(sub_suite_name="Nat Mode Client Connectivity : Suite-B")
# @pytest.mark.InteropsuiteB
# @allure.feature("BRIDGE MODE CLIENT CONNECT")
# @pytest.mark.parametrize(
#     'setup_profiles',
#     [setup_params_general_two],
#     indirect=True,
#     scope="class"
# )
# @pytest.mark.usefixtures("setup_profiles")
# class TestBridgeModeConnectivitySuiteTwo(object):
#     """ Client Connect SuiteB
#         pytest -m "client_connect and nat and InteropsuiteB"
#     """
#
#     @pytest.mark.wpa3_personal
#     @pytest.mark.twog
#     @allure.story('open 2.4 GHZ Band')
#     def test_wpa3_personal_ssid_2g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa3_personal"][0]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         # if ssidName not in get_vif_state:
#         #     allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#         #     pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
#
#     @pytest.mark.wpa3_personal
#     @pytest.mark.fiveg
#     @allure.story('open 5 GHZ Band')
#     def test_wpa3_personal_ssid_5g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa3_personal"][1]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         if ssidName not in get_vif_state:
#             allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#             pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
#
#     @pytest.mark.wpa3_personal_mixed
#     @pytest.mark.twog
#     @allure.story('open 2.4 GHZ Band')
#     def test_wpa3_personal_mixed_ssid_2g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa3_personal_mixed"][0]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         if ssidName not in get_vif_state:
#             allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#             pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
#
#     @pytest.mark.wpa3_personal_mixed
#     @pytest.mark.fiveg
#     @allure.story('open 5 GHZ Band')
#     def test_wpa3_personal_mixed_ssid_5g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa3_personal_mixed"][1]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         if ssidName not in get_vif_state:
#             allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#             pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
#
#     @pytest.mark.wpa_wpa2_personal_mixed
#     @pytest.mark.twog
#     @allure.story('wpa wpa2 personal mixed 2.4 GHZ Band')
#     def test_wpa_wpa2_personal_ssid_2g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa_wpa2_personal_mixed"][0]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         if ssidName not in get_vif_state:
#             allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#             pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
#
#     @pytest.mark.wpa_wpa2_personal_mixed
#     @pytest.mark.fiveg
#     @allure.story('wpa wpa2 personal mixed 5 GHZ Band')
#     def test_wpa_wpa2_personal_ssid_5g(self, request, get_vif_state, get_ToggleAirplaneMode_data, setup_perfectoMobile_android):
#
#         profile_data = setup_params_general_two["ssid_modes"]["wpa_wpa2_personal_mixed"][1]
#         ssidName = profile_data["ssid_name"]
#         ssidPassword = "[BLANK]"
#         print ("SSID_NAME: " + ssidName)
#         print ("SSID_PASS: " + ssidPassword)
#
#         if ssidName not in get_vif_state:
#             allure.attach(name="retest,vif state ssid not available:", body=str(get_vif_state))
#             pytest.xfail("SSID NOT AVAILABLE IN VIF STATE")
#
#         report = setup_perfectoMobile_android[1]
#         driver = setup_perfectoMobile_android[0]
#         connData = get_ToggleAirplaneMode_data
#
#         # Set Wifi/AP Mode
#         ip, is_internet = get_ip_address_and(request, ssidName, ssidPassword, setup_perfectoMobile_android, connData)
#
#         if ip:
#             if is_internet:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "with internet")
#             else:
#                 text_body = ("connected to " + ssidName + " (" + ip + ") " + "without internet")
#             print(text_body)
#             allure.attach(name="Connection Status: ", body=str(text_body))
#             assert True
#         else:
#             allure.attach(name="Connection Status: ", body=str("Device is Unable to connect"))
#             assert False
