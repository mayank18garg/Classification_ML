from flask import Flask , request
# from torchvision import models
# from torchvision import transforms
from PIL import Image
import torch
import joblib

app = Flask(__name__)

transform=joblib.load("transform.pkl")
class_model=joblib.load("resnet_model.pkl")

@app.route('/')   # routing_handler
def hello_world():
    return "Hello Sanket2\n"
    
@app.route('/classification', methods=['POST'])
def classification():
    files = request.files['imagefile']
    image = Image.open(files.stream)
    img_t = transform(image)
    batch_t = torch.unsqueeze(img_t,0)
    out = class_model(batch_t)
    with open('imagenet_classes.txt') as f:
        labels = [line.strip() for line in f.readlines()]
    _, index = torch.max(out, 1)
    # percentage = torch.nn.functional.softmax(out, dim=1)[0] * 100

    return labels[index[0]]
    

if __name__ == '__main__' :
    app.run(host='0.0.0.0')   