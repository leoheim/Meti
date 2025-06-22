from flask import Flask, render_template, request
import torch
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import io
import base64
import random

app = Flask(__name__)

…
  return render_template('index.html', images=images, selected_digit=selected_digit)

  if __name__ == '__main__':
    app.run(debug=True)
