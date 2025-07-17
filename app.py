from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')
vectorizer = joblib.load('tfidf.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = ""
    if request.method == 'POST':
        text = request.form['news']
        text_vector = vectorizer.transform([text])
        result = model.predict(text_vector)[0]
        prediction = "Fake News" if result == 1 else "Real News"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
