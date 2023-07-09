# AlpackaiAPI
Public Alpackapi repo 


# Logic
This flask_app.py[flask.app.py](flask_app.py) handles prompt interacting with Vertex AI codey API chat API.   
it calls the [processor.py](processor.py) function process_request.   
this function instantiates two classes :   

* ConfigurationLoader gets the configurations from the [configurations.yml](configurations.yml) file

* ChatModel who initiate the model, connect with it and get requests from it.



The flask_app.py is just a skeleton with one post method.

TODO:
Integration
Pass the git map to GOogle's API (Understand from Aider)
Architecture: is it possible to run serverless?




