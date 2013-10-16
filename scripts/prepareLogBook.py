#!/usr/bin/env python

import sys,glob,os

################################################
#      read command line arguments
################################################
resdir   = sys.argv[1].rstrip("/")                        # directory with results to log
texfile  = sys.argv[2]                                    # path to output tex file

################################################
#      list pdf files in resdir and its subdirectories  
################################################
resdirs = []                                               # list of directories
resfiles = []                                              # 1 list of pdf files per directory

def addResDir(dir,resdirs,resfiles):
    resdirs.append(dir)                                    # add the directory
    resfiles.append(sorted(glob.glob(dir + "/*.pdf")))  # list the pdf files in the resdir
    for subdir in sorted(glob.glob(dir + "/*")):           # loop over all entries in resdir
        if os.path.isdir(subdir):
            addResDir(subdir,resdirs,resfiles)             # add directories recursively

addResDir(resdir,resdirs,resfiles)
print resdirs
for entry in resfiles:
    print entry

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
def addLogSection(TEXFILE,title,figures,captions):
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
        cap = captions[f]
        TEXFILE.write("\\begin{figure}\n")
        TEXFILE.write("\\centering\n")
        TEXFILE.write("   \\includegraphics[height=0.3\\paperheight]{" + os.path.abspath(fig) + "}\n")
        TEXFILE.write("   \\caption{" + cap.replace("_","\\_").replace("/","/\\\\") + "}\n")
        TEXFILE.write("\\end{figure}\n")
    TEXFILE.write("\\clearpage\n")
    TEXFILE.write("\\newpage")

################################################
#      add one section per directory to the tex file
################################################
for d in range(0,len(resdirs)):
    title = resdirs[d].replace(os.path.split(resdirs[0])[0],"").lstrip("/")
    files = resfiles[d]
    captions = [file.replace(os.path.split(resdirs[0])[0],"").lstrip("/") for file in files]
    addLogSection(TEXFILE,title,files,captions)

################################################
#      finish the tex file
#      and close
################################################
TEXFILE.write("\end{document}\n")
TEXFILE.close()
