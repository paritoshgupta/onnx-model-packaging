import sys
sys.setrecursionlimit(500000)
from flask import Flask, request, jsonify
import torch 
import numpy as np
from transformers import RobertaTokenizer
import onnxruntime

app = Flask(__name__)
tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
session = onnxruntime.InferenceSession("roberta-sequence-classification-9.onnx")
print(1)

@app.route("/predict", methods=["POST"])

# The predict() function is a Flask route that enables the predict URL when the application is running. The function only allows POST 
# HTTP methods.
def predict():
    input_ids = torch.tensor(tokenizer.encode(request.json[0], add_special_tokens = True)).unsqueeze(0)

    if input_ids.require_grad:
        numpy_func = input_ids.detach().cpu().numpy()
    else:
        numpy_func = input_ids.cpu().numpy()

    inputs = {session.get_inputs()[0].name: numpy_func(input_ids)}
    out = session.run(None, inputs)
    result = np.argmax(out)

    return jsonify({"positive": bool(result)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)