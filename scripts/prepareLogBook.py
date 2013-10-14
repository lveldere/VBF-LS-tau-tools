#!/usr/bin/env python

import sys,glob,os

################################################
#      read command line arguments
################################################
resdir = sys.argv[1]    # directory with results to log
texfile = sys.argv[2]   # path to output tex file

################################################
#      list pdf files in resdir and its subdirectories  
################################################
dirs = []                                             # list of directories
files = []                                            # 1 list of pdf files per directory

dirs.append(resdir)                                   # append the resdir itself
files.append(sorted(glob.glob(resdir + "/*.pdf")))    # list the pdf files in the resdir

for entry in sorted(glob.glob(resdir + "/*")):         # loop over all entries in resdir
    print entry
    if not os.path.isdir(entry):
        continue
    dirs.append(entry)                            # append the sub directories
    files.append(glob.glob(entry + "/*.pdf"))     # append the list of pdf files in the sub directory

################################################
#      create the tex file
#      write the preamble
################################################
TEXFILE = open(texfile,"w")
TEXFILE.write("\\documentclass[a4paper,11pt]{article}\n")
TEXFILE.write("\\usepackage{a4wide}\n")
TEXFILE.write("\\usepackage{graphicx}\n")
TEXFILE.write("\\usepackage{hyperref}                                                                 % entries in table of contents are made links\n")
TEXFILE.write("\\usepackage[format=plain,justification=raggedright,singlelinecheck=false]{caption}    % allows line break in captions\n")
TEXFILE.write("\\begin{document}\n")
TEXFILE.write("\\tableofcontents\n")
TEXFILE.write("\\newpage\n")

################################################
#      function that adds a section to the tex file  
################################################
def addLogSection(TEXFILE,title,figures):
    TEXFILE.write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
    TEXFILE.write("\\section{\\texttt{" + title.replace("_","\\_") + "}}\n")
    TEXFILE.write("\\newpage")
    TEXFILE.write("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")

    if len(figures) == 0:
        return

    for f in range(0,len(figures)):
        if f%2 == 0:
            TEXFILE.write("\\clearpage\n")
        fig = figures[f]
        TEXFILE.write("\\begin{figure}\n")
        TEXFILE.write("\\centering\n")
        TEXFILE.write("   \\includegraphics[height=0.3\\paperheight]{" + os.path.abspath(fig) + "}\n")
        TEXFILE.write("   \\caption{" + fig.replace("_","\\_").replace("/","/\\\\") + "}\n")
        TEXFILE.write("\\end{figure}\n")
    TEXFILE.write("\\clearpage\n")
    TEXFILE.write("\\newpage")

################################################
#      add one section per directory to the tex file
################################################
for d in range(0,len(dirs)):
    print dirs[d]
    addLogSection(TEXFILE,dirs[d].replace(os.path.split(dirs[0])[0],""),files[d])

################################################
#      finish the tex file
#      and close
################################################
TEXFILE.write("\end{document}\n")
TEXFILE.close()
