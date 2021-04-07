#!/bin/bash
###############################################################################
#
# @brief Script used to perform Analytics Analysis on Eulerian Data Warehouse
#        Platform using python.
#
# @author THORILLON Xavier:x.thorillon@eulerian.com
#
# @date 24/03/2021
#
# version 1.0
#
###############################################################################
#
# Peer configuration file name
#
PEER_CONF_FILE='Peer.conf'
#
# Test for configuration file
#
if ! test -f "${PEER_CONF_FILE}"; then
  echo "Error : Can't find configuration file : ${PEER_CONF_FILE}"
  exit 2
fi
#
# Load configuration options
#
source ${PEER_CONF_FILE}
#
# Setup python command
#
CMD="python3 Peer.py"
#
# Script command usage
#
USAGE=$(cat << END
Usage :

./Peer.sh [options] <sqlfile>

With options :

-d : Turn on python debugger.

END
)
#
# Parse command lines argument.
#
while getopts ":d" option; do
  case "${option}" in
    d) CMD="${CMD} -m pdb ";;
    *) echo "${USAGE}"
       exit 2;;
  esac
done
#
# Remove used options
#
shift $((OPTIND-1))
#
# Add Eulerian grid of customer website to the command options.
#
CMD="${CMD} --grid=${GRID}"
#
# Add IP of the machine hosting this script to the command options.
#
CMD="${CMD} --ip=${IP}"
#
# Add Eulerian Authority platform name to the command options.
#
CMD="${CMD} --platform=${PLATFORM}"
#
# Add working directory to the command options.
#
CMD="${CMD} --working-directory=${WORKING_DIRECTORY}"
#
# If a hook class is provided, add hook class to the command options.
#
if [ -n "${HOOK}" ]; then
  CMD="${CMD} --hook=${HOOK}"
fi
#
# Add Hook options file to the command options.
#
CMD="${CMD} --hook-options=Hook.conf"
#
# If a Peer class is provided, add peer class to the command options
#
if [ -n "${PEER}" ]; then
  CMD="${CMD} --peer=${PEER}"
fi
#
# Set Host is provided, add host and ports to the command options.
#
if [ -n "${HOST}" ]; then
  CMD="${CMD} --host=\"${HOST}\""
  CMD="${CMD} --ports=\"${PORTS}\""
fi
#
# Setup secure / unsecure transport layer.
#
if [ -z "${SECURE}" ]; then
  CMD="${CMD} --unsecure";
elif [ -n "${SECURE}" ] && [ ${SECURE} == "no" ]; then
  CMD="${CMD} --unsecure";
fi
#
# Set Eulerian customer token
#
if [ -n "${TOKENS}" ];then
  CMD="${CMD} --tokens=${TOKENS}"
else
  CMD="${CMD} --token=${TOKEN}"
fi
#
# Run Peer.py
#
${CMD} $@
