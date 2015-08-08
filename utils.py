import ConfigParser
import os

class DockerConfig:
    def __init__(self):
        self.ini_name = 'docker.ini'
        self.volumes = []
        self.author = {'name': '', 'email': ''}
        self.parse_config()

    def parse_volumes(self, parser):
        count = 0
        while True:
            src_opt = 'map%dsrc' % count
            dst_opt = 'map%ddst' % count
            if not parser.has_option('volumes', src_opt) or not parser.has_option('volumes', dst_opt):
                return

            src = parser.get('volumes', src_opt)
            dst = parser.get('volumes', dst_opt)

            tmp = {}
            tmp['src'] = src
            tmp['dst'] = dst

            self.volumes.append(tmp)

            count += 1

    def parse_author(self, parser):
        if parser.has_option('author', 'name') and parser.has_option('author', 'email'):
            self.author['name'] = parser.get('author', 'name')
            self.author['email'] = parser.get('author', 'email')

    def parse_config(self):
        parser = ConfigParser.RawConfigParser()
        parser.read(self.ini_name)

        if parser.has_section('volumes'):
            self.parse_volumes(parser)

        if parser.has_section('author'):
            self.parse_author(parser)

    def get_volumes(self):
        return self.volumes

    def get_author_name(self):
        return self.author['name']

    def get_author_email(self):
        return self.author['email']

def check_permission():
    return os.geteuid() == 0

if __name__ == '__main__':
    config = DockerConfig()

    print config.get_volumes()
    print config.get_author_name()
    print config.get_author_email()
