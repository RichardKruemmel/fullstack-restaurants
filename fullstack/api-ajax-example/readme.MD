In order to run this demonstration website locally, you will first have to install the flask package. You can install flask system wide by typing `pip install flask`. At some point, you will have multiple conflicting versions of python on your computer, and you will need to use virtual environments to manage this. A good description is [found here](https://docs.python-guide.org/dev/virtualenvs/), and a good explanation for how to set up virtual environments with VSCode [can be found here](https://stackoverflow.com/questions/54106071/how-to-setup-virtual-environment-for-python-in-vs-code).  

Once flask is installed, you can start this application by typing 

`export FLASK_APP=main.py`

 followed by 

`flask run`

The second command should start a server, running by default on http://127.0.0.1:5000/. 

If you navigate to that page in your browser, you should see a simple page being rendered. 




