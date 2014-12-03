from __future__ import with_statement

__author__ = 'Dorbian'
__product__ = 'Kaidame'
__version__ = '0.0.1'

#Imports from the module itself
from Lib import *
from Core import *
from Core import Loch

#global imports
#import Processing

#Processing = Processing.Processing()
#Processing.name = __product__
#True False statements
__initialized__ = debugging = update = tracing = False
#Empty string statements
configfile = rundir = logdir = datadir = dbasefile = dbfunc = ''
#Empty lists
options = args = process = []
#Empty functions
logwriter = log = None
#Empty dicts
tmpd = dict()


logwriter = Loch()
logwriter.initialize()


def log(msg, inf):
    logwriter.log(msg, inf)


def initialize():
    #Set all variables needed as global variables
    global __initialized__, debugging, rundir, options, args, datadir, logdir, dbasefile, configfile, dbfunc, \
        tracing, process, __product__, __version__

    #add to the sys path for convenience

    __version__ = __version__
    __product__ = __product__
    rundir = get_rundir()
    sys.path.insert(0, rundir)

    #log = Core.log

    log("Initializing {0} {1}".format(__product__, __version__), "INFO")

    #Set some directories
    datadir = os.path.join(rundir, 'Data')
    logdir = os.path.join(datadir, 'Logs')

    #process = processing()

    #Set some files
    configfile = os.path.join(datadir, 'config.ini')
    dbasefile = os.path.join(datadir, 'Kaidame.sqlite')

    dbfunc = dbmod()

    #check if arguments where passed
    optsargs()

    debugging = True
    tracing = True

    kaidame.Core.Loch._debug = debugging
    kaidame.Core.Loch._trace = tracing

    __initialized__ = True
    #threadlock.release()
    return True


def start():
    if __initialized__:
        log("Connecting to database 1", "INFO")
        dbfunc.connect()