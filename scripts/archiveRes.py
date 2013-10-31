#!/usr/bin/env python


import sys,shutil,os,time

# check the archive directory
if not "PROJECTARCHIVE" in os.environ:
    print "ERROR: define environmental variable PROJECTARCHIVE"
    sys.exit()
ARCHIVEDIR = os.environ["PROJECTARCHIVE"]
if not os.path.isdir(ARCHIVEDIR):
    print "ERROR: $ARCHIVEDIR must be a directory"
    sys.exit()

# parse command line options
from optparse import OptionParser
parser = OptionParser()
parser.add_option("--histdir",help="directory with histogram files (!W/O xsection weights!)")
parser.add_option("--finalresdir",help="directory with final results")
(options, args) = parser.parse_args()

if not options.histdir:
    print "use obligatory option --histdir"
    sys.exit()
if not options.finalresdir:
    print "use obligatory option --finalresdir"
    sys.exit()

# a time stamp
tag = time.strftime("%y%m%d_%H%M%S", time.gmtime())

# creat subdir in archive
if not os.path.isdir(ARCHIVEDIR + "/archive"):
    os.mkdir(ARCHIVEDIR + "/archive")
archivedir = ARCHIVEDIR + "/archive/" + tag
os.mkdir(archivedir)

# create subdir in logbook directory
if not os.path.isdir(ARCHIVEDIR + "/logbook"):
    os.mkdir(ARCHIVEDIR + "/logbook")
logbookdir = ARCHIVEDIR + "/logbook/" + tag
os.mkdir(logbookdir)

# copy the histdir
print "copying histograms to",archivedir + "/hist"
shutil.copytree(options.histdir,archivedir + "/hist") 

# copy the pdf files
print "copying final results to",archivedir + "/hist"
shutil.copytree(options.finalresdir,archivedir + "/finalres") 

# run prepareLogBook
print "preparing the tex file for the log book"
os.system("./prepareLogBook.py " + archivedir + "/finalres " + logbookdir + "/" + tag + ".tex")

# run pdflatex
print "running pdflatex"
os.system("cd " + logbookdir + "; pdflatex " + logbookdir + "/" + tag + ".tex; pdflatex " + logbookdir + "/" + tag + ".tex;  pdflatex " + logbookdir + "/" + tag + ".tex;")
