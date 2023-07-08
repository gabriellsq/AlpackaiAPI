from utils import ConfigurationLoader, ChatModel

import vertexai

loader = ConfigurationLoader("configurations.yml")
project_id = loader.get_value("project_id")
model_id = loader.get_value("model_id")
location = loader.get_value("location")
parameters=loader.get_value("parameters")


model = ChatModel(project_id, model_id, location)
model.initialize()

if prompt:
    response = model.send_message(prompt, **parameters)
else:
    response = model.send_message("Hello", **parameters)

    print(response)



