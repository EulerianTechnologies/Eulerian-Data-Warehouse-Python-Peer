#!/usr/bin/env python3
###############################################################################
#
# @file Peer.py
#
# @brief Eulerian Data Warehouse Peer Base class type definition.
#
# @author Thorillon Xavier:x.thorillon@eulerian.com
#
# @date 18/03/2021
#
# @version 1.0
#
###############################################################################
#
# Import Eulerian.AuthorityKind
#
from Eulerian.Authority import AuthorityKind
#
# @brief Eulerian Data Warehouse Peer Base class.
#
# @class Eulerian.Edw.Peer
#
class Peer :
    "Eulerian Data Warehouse Peer Class"
    #
    # @brief Allocate and initialize a new Peer instance.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    def __init__( self ) :
        self.__kind = AuthorityKind.ACCESS
        self.__accept = 'application/json'
        self.__hook = None
        self.__tokens = None
        self.__token = None
        self.__host = None
        self.__ports = None
        self.__platform = None
        self.__grid = None
        self.__secure = 1 
        self.__ip = None
        self.__wdir = None
    #
    # @brief Set remote host.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param host - Remote host name.
    #
    def set_host( self, host ):
        self.__host = host
    #
    # @brief Get remote host.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Remote host name.
    #
    def get_host( self ) :
        return self.__host
    #
    # @brief Set remote ports.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param ports - Remote ports.
    #
    def set_ports( self, ports ):
        self.__ports = ports
    #
    # @brief Get remote ports.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Remote ports.
    #
    def get_ports( self ) :
        return self.__ports
    #
    # @brief Set remote platform
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param platform - Remote platform.
    #
    def set_platform( self, platform ):
        self.__platform = platform
    #
    # @brief Get remote platform.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Remote platform name.
    #
    def get_platform( self ) :
        return self.__platform
    #
    # @brief Set customer grid name.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param grid - Customer grid name.
    #
    def set_grid( self, grid ):
        self.__grid = grid
    #
    # @brief Get customer grid name.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Customer grid name.
    #
    def get_grid( self ) :
        return self.__grid
    #
    # @brief Set secure remote transport.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param secure - Secure remote transport flag
    #
    def set_secure( self, secure ):
        self.__secure = secure
    #
    # @brief Get customer grid name.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Customer grid name.
    #
    def get_secure( self ) :
        return self.__secure
    #
    # @brief Set Peer IP.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param ip - Peer IP.
    #
    def set_ip( self, ip ):
        self.__ip = ip
    #
    # @brief Get customer IP address.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Customer IP address.
    #
    def get_ip( self ) :
        return self.__ip
    #
    # @brief Set Peer accept reply format.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param accept - Accept reply format.
    #
    def set_accept( self, accept ) :
        self.__accept = accept
    #
    # @brief Get Peer accept reply format.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Accept reply format.
    #
    def get_accept( self ) :
        return self.__accept
    #
    # @brief Set Peer working directory path.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param wdir - Working directory path.
    #
    def set_wdir( self, wdir ) :
        self.__wdir = wdir
    #
    # @brief Get Peer working directory path.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Working directory path.
    #
    def get_wdir( self ) :
        return self.__wdir
    #
    # @brief Set Authorization token kind.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param kind - Authorization token kind.
    #
    def set_kind( self, kind ) :
        self.__kind = kind
    #
    # @brief Get Authorization token kind.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Authorization token kind.
    #
    def get_kind( self ) :
        return self.__kind
    #
    # @brief Set Eulerian token used to request Eulerian Authority.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param token - Eulerian token.
    #
    def set_token( self, token ) :
        self.__token = token
    #
    # @brief Get Eulerian token used to request Eulerian Authority.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Eulerian token.
    #
    def get_token( self ) :
        return self.__token
    #
    # @brief Set Eulerian tokens file path used to request Eulerian Authority.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param tokens - Eulerian tokens file path.
    #
    def set_tokens( self, tokens ) :
        self.__tokens = tokens
    #
    # @brief Get Eulerian tokens file path used to request Eulerian Authority.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Eulerian tokens file path.
    #
    def get_tokens( self ) :
        return self.__tokens
    #
    # @brief Set Eulerian output Hooks.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param hook - Eulerian output hook.
    #
    def set_hook( self, hook ) :
        self.__hook = hook
    #
    # @brief Get Eulerian output hook.
    #
    # @param self - Eulerian Data Warehouse Peer.
    #
    # @return Eulerian output hook.
    #
    def get_hook( self ) :
        return self.__hook
    #
    # @brief base function used to send request to Eulerian Data 
    #        Warehouse Services.
    #
    # @param self - Eulerian Data Warehouse Peer.
    # @param command - Eulerian Data Warehouse command.
    #
    def request( self, command ) :
        pass
