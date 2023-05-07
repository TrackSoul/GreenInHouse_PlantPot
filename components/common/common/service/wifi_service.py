import os

class WifiService:
     
    @staticmethod
    def scan_networks(iface = "wlan0"):
        command = "iwlist {} scan | grep -ioE 'SSID:\"(.+)\"'"
        result = os.popen((command.format(iface)))
        result = list(result)

        if "Device or resource busy" in result:
            return []
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            return ssid_list
        
    @staticmethod
    def wifi_conected():
        wifi_list = []
        command = "iwgetid"
        result = os.popen((command.format()))
        result = list(result)
        for item in result:
            itemp_p = item.partition('     ESSID:')
            wifi_list.append([itemp_p[0],itemp_p[2].strip('"\n')])
        return wifi_list

    @staticmethod
    def kwnown_wifis():
        wifi_list = []
        command = "cat /etc/wpa_supplicant/wpa_supplicant.conf | grep -A 1 -iE 'ssid=\"(.+)\"'"
        result = os.popen((command.format()))
        result = list(result)
        while(True):
            try:
                result.remove('--\n')
            except:
                break
        for n_item in range(0,len(result),2):
            wifi_list.append([result[n_item].lstrip('\t ssid="').strip('"\n'),result[n_item+1].lstrip('\t psk="').strip('"\n')])
        return wifi_list 
    
    @staticmethod
    def connect_wifi(ssid,psk):
        network = ""
        wifi_list=WifiService().kwnown_wifis()
        wifi_exists = False       
        for wifi in wifi_list:
            if ssid == wifi[0]:
                wifi_exists = True
                if psk != wifi[1]:
                    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "rt") as file:
                        x = file.read()

                    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "wt") as file:
                        x = x.replace(wifi[1],psk)
                        file.write(x)
        if not wifi_exists:
            with open("/etc/wpa_supplicant/wpa_supplicant.conf", "at") as file:
                new_network="\nnetwork={\n"+"\t\tssid=\"{}\"\n".format(ssid)+"\t\tpsk=\"{}\"\n".format(psk)+"\t\tkey_mgmt=WPA-PSK\n}\n"
                file.write(new_network)
        return True

# if __name__ == "__main__":
#     print(WifiService().scan_networks())
#     print()
#     print(WifiService().wifi_conected())
#     print()
#     print(WifiService().kwnown_wifis())
#     print()
#     print(WifiService().connect_wifi("UniqueSo","TrackSoul_1995"))
#     print()
#     print(WifiService().kwnown_wifis())
#     print()
    