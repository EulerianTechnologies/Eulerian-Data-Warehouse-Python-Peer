#!/usr/bin/env python3
###############################################################################
#
# @file Authority.py
#
# @brief Eulerian Authority class definition. This class is used to request 
#        Eulerian Authority services for session or access tokens. Those 
#        tokens are mandatory to request Eulerian Data Warehouse Services.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 19/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import third party packages
#
import requests, json
#
# Import IntEnum
#
from enum import IntEnum
#
# @brief Eulerian Authority Token kind class definition.
#
# @class AuthorityKind
#
class AuthorityKind( IntEnum ) :
    SESSION = 1
    ACCESS = 2
#
# @brief Eulerian Authority class definition.
#
# @class Authority
#
class Authority :
    #
    # Setup Eulerian Authority domains.
    #
    DOMAINS = {
        'dev'    : 'api.erdev-next.eulerian.com',
        'france' : 'api.eulerian.com',
        'canada' : 'api.eulerian.ca',
    }
    #
    # Setup Name of token column name read from Eulerian Authority reply 
    #
    COLUMNS = {
        AuthorityKind.SESSION : 'session_token',
        AuthorityKind.ACCESS  : 'access_token',
    }
    #
    #  Setup path on Eulerian Authority server matching token type
    #
    PATHS = {
        AuthorityKind.SESSION : '/er/account/get_dw_session_token.json?ip=',
        AuthorityKind.ACCESS  : '/er/account/get_dw_access_token.json?ip=',
    }
    #
    # @brief Create URL to Eulerian Authority service.
    #
    # @param klass - Eulerian.Authority class.
    # @param kind - Eulerian Authority token kind.
    # @param platform - Eulerian Authority platform name.
    # @param grid - Eulerian Customer grid.
    # @param ip - Eulerian Customer IP used to query Eulerian Data Warehouse
    #             Services.
    # @param token - Eulerian Customer token.
    #
    @classmethod
    def url( klass, kind, platform, grid, ip, token ) :
        domain = Authority.DOMAINS[ platform ]
        if not domain is None :
            url  = 'https://'
            url += grid + '.'
            url += domain + '/ea/v2/'
            url += token + Authority.PATHS[ kind ]
            url += ip + '&output-as-kv=1'
            return url
        else :
            return None
    #
    # @brief Request Eulerian Authority services for a bearer token. This token
    #        is mandatory to request Eulerian Data Warehouse Services.
    #
    # @param klass - Eulerian.Authority class.
    # @param kind - Eulerian Authority token kind.
    # @param platform - Eulerian Authority platform name.
    # @param grid - Eulerian Customer grid.
    # @param ip - Eulerian Customer IP used to query Eulerian Data Warehouse
    #             Services.
    # @param token - Eulerian Customer token.
    #
    # @return Bearer token
    #
    @classmethod
    def bearer( klass, kind, platform, grid, ip, token ) :
        url = Authority.url( kind, platform, grid, ip, token )
        reply = requests.get( url )
        if reply.status_code == 200 :
            json = reply.json()
            if json[ 'error' ] == True :
                print(
                    "Error : " + Authority.bearer.__qualname__ +
                    "() failed. " + json[ 'error_msg' ]
                    )
                return None
            row = json[ 'data' ][ 'rows' ][ 0 ]
            column = Authority.COLUMNS[ kind ]
            bearer = 'bearer '
            bearer += row[ column ]
            return bearer
        else :
            return None
