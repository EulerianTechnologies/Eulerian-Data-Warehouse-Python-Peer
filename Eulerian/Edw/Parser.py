#!/usr/bin/env python3
###############################################################################
#
# @file Parser.py
#
# @brief Eulerian Data Warehouse Parser base class definition.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 06/04/2021
#
# @version 1.0
#
###############################################################################
#
# @brief Eulerian Data Warehouse Parse Error class definition.
#
# @class Eulerian.Edw.Parser.Error
#
class Error :

    def __init__( self, error ) :
        self.__error = error

    def __str__( self ) :
        return str( self.__class__ ) + '\n' + '\n'.join( ( str( item ) + ' = ' + str( self.__dict__[ item ] ) for item in sorted( self.__dict__ ) ) )
#
# @brief Eulerian Data Warehouse Parser base class definition.
#
# @class Parser
#
class Parser :
    # 
    # @brief Parse given file and call matching hooks functions.
    #
    # @param self - Eulerian.Edw.Parser instance.
    # @param path - File path.
    # @param hooks - Eulerian Data Warehouse Peer Hooks instance.
    #
    def do( self, path, hooks ) :
        pass
