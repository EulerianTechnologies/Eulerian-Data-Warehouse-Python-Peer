###############################################################################
#
# @brief CSV Hooks of Eulerian Data Warehouse Peer.
#
# @author x.thorillon@eulerian.com
#
# @date 31/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import Eulerian.Edw.Hook class
#
from Eulerian.Edw.Hook import Hook
#
# Import sys and os module
#
import sys, os
#
# @brief
#
# @class CSV
#
class CSV( Hook ) :
    #
    # @brief Default terminal size.
    #
    DEFAULT_TERMINAL_SIZE = 80
    #
    # @brief Get hooks options.
    #
    # @param self - CSV hooks.
    #
    # @return options
    #
    def get_options( self ) :
        return Hook.get_options( self )
    #
    # @brief Set CSV options.
    #
    # @param self - CSV instance.
    # @param options - String options
    #
    def set_options( self, options ) :
        Hook.set_options( self, options )
        options = self.get_options()
        if options is None :
            print( "CSV hooks isnt set" )
            sys.exit( 2 )
        elif 'separator' not in options :
            print( "CSV hooks separator isn't set" )
            sys.exit( 2 )
        if 'sizes' not in options :
            if 'term_size' not in options :
                if sys.stdout.isatty() :
                    options[ 'term_size' ] = os.get_terminal_size( 0 )[ 0 ]
                else :
                    options[ 'term_size' ] = self.DEFAULT_TERMINAL_SIZE
    #
    # @brief
    #
    # @param self - CSV instance.
    # @param uuid - Analysis UUID.
    # @param rows - Analysis results rows.
    #
    def on_add( self, uuid, rows ) :
        options = self.get_options()
        separator = options[ 'separator' ]
        sizes = options[ 'sizes' ]
        for row in rows :
            string = '' 
            for col, size in zip( row, sizes ) :
                if type( col ) is bytes :
                    col = col.decode()
                format = '{0: >{width}}'.format( col, width=size )
                string += format
                string += separator
            print( string )
    #
    # @brief
    #
    # @param self -
    #
    def dispose( self ) :
        pass
    #
    # @brief
    #
    # @param self - CSV instance.
    # @param uuid - Analysis UUID.
    # @param timerange - Analysis timerange
    #
    def on_headers( self, uuid, timerange, headers ) :
        SIZES = {
             'UNKNOWN' : 4,  # NULL
             'UINT8'   : 3,  # 255
              'INT8'   : 4,  # -128
            'UINT16'   : 5,  # 32767
             'INT16'   : 6,  # -32768
            'UINT32'   : 10, # 4294967295
             'INT32'   : 11, # -2147483648
            'UINT64'   : 21, # 18446744073709551615
             'INT64'   : 21, # -9223372036854775808
             'DOUBLE'  : 10, # 10.3f
             'FLOAT'   : 10, # 10.3f
             'STRING'  : -1, # Elastics
        }
        options = self.get_options()
        separator = options[ 'separator' ]

        if 'sizes' not in options :
            term_size = options[ 'term_size' ]
            headers_count = len( headers )

            # Compute row size using headers types
            separator_size = len( separator )

            elastics_count = 0
            fixed_size = 0
            for type, header in headers :
                if SIZES[ type ] == -1 :
                    elastics_count += 1
                else :
                    fixed_size += SIZES[ type ]
            separators_size = separator_size * ( headers_count - 1 )
            elastics_size = term_size - ( fixed_size + separators_size )
            elastics = []

            if elastics_size > elastics_count :
                elastics_average = elastics_size / elastics_count
                elastics_average = round( elastics_average )
                while elastics_size != 0 :
                    size = elastics_average if elastics_size >= elastics_average else elastics_size
                    elastics.append( size )
                    elastics_size -= size
            else :
                # Doesnt fit into terminal
                print(
                    "Doesnt fit : \n" + 
                    "TERM_SZ    : " + str( term_size ) +
                    "FIXED_SZ   : " + str( fixed_size ) + 
                    "SEPS_SZ    : " + str( separators_size ) + 
                    "ELASTIC_SZ : " + str( elastics_size )
                    )
                sys.exit( 2 )
            options[ 'sizes' ] = sizes = []
            for type, header in headers :
                size = SIZES[ type ]
                if size == -1 :
                    sizes.append( elastics.pop( 0 ) - 1 )
                else :
                    sizes.append( size - 1 )
    #
    # @brief
    #
    # @param self
    # @param uuid
    #
    def on_status( self, uuid ) :
        print( "on_status()" )
        pass
