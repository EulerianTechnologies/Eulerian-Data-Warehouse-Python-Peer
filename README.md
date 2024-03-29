<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/EulerianTechnologies/Eulerian-Data-Warehouse-Python-Peer">
    <img src="./images/Eulerian-logo.gif" alt="Logo">
  </a>
  <h3 align="center">Eulerian Data Warehouse Python Peer</h3>
  <p align="center">
    The Python Peer is used to request Eulerian Data Warehouse Services.
    <br />
    <a href="https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer">View Demo</a>
    ·
    <a href="https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer/issues">Report Bug</a>
    ·
    <a href="https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Rest](https://en.wikipedia.org/wiki/Representational_state_transfer)
* [Requests](https://docs.python-requests.org/en/master/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Peer rely on python package requests : https://docs.python-requests.org/en/master/

* pip
  ```sh
  python -m pip install requests
  ```

Peer rely on python package ijson : https://pypi.org/project/ijson/

* pip
  ```sh
  python -m pip install ijson
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer.git
   ```

<!-- USAGE EXAMPLES -->
## Command line tool Usage

Helper script <strong>Peer.sh</strong> is provided to simplify the python <strong>Peer.py</strong> usage.

This script rely on the setup of a configuration file named Peer.conf located in the same directory than the script, it is in charge of
providing mandatories parameters to ./Peer.py script.




 ```sh
 ./Peer.sh file1 file2 ... filex
 ```

If used directly, python script help is as following :

 ```sh
 ./Peer.py <options> file1 file2 ... filex
 ```

 ```txt
 With options :

  Mandatories :

  --grid=<grid>   : Set Eulerian customer Grid name.
  --ip=<ip>       : Set Eulerian customer IPv4 address.
  --token=<token> : Set Eulerian customer AES token.

  Optionals :

  --accept=<accept>  : Set accepted reply format. ( default : 'application/json' ).
  --wdir=<directory> : Set Working directory used to download replies. ( default : '/tmp' ).
  --download-only    : Download the replies into working directory.

  Experts :

  --peer=<class>        : Set transport class. ( default : Eulerian.Edw.Peers.Rest ).
  --hook=<class>        : Set output hook class. ( default : Eulerian.Edw.Hooks.CSV ).
  --hook-options=<path> : Set output hook options. ( default : Hook.conf ).
  --host=<host>         : Set remote host. ( default : None ).
  --ports=<ports>       : Set remote ports. ( default : 80,443 ).
  --platform=<platform> : Set the name of authority platform. ( default : france ).
  --unsecure            : Use unsecure transport layer.
 ```
 
## API reference

class Eulerian.Edw.Peers.Rest

### Allocator

```Cpp

/** 
 * @brief Eulerian Data Warehouse Rest Peer constructor.
 */
Rest()

```

### Mandatory settings

```Python

/**
 * @brief Defines Eulerian Grid Name. 
 *        This attribute is mandatory.
 *        Its default value is None.
 *
 * @param grid - Grid Name.
 */
set_grid( grid )

/**
 * @brief Defines Eulerian Grid Name.
 *        This attribute is mandatory.
 *        Its default value is None.
 *
 * @param token - Token.
 */
set_token( token ) 

```

### Common settings

```Python

/**
 * @brief Defines Eulerian Platform Name. 
 *        'france' or 'canada' are the only accepted values.
 *        Default value is 'france'.
 *
 * @param platform - Platform name.
 */
set_platform( platform )

/**
 * @brief Defines Accepted reply format. 
 *        'application/json', 'text/csv' and 'application/parquet' are the only accepted values.
 *        Default value is 'application/json'.
 *
 * @param accept - Accept format.
 */
set_accept( accept ) 

/**
 * @brief Defines local working directory.
 *        Any writable directory is valid.
 *        Default value is '/tmp'.
 *
 * @param dir - Working directory.
 */
set_wdir( dir )

````

### Expert settings
set_host( host )         : Defines Remote host.
set_ports( ports )       : Defines Remotes ports( secure/unsecure ).
set_kind( kind )         : Defines Authority token type ( Access/Session ).

# Requesting

request( command )       : Do command

## API usage

Create a Job download the resulting file

MyPeer.py

 ```python

from Eulerian.Edw.Peers.Rest import Rest as Rest

/* Setup mandatory parameters */
platform = 'france'   // ( Can be france or canada )
grid     = <GridName> // ( Eulerian Customer Grid )
token    = <Token>    // ( Eulerian Customer Token )
request  = <request>  // ( Eulerian Data Warehouse Request )

/* Create new Peer Instance */
peer = Rest()

/* Setup mandatory parameters */
peer.set_platform( platform )
peer.set_grid( grid )
peer.set_token( token )
peer.set_download( True )

/* Send request to the server, wait end of the job, download
   resulting file, return path to the file */
path = peer.request( request )

 ```
Create a Job download the resulting file, parse streamed file and call Hook functions 

MyHook.py

```python

from Eulerian.Edw.Hook import Hook as Hook

class MyHook( Hook ) :
    def on_add( self, uuid, rows ) :
      for row in rows :
        string = ''
        for col in row :
          if type( col ) is bytes :
            col.col.decode()
          string += col
          string += '#'
         print( string )
         
```

MyPeer.py

```python

from Eulerian.Edw.Peers.Rest import Rest as Rest
import MyHook

/* Setup mandatory parameters */
platform = 'france'   // ( Can be france or canada )
grid     = <GridName> // ( Eulerian Customer Grid )
token    = <Token>    // ( Eulerian Customer Token )
request  = <request>  // ( Eulerian Data Warehouse Request )

/* Create new Peer Instance */
peer = Rest()

/* Setup mandatory parameters */
peer.set_platform( platform )
peer.set_grid( grid )
peer.set_token( token )
peer.set_hooks( MyHook() )
peer.set_accept( "application/json" )

/* Send request to the server, wait end of the job, download
   resulting file, parse the file call hooks */
peer.request( request )

```
Create a Job download the resulting file, load its content into Pandas Data Frame

MyPeer.py

```python

from Eulerian.Edw.Peers.Rest import Rest as Rest
import pandas as Pandas

/* Setup mandatory parameters */
platform = 'france'   // ( Can be france or canada )
grid     = <GridName> // ( Eulerian Customer Grid )
token    = <Token>    // ( Eulerian Customer Token )
request  = <request>  // ( Eulerian Data Warehouse Request )

/* Create new Peer Instance */
peer = Rest()

/* Setup mandatory parameters */
peer.set_platform( platform )
peer.set_grid( grid )
peer.set_token( token )
peer.set_download( True )

/* Setup format used to load data into Pandas */
peer.set_accept( "application/parquet" )

/* or 
peer.set_accept( "text/csv" ) */

/* Send request to the server, wait end of the job, download
   resulting file, return path to the file */
path = peer.request( request )

/* Load resulting file ( parquet format ) */
frame = Pandas.read_parquet( path )

/* or 
frame = Pandas.read_csv( path ) */


```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer/issues) for a list of proposed features (and known issues)

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact

THORILLON Xavier - x.thorillon@eulerian.com

Project Link: [https://github.com/EulerianTechnologies/Eulerian-Data-Warehouse-Python-Peer](https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [python](https://docs.python.org/3/tutorial/)
* [rest](https://en.wikipedia.org/wiki/Representational_state_transfer)
* [Edw]()


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/THORCOMP/Eulerian-Data-Warehouse-Python-Peer.svg?style=for-the-badge
[contributors-url]: https://github.com/THORCOMP//Eulerian-Data-Warehouse-Python-Peer/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/THORCOMP/Eulerian-Data-Warehouse-Python-Peer.svg?style=for-the-badge
[stars-url]: https://github.com/THORCOMP//Eulerian-Data-Warehouse-Python-Peer/stargazers
[issues-shield]: https://img.shields.io/github/issues/THORCOMP/Eulerian-Data-Warehouse-Python-Peer.svg?style=for-the-badge
[issues-url]: https://github.com/THORCOMP/Eulerian-Data-Warehouse-Python-Peer/issues
[license-shield]: https://img.shields.io/github/license/THORCOMP/Eulerian-Data-Warehouse-Python-Peer.svg?style=for-the-badge
[license-url]: https://github.com/THORCOMP//Eulerian-Data-Warehouse-Python-Peer/blob/master/LICENSE.txt

