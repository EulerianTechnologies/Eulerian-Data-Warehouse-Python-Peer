#!/usr/bin/env python3
###############################################################################
#
# @brief Eulerian Data Warehouse Peer Hook class definition.
#
# A Peer Hook is the base class of objects used to transform the reply of
# an Analytics Analysis into events.
#
# Hook.on_headers() : Called to mark the begin of Analytics analysis.
#                      It provides Analytics Analysis attributes. 
#                      ie : UUID of the Analysis, timerange of the
#                      analysis, formulas with their matching computed type.
#
# Hook.on_add() : Called for each Analytics analysis records.
#
# Hook.on_status() : Called at the end of an analysis or on error.
#
# @author THORILLON Xavier : x.thorillon@eulerian.com
#
# @date 07/04/2021
#
# @version 1.0
#
###############################################################################
#
# Import json
#
import json
#
# @brief Eulerian Data Warehouse Peer Hook base class definition.
#
# @class Eulerian.Edw.Hook
#
class Hook :
    #
    # @brief Hook instance initializer.
    #
    # @param self - Hook instance.
    #
    def __init__( self ) :
        self.__options = None
    #
    # @brief Set Hook options.
    #
    # Hook options are used to provide parameters to the Hook, those 
    # parameters can be either a valid JSON encoded string or a
    # dictionnary.
    #
    # @param self - Hook instance.
    # @param options - Hook options.
    #
    def set_options( self, options ) :
        if isinstance( options, dict ) :
            # Dictionnary is used verbatim
            self.__options = options
        else :
            # Expect a valid encoded JSON string
            try :
                self.__options = json.loads( options )
            except ValueError as e:
                print( "Error : Hook.set_options() : " + str( e ) )
    #
    # @brief Get Hook options.
    #
    # @param self - Hook instance.
    #
    # @return Hook options.
    #
    def get_options( self ) :
        return self.__options
    #
    # @brief Interface definition of the function used to export Analytics
    #        rows.
    #
    # @param self - Hook instance.
    # @param uuid - Analysis UUID.
    # @param rows - Analysis rows.
    #
    def on_add( self, uuid, rows ) :
        pass
    #
    # @brief Interface definition of the function used to start export of
    #        an Analytics Analysis.
    #
    # @param self - Hook instance.
    # @param uuid - Analysis UUID.
    # @param headers - Analysis columns headers.
    #
    def on_headers( self, uuid, timerange, headers ) :
        pass
    #
    # @brief Interface definition of the function used to end an Analytics
    #        Analysis.
    #
    # @param self - Hook instance.
    # @param uuid - Analysis UUID.
    #
    def on_status( self, uuid ) :
        pass
