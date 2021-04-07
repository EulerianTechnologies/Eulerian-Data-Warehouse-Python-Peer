#!/usr/bin/env python3
###############################################################################
#
# @file File.py
#
# @brief Eulerian File module definition. This module regroup a set of file 
#        operations.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 06/04/2021
#
# @version 1.0
#
###############################################################################
#
# Import sys module
#
import sys
#
# @brief Read and return content of given file path.
#
# @param path - File path.
#
# @return File content.
#
def read( path ) :
    try :
        # Open file for reading
        f = open( path, "r" )
        # Read file content
        data = f.read()
        # Close file
        f.close()
    except IOError as e :
        print( str( e ) )
        sys.exit( 2 )
    return data
