#!/usr/bin/env python

ARCHIVE = "/afs/desy.de/user/l/lveldere/VBF-LS-tau/archive"
LOGBOOK = "/afs/desy.de/user/l/lveldere/VBF-LS-tau/logbook"

import sys,shutil,os,time

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
archive_subdir = ARCHIVE + "/" + tag
os.mkdir(archive_subdir)

# create subdir in logbook directory
logbook_subdir = LOGBOOK + "/" + tag
os.mkdir(logbook_subdir)

# copy the histdir
print "copying histograms to",archive_subdir + "/hist"
shutil.copytree(options.histdir,archive_subdir + "/hist") 

# copy the pdf files
print "copying final results to",archive_subdir + "/hist"
shutil.copytree(options.finalresdir,archive_subdir + "/finalres") 

# run prepareLogBook
print "preparing the tex file for the log book"
os.system("./prepareLogBook.py " + archive_subdir + "/finalres " + logbook_subdir + "/" + tag + ".tex")

# run pdflatex
print "running pdflatex"
os.system("cd " + logbook_subdir + "; pdflatex " + logbook_subdir + "/" + tag + ".tex; pdflatex " + logbook_subdir + "/" + tag + ".tex;  pdflatex " + logbook_subdir + "/" + tag + ".tex;")
