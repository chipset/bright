from jobsOps import jobsOps
import argparse
import sys
from subprocess import call
import traceback


def main(args):
    print "Starting..."
    parser = argparse.ArgumentParser("jobs")
    parser.add_argument("JCL", help="JCL Dataset Location -- mccqth01.jcl.ex(HW)", type=str)
    parser.add_argument("-d", "--debug",  help="Debugging Information", type=int)
    parser.add_argument("-a", "--add", help="Add JCL from HW.txt to PDS in JCL", type=str)
    args = parser.parse_args()

    jclJob = jobsOps(args.debug, args.JCL)

    if(args.add):
        print "Adding JCL to {}".format(args.JCL)
        jclJob.addJCLtoPDS(args.JCL, "ex")

    # Submit Job
    jobId = jclJob.submitJob()
    print jobId
    output = jclJob.getJobOutput(jobId, 103)
    print output



if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception, details:
        print "Details of error %s" % details
        print Exception, details
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)