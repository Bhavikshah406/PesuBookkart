# Python Hello World Sample

This application demonstrates a simple, reusable Python web application.

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/IBM-Bluemix/python-helloworld)

## Run the app locally

1. [Install Python][]
+ cd into this project's root directory
+ Run `python server.py`
+ Access the running app in a browser at <http://localhost:8000>

[Install Python]: https://www.python.org/downloads/

## steps to deploy a bookkart app in ibm bluemix

1)login to ibm bluemix
2)click catalog -> search for python -> deploy python code (https://console.ng.bluemix.net/catalog/starters/python/)
-->give your app name and create
3)follow the steps given on 'getting started' page
	1)download the sample app
	2)now in the server.py file copy server code (definations for requests get,put,post,delete and the run_server code)
	3)in the manifest file add "buildpack: https://github.com/heroku/heroku-buildpack-python" under the path
	4)"Requirements files" are files containing a list of items to be installed using pip install 
	  we here require web.py to work with python 3  hence the version 0.40.dev0  ===>  web.py==0.40.dev0 in requirements.txt
	4)in your client file have all kind of requests made and add the following -->    service="app-name.mybluemix.net"
	5)now use the command line interface - 
		i)cd to your project directory 
		ii)cf login -u username -o organisation -s space
		iii)cf push your-app-name 
		iv)once yor instance in running  run your client file locally and now any interation or requests made directly goes to your server.py which is now deployed in ibm bluemix.
