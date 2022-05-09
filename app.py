from flask import render_template ,url_for,flash,redirect,request
from output import output
import os

from flask import Flask

app = Flask(__name__,template_folder='Templates')
@app.route('/',methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/',methods=['POST','GET'])
def predict():
    imagefile=request.files['imagefile']
    image_path=os.path.join(app.root_path,'static\\images\\demo_imgs',imagefile.filename)
    imagefile.save(image_path)
    img="/images/demo_imgs/"+imagefile.filename
    title,ingredients,recipe = output(image_path)
    return render_template('predict.html',title=title,ingredients=ingredients,recipe=recipe,img=img)

if __name__=='__main__':
    app.run(debug=True)