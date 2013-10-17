# some switches
cmsswdir=$HOME                 # where to keep the CMSSW release ?
scratch=$MYSCRATCH             # where is my scratch space ?

# read command line arguments
projectdir=$HOME/$1
if [ -z "$projectdir" ]; then
   echo "error: first command line argument: name of project directory to be created"
   return
fi

# where are we?
pwd=$PWD


# check if project directory is free
if [ -d $projectdir ]; then
   echo "ERROR: directory $HOME/$projectdir already exists"
   return
fi


# setup cmssw area
echo "\n SETUP CMSSW \n"
cd $cmsswdir
ini cmssw
source $pwd/setup_cmssw.sh
cd $pwd

# get anascripts
echo "\n RETRIEVING ANASCRIPTS \n"
export $ANASCRIPTS=$HOME/anascripts
if [ ! -d $ANASCRIPTS ]; then
    git clone https://github.com/lveldere/anascripts $HOME/anascripts
export PATH=$PATH:$ANASCRIPTS

# create project directory
mkmyproject.py $projectdir $scratch

# setup analyzers
git clone https://github.com/rathjd/VBF-LS-tau-analyzer $projectdir/analyzers

# setup tools
git clone https://github.com/lveldere/VBF-LS-tau-tools $projectdir/tools

# retrieve sample lists

# complete the setenv script
