#!/usr/bin/env python3
###############################################################################
#
# @file Rest.py
#
# @brief Eulerian Data Warehouse Rest Peer class definition. This class is used
#        to request Eulerian Data Warehouse Rest services.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 18/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import base Peer class definition
#
from Eulerian.Edw.Peer import Peer as Peer
#
# Import Eulerian.Authority class used to get authorization tokens
#
from Eulerian.Authority import Authority
#
# Import Eulerian.ObjectFactory class used to create object
#
from Eulerian.ObjectFactory import ObjectFactory
#
# Import Eulerian File used to read files
#
from Eulerian import File
#
# Import every Eulerian.Edw.Parsers modules
#
#from Eulerian.Edw import Parsers
#
# Import requests, time, json, socket modules
#
import requests, time, json, socket, re, json
#
# Import datetime
#
from datetime import datetime
#
# @brief Eulerian Data Warehouse Rest Peer class definition.
#
# @class Rest
#
class Rest( Peer ) :
    "Eulerian Data Warehouse Rest Peer Class"
    #
    # @brief Get remote URL to Eulerian Data Warehouse Services.
    #
    # @param self - Eulerian.Edw.Peers.Rest instance.
    #
    # @return URL to Eulerian Data Warehouse Services.
    #
    def url( self ) :
        # Add protocol accordingly to secure mode
        url = 'https://' if self.get_secure() else 'http://'
        # There is a trick, every platform doesnt listen on same ports
        # Even the url isnt built with the same format
        platform = self.get_platform()
        host = self.get_host()
        if host is not None :
            url += host + ':' 
            url += self.get_ports()[ self.get_secure() ]
        elif platform == 'france' :
            url += 'edw.ea.eulerian.com'
        else :
            url += self.get_grid() + '.'
            url += Authority.DOMAINS[ platform ]
        url += '/edw/jobs'
        return url
    #
    # @brief Get Authorization bearer value from Eulerian Authority service.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    #
    # @return Authorization bearer.
    #
    def bearer( self ) :
        token = self.get_token()
        grid = self.get_grid()
        if token is None :
            tokens = json.loads( File.read( self.get_tokens() ) )
            token = tokens[ grid ]
        return Authority.bearer(
            self.get_kind(), self.get_platform(), grid,
            self.get_ip(), token
            )
    #
    # @brief Get HTTP header
    #
    # @param self - Eulerian.Edw.Peers.Rest instance.
    #
    # @return headers
    #
    def headers( self ) :
        bearer = self.bearer()
        if bearer is None :
            print(
                "Error : " + Rest.headers.__qualname__ +
                "() failed. bearer is invalid"
                )
            return None
        else :
            return {
                'Authorization' : bearer,
                'Content-Type'  : self.get_accept(),
            }
    #
    # @brief Get current Date time.
    #
    # @param self - Eulerian.Edw.Peers.Rest instance.
    # 
    # @return Current Date time.
    #
    def now( self ) :
        return datetime.now().strftime( "%d/%m/%Y %H:%M:%S" );
    #
    # @brief Get body of HTTP request used to create a new JOB on Eulerian
    #        Data Warehouse Platform.
    #
    # @param self - Eulerian.Edw.Peers.Rest instance.
    # @param command - Eulerian Data Warehouse command.
    #
    # @return body
    #
    def body( self, command ) :
        return json.dumps( {
            'kind'  : 'edw#request',
            'query' : command,
            'creationTime' : self.now(),
            'location' : socket.gethostname(),
            'expiration' : None,
        } )
    #
    # @brief Display error.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param what - What did failed.
    # @param reply - Last reply from Eulerian Data Warehouse Services.
    #
    def error( self, what, reply ) :
        json = reply.json()
        error  = 'Failed to ' + what + '. Code : '
        error += str( reply.status_code ) + '\n'
        error += ', domain  : ' + json[ 'data' ][ 0 ] + '\n'
        error += ', layer   : ' + json[ 'data' ][ 1 ] + '\n'
        error += ', message : ' + json[ 'data' ][ 2 ] + '\n'
        error += ', code    : ' + json[ 'data' ][ 3 ]
        print( error )
    #
    # @brief Create a new job on Eulerian Data Warehouse Services.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param command - Eulerian Data Warehouse Command.
    #
    # @return JSON reply message
    #
    def create( self, command ) :
        headers = self.headers()
        if headers is None :
            print(
                "Error : " + Rest.create.__qualname__ +
                "() failed. Header is invalid"
                )
            return None
        else :
            reply = requests.post(
                self.url(), headers = headers,
                data = self.body( command )
                )
            json = reply.json()
            if reply.status_code != 200 :
                self.error( "Create a new JOB", reply )
                json = None
            return json
    #
    # @brief Get job status on Eulerian Data Warehouse Services.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param reply - Previous reply received from Eulerian Data Warehouse.
    #
    # @return JSON reply message
    #
    def status( self, reply ) :
        reply = requests.get(
            reply[ 'data' ][ 1 ], headers = self.headers()
            )
        json = reply.json()
        if reply.status_code != 200 :
            self.error( "Get JOB status", reply )
            json = None
        return json
    #
    # @brief Get parser dedicated to current accepted reply format.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    #
    # @return Parser
    #
    def parser( self ) :
        parser = None
        pattern = re.compile( '\w+$' )
        search = pattern.search( self.get_accept() )
        name = 'Eulerian.Edw.Parsers.'
        if not search is None :
            name += search.group().title()
            parser = ObjectFactory.create( name )
        return parser
    #
    # @brief Get local reply file path.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param url - Reply URL.
    #
    # @return Local path to reply file.
    #
    def path( self, url ) :
        pattern = re.compile( "\d*\.\w*$" )
        search = pattern.search( url )
        if not search is None :
            return self.get_wdir() + '/' + search.group()
        else :
            return None
    #
    # @brief Store Job reply result in working directory.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param url - Reply URL.
    # @param reply - Last reply received from Eulerian Data Warehouse.
    #
    def store( self, url, reply ) :
        path = self.path( url )
        out = open( path, "wb" )
        if out is None :
            self.error( "Store JOB results", reply )
        else :
            out.writelines( reply.iter_content( 1024 ) )
            out.close()
        return path
    #
    # @brief Get job result on Eulerian Data Warehouse Services.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param reply - Last reply received from Eulerian Data Warehouse.
    #
    def download( self, reply ) :
        path = None
        url = reply[ 'data' ][ 1 ]
        reply = requests.get( 
            url, headers = self.headers(), stream = True
            )
        if reply.status_code == 404 :
            print( "Failed to get " + url + ". Not found" )
        elif reply.status_code != 200 :
            self.error( "Get JOB results", reply )
        else :
            path = self.store( url, reply )
        return path
    #
    # @brief Parse Job results
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param path - Path to Job result
    #
    def parse( self, path ) :
        parser = self.parser()
        if parser is not None :
            parser.do( path, self.get_hook() )
    #
    # @brief Request Eulerian Data Warehouse Services.
    #
    # @param self - Eulerian Data Warehouse Rest Peer.
    # @param command - Eulerian Data Warehouse command.
    #
    def request( self, command ) :
        # Create a new JOB
        reply = self.create( command )
        if reply is None :
            print(
                "Error : " + Rest.request.__qualname__ +
                "() failed. Job creation failed."
                )
            return
        status = reply[ 'status' ]
        while status == 'Running' :
            # Get JOB status
            reply = self.status( reply )
            if reply is None :
                status = 'Error'
            else :
                status = reply[ 'status' ]
                time.sleep( 1 )
        if status != 'Done' :
            self.error( 'Get JOB status', reply )
        else :
            # Download JOB response
            path = self.download( reply )
            if path is not None :
                # Parse JOB response
                self.parse( path )
