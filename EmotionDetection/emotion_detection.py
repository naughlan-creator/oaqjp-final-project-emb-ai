import requests, json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}
    input = {"raw_document" : {"text" : text_to_analyze}}
    response = requests.post(url, headers=headers, json=input)

    data = response.json()
    predictions = data.get("emotionPredictions", [])

    emotions = predictions[0].get("emotion", {})

    scores = {
        "anger" : emotions.get("anger"),
        "disgust" : emotions.get("disgust"),
        "fear" : emotions.get("fear"),
        "joy" : emotions.get("joy"),
        "sadness" : emotions.get("sadness"),
    }

    scores["dominant_emotion"] = max(scores, key=scores.get)
    return scores


    