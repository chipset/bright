from brightOps import brightOps
import argparse
import sys
from subprocess import call
import traceback

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
    parser.add_argument("-l", "--componentlist", help="Gets component and input components", default=False, action="store_true")
    parser.add_argument("-comp", "--component", help="Component Name to Download", type=str)
    parser.add_argument("-e", "--element", help="Element to Download", type=str)
    parser.add_argument("-et", "--elementType", help="Element Type for Download", type=str)
    parser.add_argument("-stg", "--stageNumber", help="Stage Number for Element Download", type=str)

    args = parser.parse_args()
    #        num, member, vvll, date, time, system, subsystem, element, elementType, stg, ste, environment = element



    bright = brightOps(args.Instance, args.Environment, args.System, args.Subsystem)

    if(args.componentlist):
        element = ["", args.element, "", "", args.Environment, args.System, args.Subsystem, args.element, args.elementType, args.stageNumber, "", args.Environment]
        print element
        elements = bright.getInputComponentList(element)
        elementList = bright.getElementList(elements)
        for components in elementList:
            print "Component Print"
            print components
            num, member, vvll, date, time, system, subsystem, element, element_type, stg, ste, environment = components
            print member, system, subsystem, element, element_type, stg, environment
            bright = brightOps("", "", "", "")
            bright.get_files_by_details(components)
            bright.getInputComponentList(components)        
    elif(args.all):
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
        print Exception, details
        traceback.print_exc()
        sys.exit(1)

    sys.exit(0)