import json
import subprocess

class brightOps:
    def __init__(self, instance, environment, system, subsystem):
        self.instance = instance
        self.environment = environment
        self.system = system
        self.subsystem = subsystem
    def get_files(self, ccid):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        jObj = json.loads(out)
        print "Download These Files"
        for i in jObj:
            if i['lastActCcid'] == ccid:
                print i["elmName"], i["typeName"]
    def get_all_files(self):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        endevor_file_list = json.loads(out)
        for file in endevor_file_list:
            print file["elmName"], file["typeName"], file["lastActCcid"]

