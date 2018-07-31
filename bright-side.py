from brightOps import brightOps
import argparse
import sys
from subprocess import call

def cleanup():
    call("del", "end*.txt")

def main(args):
    print "Starting..."
    parser = argparse.ArgumentParser("bright-side")
    parser.add_argument("Instance", help="Endevor REST Server Instance Name", type=str)
    parser.add_argument("Environment", help="Endevor Environment Name", type=str)
    parser.add_argument("System", help="Endevor System Name", type=str)
    parser.add_argument("Subsystem", help="Endevor Subsystem Name" , type=str)
    parser.add_argument("-c", "--ccid", help="CCID to search for", type=str)
    #parser.add_argument("-p", "--package", help="Package Name", type=str)
    parser.add_argument("-d", "--debug",  help="Debugging Information", type=int)
    parser.add_argument("-a", "--all", help="Gets all files based upon Env, Sys and Sub search", dest='all', default=False, action='store_true')
    args = parser.parse_args()



    bright = brightOps(args.Instance, args.Environment, args.System, args.Subsystem)

    
    if(args.all):
        print "Getting all files"
        bright.get_all_files()
    else:
        print "getting files by ccid"
        bright.get_files_by_ccid(args.ccid)


    #cleanup()


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except Exception, details:
        print "Details of error %s" % details
        sys.exit(1)

    sys.exit(0)