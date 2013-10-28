# check environment
if [ -z $MYSCRATCH ]; then
   echo "ERROR: please define a variable \$MYSCRATCH"
   return
fi

# some switches
project="VBF-LS-tau"
cmsswdir=$MYSCRATCH/$project-CMSSW                 # where to keep the CMSSW release ?
scratchdir=$MYSCRATCH/$project             # where is my scratch space ?
projectdir=$HOME/$project

# where are we?
pwd=$PWD

# check if project directory is free
if [ -d $projectdir ]; then
   echo "ERROR: project directory $projectdir already exists"
   return
fi
# check if scratch directory is free
if [ -d $scratchdir ]; then
   echo "ERROR: scratch directory $scratchdir already exists"
   return
fi
# check if cmssw directory is free
if [ -d $cmsswdir ]; then
   echo "ERROR: cmssw directory $cmsswdir already exists"
   return
fi

# setup cmssw area
echo "SETUP CMSSW"
mkdir $cmsswdir
cd $cmsswdir
ini cmssw
source $pwd/setup_cmssw_light.sh
cd $pwd

# get anascripts
echo "SETUP ANASCRIPTS"
export ANASCRIPTS=$HOME/anascripts
if [ ! -d $ANASCRIPTS ]; then
    echo "   RETRIEVING ANASCRIPTS"
    git clone https://github.com/lveldere/anascripts $HOME/anascripts
else
    echo "   ANASCRIPTS ALREADY AVAILABLE,"
    echo "   CONSIDER TO PULL IN THE LATEST VERSION THROUGH GIT"
fi
export PATH=$PATH:$ANASCRIPTS

# create project directory
echo "SETUP PROJECT DIRECTORY"
mkmyproject.py $projectdir $scratchdir

# setup analyzers
echo "SETUP ANALYZER DIRECTORY"
git clone https://github.com/rathjd/VBF-LS-tau-analyzer $projectdir/analyzers

# setup tools
echo "SETUP TOOLS"
git clone https://github.com/lveldere/VBF-LS-tau-tools $projectdir/tools

# retrieve sample lists
echo "SETUP SAMPLE LIST"
git clone https://github.com/lveldere/VBF-LS-tau-data $projectdir/data/VBF-LS-tau-data
rmdir $projectdir/data/samples
ln -s $projectdir/data/VBF-LS-tau-data/samples $projectdir/data/samples

# complete the setenv script
echo "export PATH=\$PATH:\$PROJECTDIR/tools/drawHist:\$PROJECTDIR/tools/scripts" &> $projectdir/setenv.sh
echo "export PYTHONPATH=\$PYTHONPATH:\$PROJECTDIR/tools/drawHist" &> $projectdir/setenv.sh

echo "PLEASE START FROM NEW SHELL AND RUN:"
echo "\$ source $projectdir/setenv.sh"
 