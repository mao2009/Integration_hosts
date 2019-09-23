import unittest


class MyTestCase(unittest.TestCase):

    @classmethod
    def test_write(cls):
        from hostsfile import HostsIntegrator
        hosts = HostsIntegrator()
        hosts.add_hosts("https://sites.google.com/site/hosts2ch/ja")
        hosts.add_hosts("https://warui.intaa.net/adhosts/hosts_lb.txt")
        hosts.add_hosts("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts")
        hosts.add_hosts("https://mirror1.malwaredomains.com/files/justdomains")
        hosts.add_hosts("http://sysctl.org/cameleon/hosts")
        hosts.add_hosts("https://zeustracker.abuse.ch/blocklist.php?download=domainblocklist")
        hosts.add_hosts("https://s3.amazonaws.com/lists.disconnect.me/simple_tracking.txt")
        hosts.add_hosts("https://s3.amazonaws.com/lists.disconnect.me/simple_ad.txt")
        hosts.add_hosts("https://hosts-file.net/ad_servers.txt")
        hosts.add_hosts("https://mao2009.github.io/maos_adblock_hosts/hosts.txt")
        hosts.write_hosts(comments=["#mao's ad-block hosts"])


if __name__ == '__main__':
    unittest.main()
