#!/usr/bin/env python3
###############################################################################
#
# @file Json.py
#
# @brief
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 06/04/2021
#
# @version 1.0
#
###############################################################################
from Eulerian.Edw.Parser import Parser
from Eulerian.Edw.Parser import Error
#
# Import JSON parser
#
import ijson
#
# @brief
#
# @class Eulerian.Edw.Parsers.Json.Error
#
#class Error( Exception ) :
#    "JSON Parse Error Class"
    #
    # @brief
    #
    # @param self -
    # @param error - 
    #
#    def __init__( self, error ) :
#        self.__error = error
    #
    # @brief
    #
    # @param self -
    #
    # @return Error string.
    #
#    def __str__( self ) :
#        return "JSON Parse error : " + self.__error
#
# @brief
#
# @class Eulerian.Edw.Parsers.Json
#
class Json( Parser ) :
    "Eulerian Data Warehouse JSON parser Class"
    #
    # JSON events
    #
    events = None
    #
    # Analytics UUID
    #
    uuid = 0
    #
    # @brief
    #
    # @param self -
    # @param what -
    # @param value -
    #
    @classmethod
    def expect( self, what ) :
        event, value = next( self.events )
        if event != what :
            error  = "Expected '" + what 
            error += "' got '" + event + "'"
            raise Error( error )
        return value
    #
    # @brief
    #
    # @param self
    #
    # @return String value.
    #
    @classmethod
    def string( self ) :
        return self.expect( 'string' )
    #
    # @brief
    #
    # @param self -
    # 
    @classmethod
    def object_start( self ) :
        self.expect( 'start_map' )
    #
    # @brief
    #
    # @param self -
    #
    @classmethod
    def object_key( self, key ) :
        value = self.expect( 'map_key' )
        if value != key :
            error  = "Expected key : '" + key 
            error += "' got '" + value + "'"
            raise Error( error )
    #
    # @brief
    #
    # @param self -
    # @param key -
    # @param string -
    #
    @classmethod
    def object_string( self, key, string ) :
        self.object_key( key )
        value = self.string()
        if value != string :
            error  = "Expected string : '" + string 
            error += "' got '" + value + "'"
            raise Error( error )
    #
    # @brief
    #
    # @param self -
    # @param key -
    # @param strings -
    #
    @classmethod
    def object_strings( self, key, strings ) :
        self.object_key( key )
        string = self.string()
        match = string in strings
        if not match :
            error  = "Expected strings( " + ' '.join( strings )
            error += " ) got '" + string + "'"
            raise Error( error )
        return string
    # 
    # @brief
    #
    # @param self
    # @param key
    #
    # @return value
    #
    @classmethod
    def object_value( self, key ) :
        self.object_key( key )
        return self.string()
    #
    # @brief
    #
    # @param self - 
    # 
    @classmethod
    def object_end( self ) :
        self.expect( 'end_map' )
    #
    # @brief
    #
    # @param self - 
    # 
    @classmethod
    def array_start( self ) :
        self.expect( 'start_array' )
    #
    # @brief
    #
    # @param self
    #
    # @return
    #
    @classmethod
    def array_next( self ) :
        event, value = next( self.events )
        if event == 'end_array' : return None, None
        else : return event, value
    #
    # @brief
    #
    # @param self
    #
    # @return
    #
    @classmethod
    def array_value( self ) :
        return self.string()
    #
    # @brief
    #
    # @param self - 
    # 
    @classmethod
    def array_end( self ) :
        self.expect( 'end_array' )
    #
    # @brief
    #
    # @param self -
    # @param hooks -
    #
    @classmethod
    def headers( self, hooks ) :
        self.object_key( 'headers' )
        self.object_start()
        self.uuid = self.object_value( 'uuid' )
        begin = self.object_value( 'from' )
        end = self.object_value( 'to' )
        columns = []
        self.object_key( 'schema' )
        self.array_start()
        while True :
            event, value = self.array_next()
            if event is None : break
            type = self.array_value()
            column = self.array_value()
            columns.append( [ type, column ] )
            self.array_end()
        self.object_end()
        hooks.on_headers( self.uuid, [ begin, end ], columns )
    #
    # @brief
    #
    # @param self
    #
    # @return row
    #
    @classmethod
    def row( self ) :
        row = []
        while True :
            event, value = self.array_next()
            if event is None : break
            elif value is None : row.append( 'NULL' )
            else : row.append( value.encode( 'utf8' ) )
        return row
    #
    # @brief
    #
    # @param self
    #
    @classmethod
    def rows( self, hooks ) :
        #
        # 'rows' : [
        #  [ <value1>, <value2>, ..., <valueX> ],
        #  [
        #   [ <value>, <value2>, ..., <valueX> ],
        #   [ <value>, <value2>, ..., <valueX> ],
        #  ]
        # ]
        #
        self.object_key( 'rows' )
        self.array_start()
        while True :
            rows = []
            event, value = self.array_next()
            if event is None : break
            rows.append( self.row() )
            hooks.on_add( self.uuid, rows )
    #
    # @brief
    #
    # @param self
    # @param hooks
    #
    @classmethod
    def error( self ) :
        pass
    #
    # @brief
    #
    # @param self
    # @param hooks
    #
    @classmethod
    def status( self ) :
        pass
    #
    # @brief
    #
    # @param self -
    # @param path -
    # @param hooks -
    #
    @classmethod
    def do( self, path, hooks ) :
        stream = open( path, 'r' )
        self.events = ijson.basic_parse( stream )
        self.uuid = 0
        try :
            self.object_start()
            self.object_string( 'kind', 'edw#response' )
            status = self.object_strings( 'status', [ 'Done', 'Error' ] )
            if status == 'Error' :
                self.error()
            else :
                self.headers( hooks )
                self.rows( hooks )
                self.object_end()
                #self.status()
        except Error as e :
            print( e )

