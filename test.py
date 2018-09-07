import ast
import sys
import subprocess
from brightOps import brightOps

 
def main():
  element = ["1", "MCQTH01", "", "", "SMPLTEST", "FINANCE", "ACCTREC", "MCQTH01", "COBOL", "1", "", "SMPLTEST"]
  bright = brightOps("WEBSALC", "SMPLTEST", "FINANCE", "ACCTREC")
  out = bright.submitCommand(element)

  elements = bright.testing(out)
  for components in elements:
        num, member, vvll, date, time, system, subsystem, element, element_type, stg, ste, environment = components
        print member, system, subsystem, element, element_type, stg, environment
        bright = brightOps("", "", "", "")
        bright.get_files_by_details(components)
        bright.submitCommand(components)

if __name__ == "__main__":
  main()
  sys.exit(0)