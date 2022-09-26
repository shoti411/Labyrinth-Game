<strong>README.md: </strong> Readme filled with information about the project</br></br>

<strong> Other/xtcp.py: </strong></br> 
Python file that creates a TCP server socket, waits for a single client connection and accepts, consumes series of JSON values until
connection is closed, then delivers corresponding acceptable strings as JSON object to the output side of client
TCP connection. Shuts down.</br></br>

<strong> Other/xjson.py: </strong></br> 
Python script that takes well-formed JSON strings as arguments, parses and then returns JSON array of corresponding acceptable strings.</br></br>

<strong>xtcp: </strong> Bash script</br></br>
<strong> Tests: </strong> directory filled with json tests </br></br>

<strong> RoadMap: </strong></br>
<li>Auxilary files are in C/Other. There are only 2 auxilary files contained in other which are xjson.py and xtcp.py which are the python scripts stated above.</li>
<li>Testing files are in C/Tests.</li>
<li>In C directory contains the README.md about the project and the xtcp bash script for user to call.</li></br>

<strong>Testing:</strong></br>
For testing from the C directory run xtcp with any [NATURAL 0-2]-in.json file from C/Tests. Then compare the output with the corresponding [NATURAL 0-2]-out.json.</br>
Example: './xtcp < Tests/0-in.json </br>
Testing can only be done through Northeastern's Khoury College Linux servers.