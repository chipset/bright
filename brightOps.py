import json
import subprocess
from subprocess import call
import os
import re

class brightOps:
    def __init__(self, instance, environment, system, subsystem, debug):
        self.instance = instance
        self.environment = environment
        self.system = system
        self.subsystem = subsystem
        self.debug = debug
    
    def debug(self, msg):
        if self.debug == True:
            print msg
    
    def getComponentTree(self, element):
        self.get_files_by_details(element)
        print "Pocessing Component Tree"
        elements = self.getInputComponentList(element)
        elementList = self.getElementList(elements)
        for components in elementList:
            #self.debug("Component Print")
            num, member, vvll, date, time, system, subsystem, element, element_type, stg, ste, environment = components
            print member, system, subsystem, element, element_type, stg, environment
            self.get_files_by_details(components)
            self.getInputComponentList(components)     
            self.clean_up_mess()   

    def getInputComponentList(self, element):
        num, member, vvll, date, time, system, subsystem, element, elementType, stg, ste, environment = element
        cmdLine = "bright.cmd endevor print comp MCQTH01 --env {} --sys {} --sub {} --typ {} -i WEBSALC --sn {}".format(environment, system, subsystem, elementType, stg)
        output = subprocess.check_output(cmdLine.split())
        lines = output.split("\n")
        successCheck = "finished with 0000"
        failureCheck = "finished with 0004 *NOTFND*"
        for i in reversed(lines):
                if successCheck in i:
                    #self.debug("Success!")
                    return lines
        for i in reversed(lines):
                if failureCheck in i:
                    #self.debug("found failure")
                    return
        print lines
        return lines


    def getElementList(self,infile):
        elementList = list()
        copy = False
        for line in infile:
                if "INPUT COMPONENTS" in line:
                    copy = True
                elif "OUTPUT COMPONENTS" in line:
                    copy = False
                elif copy:
                    if "+" in line:
                        print line
                        temp = line.split()
                        if(len(temp) > 3):
                            elementList.append(temp)
        return elementList


    def get_files_by_details(self, details):
        num, member, vvll, date, time, system, subsystem, element, element_type, stg, ste, environment = details
        command = "bright.cmd endevor ret ele {} --typ {} --env {} --sys {} --sub {} --sn {} -i WEBSALC --comment BrightDownload --ccid TEST --tf {} --sm".format(element, element_type, environment,
        system, subsystem, stg, "{}.{}".format(element, element_type))
        #print "Trying Command {}".format(command)
        try:
            out = subprocess.check_output(command.split())
        except Exception, details:
            #print get_files
            print "Error downloading file %" % details

        self.clean_up_mess()

    def get_files_by_ccid(self, ccid):
        out = subprocess.check_output(['bright.cmd', 'endevor', 'list', 'elements', '-i', self.instance, '--sm', '--fo', '--env', self.environment, '--sys', self.system, '--sub', self.subsystem, '--rft', 'string'])
        jObj = json.loads(out)
        #self.debug("Download These Files")
        for i in jObj:
            if i['lastActCcid'] == ccid:
                #print i["elmName"], i["typeName"], i['stgNum']
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
            #print file["elmName"], file["typeName"], file['stgNum']
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
        #print "Cleaning up"
        dir = ".\\"
        pattern = "end.*.txt"
        for f in os.listdir(dir):
            if re.search(pattern, f):
                os.remove(os.path.join(dir, f))
