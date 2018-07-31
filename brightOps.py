import json
import subprocess
from subprocess import call
import os
import re

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
                try: 
                    get_files = subprocess.check_output(['bright.cmd', 'endevor', 'ret', 'ele', i["elmName"], "--typ", i["typeName"], "--env", self.environment, "--sys", self.system, "--sub",
                        self.subsystem, "--sn", i["stgNum"],  "-i", self.instance, "--comment", "Bright Download", "--ccid", "BRIGHT", "--tf", tofile, "--sm"])
                except Exception, details:
                    #print get_files
                    print "Error downloading file %" % details
        
                    continue
        self.clean_up_mess()
        
    def get_all_files(self):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        endevor_file_list = json.loads(out)
        for file in endevor_file_list:
            print file["elmName"], file["typeName"], file['stgNum']
            tofile = "" + file["elmName"] + "." + file["typeName"]
            try:
                get_files = subprocess.check_output(['bright.cmd', 'endevor', 'ret', 'ele', file["elmName"], "--typ", file["typeName"], "--env", self.environment, "--sys", self.system, "--sub",
                    self.subsystem, "--sn", file["stgNum"],  "-i", self.instance, "--comment", "Bright Download", "--ccid", "BRIGHT", "--tf", tofile, "--sm"])
            except Exception, details:
                #print get_files
                print "Error downloading file %" % details
                continue

        self.clean_up_mess()

    def clean_up_mess(self):
        print "Cleaning up"
        dir = ".\\"
        pattern = "end.*.txt"
        for f in os.listdir(dir):
            if re.search(pattern, f):
                os.remove(os.path.join(dir, f))
