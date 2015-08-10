import ConfigParser
import os
import subprocess
import re

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

def parse_output(s):
    lines = re.split('\n', s)
    list = []

    for l in lines:
        if l.startswith('CONTAINER'):
            continue

        if l == '':
            continue

        fields = re.split('\s+', l)
        tmp = {}
        tmp['id'] = fields[0]
        tmp['image'] = fields[1]
        list.append(tmp)

    return list

def get_containers():
    out = subprocess.check_output('docker ps -a', shell = True)

    list = parse_output(out)

    return list

def prompt_container(list):
    print 'Available containers:'

    c = 0
    for i in list:
        print '%d) %s (%s)' % (c, i['id'], i['image'])
        c += 1

    print ''
    ans = ''
    while True:
        ans = raw_input('Select a container: ')

        if not ans:
            continue

        idx = int(ans)
        if idx > len(list) - 1:
            print 'Out of range'
            continue

        return list[idx]

if __name__ == '__main__':
    config = DockerConfig()

    print config.get_volumes()
    print config.get_author_name()
    print config.get_author_email()
