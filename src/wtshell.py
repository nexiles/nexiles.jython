import os
import sys
import code
import wt_classpath

def main():
    if "WT_HOME" not in os.environ:
        print "please set WT_HOME."
        sys.exit(10)
    WT_HOME = os.environ["WT_HOME"]
    wt_classpath.set_windchill_classpath(WT_HOME)
    code.interact()

if __name__ == '__main__':
    main()

