#!/usr/bin/env python3
###############################################################################
#
# @file PeerFactory.py
#
# @brief Eulerian Data Warehouse Peer Factory module. This module is aimed to
#        create new instance of Eulerian Data Warehouse Peer accordingly to
#        given command lines arguments.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 18/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import Eulerian.ObjectFactory class
#
from Eulerian.ObjectFactory import ObjectFactory
#
# Import Eulerian.File module
#
from Eulerian import File
#
# Import sys, getopt, copy and json modules
#
import sys, getopt, copy, json
#
# @brief Display PeerFactory usage
#
def usage() :
    print( File.read( "./conf/Peer.help" ) )
#
# @brief Create and setup a new instance of an Eulerian Data Warehouse Peer
#        matching given arguments.
#
# @param argv - Command line arguments.
#
# @return Eulerian Data Warehouse Peer instance.
#
def create( argv ) :
    peer_name = 'Eulerian.Edw.Peers.Rest'
    hook_name = 'Eulerian.Edw.Hooks.CSV'
    hook_options = None
    options = [
        'grid=', 'ip=', 'token=', 'accept=',
        'working-directory=', 'peer=', 'host=', 'ports=',
        'platform=', 'tokens=', 'unsecure',
        'hook=', 'hook-options=', 'help',
    ]

    # Parse command line arguments
    try :
        options, args = getopt.getopt( argv, '', options )
    except getopt.GetoptError as e:
        print( "Failed to parse command line. " + e.msg )
        usage()
        sys.exit( 2 )

    # Get Eulerian Data Warehouse Peer name from command line arguments
    for option, arg in options :
        if option == '--peer' :
            peer_name = arg

    # Create Peer instance
    peer = ObjectFactory.create( peer_name )

    # Setup peer attribute accordingly to given command line arguments
    for option, arg in options :
        if option == '--grid' :
            peer.set_grid( arg )
        elif option == '--ip' :
            peer.set_ip( arg )
        elif option == '--token' :
            peer.set_token( arg )
        elif option == '--accept' :
            peer.set_accept( arg )
        elif option == '--working-directory' :
            peer.set_wdir( arg )
        elif option == '--host' :
            peer.set_host( arg )
        elif option == '--ports' :
            peer.set_ports( arg.split( ',' ) )
        elif option == '--platform' :
            peer.set_platform( arg )
        elif option == '--tokens' :
            peer.set_tokens( arg )
        elif option == '--unsecure' :
            peer.set_secure( 0 )
        elif option == '--hook' :
            hook_name = arg
        elif option == '--hook-options' :
            hook_options = arg
        elif option == '--help' :
            usage()
            sys.exit( 0 )
 
     # Sanity check mandatory argument 'platform'
    platform = peer.get_platform()
    if platform is None :
        print( "Mandatory argument 'platform' is missing" )
        sys.exit( 22 )

    # Sanity check mandatory argument 'grid'
    if peer.get_grid() is None :
        print( "Mandatory argument 'grid' is missing" )
        sys.exit( 22 )

    # Sanity check mandatory argument 'ip'
    if peer.get_ip() is None :
        print( "Mandatory argument 'ip' is missing" )
        sys.exit( 22 )

    # Sanity check mandatory argument 'token'
    if peer.get_token() is None and peer.get_tokens() is None :
        print( "Mandatory argument 'token' or 'tokens' is missing" )
        sys.exit( 22 )

    # Create outputs hook
    hook = ObjectFactory.create( hook_name )

    # Setup outputs hook options
    if hook_options is not None :
        hook.set_options( File.read( hook_options ) )

    # Setup peer hook
    peer.set_hook( hook )

    # Deep copy remaining arguments
    args = copy.deepcopy( args )

    # Clear command line arguments
    del argv[:]

    # Append remaining args to argv
    argv.extend( args )

    return peer

