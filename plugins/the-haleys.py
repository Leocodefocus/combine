from yapsy.IPlugin import IPlugin
import datetime

class PluginOne(IPlugin):
    NAME = "the-haleys"
    DIRECTION = "inbound"
    URLS = ['http://charles.the-haleys.org/ssh_dico_attack_hdeny_format.php/hostsdeny.txt']

    def get_URLs(self):
        return self.URLS

    def get_direction(self):
        return self.DIRECTION

    def get_name(self):
        return self.NAME

    def process_data(self, source, response):
        data = []
        current_date = str(datetime.date.today())
        for line in response.splitlines():
            if not line.startswith('#') and len(line) > 0:
                i = line.partition(':')[2].strip()
                data.append((i, "IPv4", self.DIRECTION, self.NAME, '', current_date))
        return data