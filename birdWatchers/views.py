from birdWatchers import app
import tensorflow as tf
import os
# from flask import render_template
# from birdWatchers.Inception.inception import download
from birdWatchers.Inception.inception import Inception


@app.route('/')
def main():
    return '<h1>hello world!</h1>'


@app.route('/search')
def search():
    print(tf.__version__)

    # Download Inception model if not already done.
    # maybe_download()

    data_dir = "Inception/inception"
    imagePath = 'cropped_panda.jpg'
    image_path = os.path.join(data_dir, imagePath)
    # Load the Inception model so it is ready for classifying images.
    model = Inception()
    pred = model.classify(image_path=image_path)

    # Print the scores and names for the top-10 predictions.
    model.print_scores(pred=pred, k=10)

    # Close the TensorFlow session.
    model.close()
