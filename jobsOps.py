import json
import subprocess
from subprocess import call
import os
import re

class jobsOps:
    def __init__(self, debug, jobName):
        self.jobName = jobName
        self.debug = debug
    
    def debug(self, msg):
        if self.debug == True:
            print msg
    
    def submitJob(self):
        cmdLine = "bright.cmd jobs submit ds --rfj true {} ".format(self.jobName)
        output = ""
        jobid = ""
        success = False
        try:
            output = subprocess.check_output(cmdLine.split(), stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output
 
        lines = output.split('\n')
        for i in lines:
            if self.debug:
                print "testing:" + i
            if '"jobid":' in i:
                if self.debug:
                    print "found here"
                values = re.findall(r'"([^"]*)"', i)  # Searches for items in quotes.  Should return 2 values.  Jobid and the Actual JobId.
                for value in values:
                    if value != "jobid":
                        jobid = value
        return value

    def getJobOutput(self, jobId, spoolId):
        cmdLine = "bright.cmd jobs view sfbi {} {}".format(jobId, spoolId)
        try:
            output = subprocess.check_output(cmdLine.split(), stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            output = e.output

        return output

    def addJCLtoPDS(self, PDS, fileToAdd):
        #remove the PDS member to add to the PDS.
        temp = PDS.split("(")
        PDS = temp[0]
        cmdLine = "bright.cmd files ul dtp {} {}".format(fileToAdd, PDS)
        if self.debug:
            print cmdLine
        try:
            output = subprocess.check_output(cmdLine.split())
        except subprocess.CalledProcessError as e:
            print e.output
            exit()

    def clean_up_mess(self):
        #print "Cleaning up"
        dir = ".\\"
        pattern = "end.*.txt"
        for f in os.listdir(dir):
            if re.search(pattern, f):
                os.remove(os.path.join(dir, f))
