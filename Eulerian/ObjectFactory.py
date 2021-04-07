#!/usr/bin/env python3
###############################################################################
#
# @file ObjectFactory.py
#
# @brief Object Factory class definition. This class is used to load the 
#        module and create object instance from a given string.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 06/04/2021
#
# @version 1.0
#
###############################################################################
#
# @brief Object factory class definition.
#
# @class Eulerian.ObjectFactory
#
class ObjectFactory :
    #
    # @brief Import and return matching module.
    #
    # @param self - Eulerian.ObjectFactory class
    # @param name - Object class name.
    #
    # @return Module or None.
    #
    @classmethod
    def module( self, name ) :
        parts = name.split( '.' )
        copy = parts[ : ]
        while copy :
            try :
                module = __import__( '.'.join( copy ) )
                break
            except ImportError :
                del copy[ -1 ]
                if not copy : raise
        parts = parts[ 1: ]
        for part in parts :
            parent, module = module, getattr( module, part )
        return module
    #
    # @brief Import module and create a new instance of class.
    #
    # @param self - Eulerian.ObjectFactory class.
    # @param name - Object class name.
    #
    # @return Instance of given class or None.
    #
    @classmethod
    def create( self, name ) :
        object = None
        module = self.module( name )
        if module is not None :
            module = getattr( module, name.split( '.' )[ -1 ] )
            object = module()
        return object
