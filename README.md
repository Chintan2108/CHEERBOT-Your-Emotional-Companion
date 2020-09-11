# CHEERBOT-Your-Emotional-Companion

## Affiliations
#### Charotar University of Science and Technology
#### Jan 2017 - April 2018

## Summary

Cheerbot is a special kind of chatbot that can talk to you with voice, or texts. It is your emotional companion - it will cheer you up if you are sad and add to your happiness otherwise. The main objective of creating this project was to attempt and help fight lonliness and depression in this world. A lot of us feel depressed at times, feel vulnerable and scared of talking out loud to another person. This is a sincere attempt to try and help in such a scenario - talk to Cheerbot. It will understand you, and try to determine your emotional state based on the keywords you speak, based on the pitch of your voice and even your facial contours and expressions. If you are sad Cheerbot will try to make some jokes and make you laugh. 

## Modules

### Built With/Libraries Used/Tools & Technology

* Google Text to Speech
* Google Speech to Text
* PyAudio
* NLTK
* Numpy, PyWave

### Emotion Detection based on Text Analysis

If the user chooses to text-chat with Cheerbot, the input of the user will be analysed for keywords that particularly indicate a sad or unhappy emotional state with the help of tokenization and word embeddings. If the user's input is flagged as sad or unhappy, Cheerbot will come up with confronting replies and mildly funny replies that can make the user feel better. It will also try to get the user to stay and talk if the user leaves in a distressed state. In other cases the Cheerbot will usually come up with funny and witty responses.

### Emotion Detection based on Voice Pitch

If the user chooses  to voice-chat with the Cheerbot, the speech will be converted to text and the text analysis will be carried to determine the emotional state of the user. Moreover, the voice pitch of the user will also be analysed. Usually, when a person is sad, his/her voice tone and pitch are really low as compared to when a person is happy or not sad. Keeping this in mind, chunk-by-chunk frequency is extracted of the user's voice and pitch analysis is done. Combinedly with both these analyses, if the user's input is flagged as sad or unhappy, Cheerbot will come up with confronting replies with a warm voice pitch and mildly funny replies with gentle chuckles that can make the user feel better. It will also try to get the user to stay and talk if the user leaves in a distressed state. In other cases the Cheerbot will usually come up with funny and witty responses.

### Emotion Detection based on Facial Expression

If the user chooses to have a video chat with the Cheerbot, a happy animation of a character of the user's choice serves as the Cheerbot on the other side. In this case, apart from the text and voice analysis, the person's facial expressions and facial contour patterns will be analysed to determine if the user is sad. Based on the analyses of text, audio and video, if the user's input is flagged as sad or unhappy, Cheerbot will come up with confronting replies and mildly funny replies that can make the user feel better. It will also try to get the user to stay and talk if the user leaves in a distressed state. This will be in conjunction with the cheerful expressions in the animated character as well as confronting and happy voice pitch of Cheerbot. In other cases the Cheerbot will usually come up with funny and witty responses.

### Application Development (GUI) and Deployment

Currently the code is completely bare of a GUI and hence there is no medium to use this and to provide this to people around the world. A single page web application, which is responsive and can run well on mobile and laptops is proposed, which shall be deployed on Google Cloud Platform with the entire backend of Cheerbot.

## Contribution

Please feel free to raise issues and fix any existing ones. Further details can be found in our [code of conduct](https://github.com/Chintan2108/CHEERBOT-Your-Emotional-Companion/blob/master/CODE_OF_CONDUCT.md).

## Credits

Please cite this work as:

```
Maniyar, C. B., Bhatt, C. M., Pandit, T. N., & Yadav, D. H. (2019). CHEERBOT: A Step Ahead of Conventional ChatBot. In Next-Generation Wireless Networks Meet Advanced Machine Learning Applications (pp. 306-322). IGI Global.
```
