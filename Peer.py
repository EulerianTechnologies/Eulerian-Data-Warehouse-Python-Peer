#!/usr/bin/env python3
###############################################################################
#
# @file Peer.py
#
# @brief Main entry point of the python script used to perform Eulerian Data
#        Warehouse Analysis.
#
# usage :
#
# ./Peer.py [ options ] <Command file path>
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 18/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import Eulerian.Edw.PeerFactory
#
from Eulerian.Edw import PeerFactory as Factory
#
# Import Eulerian.File
#
from Eulerian import File as File
#
# Import sys package
#
import sys
#
# @brief Main entry point of the script.
#
# @param argv - Command line arguments
#
def main( argv ) :
    # Create a new Peer
    peer = Factory.create( argv )
    if peer is not None :
        # Remaining arguments are paths to command files.
        for arg in argv :
            peer.request( File.read( arg ) )
#
# Forward script execution on main function
#
if __name__ == '__main__' :
    main( sys.argv[ 1: ] )
