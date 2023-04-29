from flask import Flask, request, jsonify, render_template,url_for, redirect
import util
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')




@app.route('/classify_image',methods=['GET','POST'])
def classify():
    image_data = str(request.form['image'])
    img_path = "./test_images/" + image_data
    output = str(util.classify_image(None,img_path))
    # Editing the name in proper format #
    output =output.replace('_',' ')
    output = output.upper()
    if(output == 'NONE'):
        return redirect('/none')

    return render_template('classify.html',op = output,)

@app.route('/none')
def none():
    return render_template('none.html')


# Testing all the routes and requests #
@app.route('/test')
def test():
    # loc = request.form['image']
    # data = request.form['photo']
    # print(data)
    return render_template('index1.html')

# Testing successful #

if __name__ == "__main__":
    print("Starting Flask Server")
    util.load_artifacts()
    print(util.classify_image(None, "./test_images/rf.jfif"))

    app.run(port=5000,debug=True)