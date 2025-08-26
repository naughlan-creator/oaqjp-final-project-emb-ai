from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    text = request.args.get('textToAnalyze')

    response = emotion_detector(text)

    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!", 200

    result = (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}. "
    )

    return result, 200

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

