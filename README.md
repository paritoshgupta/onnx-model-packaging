- Packaging ML Model is all about getting a model into container to take advantage of contarized processed to help sharing, distributing and easy deployment

- Example shows using an ONNX model and package within a container that serves a Flask app that performs the prediction.

- CI/CD platforms are the foundation of automation and reliable results.
- Build, Test, Release, Deploy and Validate.
- SageMaker is a specialized ML platform that goes beyond offering steps in a pipeline to accomplish a goal like publishing a model.
- AutoML is the automation of the tasks related to training a model on clean data.
- A pipeline is nothing but a set of steps to perform specific objective like Publishing model into production environment when run.

- Model Used:
    - RoBERTa Sequence Classification 
    - place the model (.onnx) file inside /webapp directory
    - URL: https://github.com/onnx/models/blob/main/text/machine_comprehension/roberta/model/roberta-sequence-classification-9.onnx

# test local
- cd webapp
- python app.py
- curl -X POST "Content-Type: application/JSON" --data '["Containers are more or less interesting"]' http://0.0.0.0:5000/predict
- curl -X POST "Content-Type: application/JSON" --data '["MLOps is critical for robustness"]' http://0.0.0.0:5000/predict

# docker test
- docker build -t paritoshgupta/roberta .
- docker run -it -p 5000:5000 --rm paritoshgupta/roberta
- curl -X POST "Content-Type: application/JSON" --data '["Espresso is too strong"]' http://0.0.0.0:5000/predict


- *GitHub actions shows an example of creating a container while the model is in Microsoft Azure Model Registry, image is created by retrieving the model from Azure Model Regstry and then finally creating an Docker image which is later pushed to GitHub Container Registry.*

- **Secrets required for Microsoft Azure and GitHub Container Registry.**