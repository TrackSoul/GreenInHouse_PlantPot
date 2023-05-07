"""
Search for a specific wifi ssid and connect to it.
written by Mazdak.
"""
import os


class WifiFinder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = os.system("iwlist wlan0 scan | grep -ioE 'SSID:\"(.+)\"'")
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("nmcli d wifi connect {} password {}".format(name,
                self.password))
        except:
            raise
        else:
            return True

if __name__ == "__main__":
    # Server_name is a case insensitive string, and/or regex pattern which demonstrates
    # the name of targeted WIFI device or a unique part of it.
    server_name = "Livebox6-B8F7"
    password = "your_password"
    interface_name = "wlan0" # i. e wlp2s0  
    WF = WifiFinder(server_name=server_name,
               password=password,
               interface=interface_name)
    WF.run()

    # iwgetid