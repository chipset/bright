import json
import subprocess

class brightOps:
    def __init__(self, instance, environment, system, subsystem):
        self.instance = instance
        self.environment = environment
        self.system = system
        self.subsystem = subsystem
    def get_files_by_ccid(self, ccid):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        jObj = json.loads(out)
        print "Download These Files"
        for i in jObj:
            if i['lastActCcid'] == ccid:
                print i["elmName"], i["typeName"], i['stgNum']
                tofile = "" + i["elmName"] + "." + i["typeName"]
                get_files = subprocess.check_output(['bright.cmd', 'endevor', 'ret', 'ele', i["elmName"], "--typ", i["typeName"], "--env", self.environment, "--sys", self.system, "--sub",
                self.subsystem, "--sn", i["stgNum"],  "-i", self.instance, "--comment", "Bright Download", "--ccid", "BRIGHT", "--tf", tofile, "--sm"])
                print get_files
        
    def get_all_files(self):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        endevor_file_list = json.loads(out)
        for file in endevor_file_list:
            print file["elmName"], file["typeName"], file["lastActCcid"]

