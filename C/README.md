<strong>README.md: </strong> Readme filled with information about the project</br></br>
<strong> Other/xjson.py: </strong></br> 
Python script that takes stream of well-formed JSON strings from STDIN, parses and then prints JSON array of corresponding acceptable strings.</br></br>
<strong>xjson: </strong> Bash script</br></br>
<strong> Tests: </strong> directory filled with json tests </br></br>

<strong> RoadMap: </strong></br>
<li>Auxilary files are in C/Other. There is only 1 auxilary file contained in other which is xjson.py which is the python script stated above.</li>
<li>Testing files are in C/Tests</li>
<li>In C directory contains the README.md about the project and the xjsons bash script for user to call.</li></br>

<strong>Testing:</strong></br>
For testing from the C directory run xjson with any [NATURAL 0-2]-in.json file from C/Tests. Then compare the output with the corresponding [NATURAL 0-2]-out.json.</br>
Example: './xjson <  Tests/0-in.json'
