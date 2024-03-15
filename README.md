# MULTILINGUAL E-COMMERCE ASSISTANT
(MVP)

## OVERVIEW:
The Multilingual E-Commerce Assistant is a comprehensive language-enabled platform designed to enhance the accessibility and inclusivity of online commerce. The project aims to bridge language barriers by allowing users to interact with the e-commerce platform in their preferred language, including both input and output. It leverages text, voice, and image interfaces to provide a seamless and user-friendly experience for individuals who may not be comfortable with English or typing.

## INTRODUCTION:
In the ever-expanding world of online commerce, the Multilingual E-Commerce Assistant addresses the challenge of language diversity among users. It recognizes that a significant segment of potential customers may not be fluent in English or may prefer to interact in their native languages. The project's primary goal is to increase e-commerce penetration by offering a more inclusive and accessible experience, transcending language constraints.

## FUNCTIONALITY:
1. Text Input & Output-
Users can input search queries, make payment confirmations, receive post-order updates, and access customer service in their preferred languages using text interactions. The system supports a range of Indic languages, allowing users to communicate in their preferred language. Text input is processed using linguistic collation algorithms, and the output is provided in the corresponding language.

2. Voice Input & Output-
The project supports voice interactions, enabling users to speak their queries and receive responses in their preferred language. Utilizing automatic speech recognition (ASR) and text-to-speech (TTS) technologies, the system ensures a smooth transition between spoken words and textual information.

3. Image Input & Output-
Image translation functionality allows users to upload images containing text, such as product descriptions or instructions. Optical Character Recognition (OCR) is employed to extract text from images, which is then translated into the desired language. Translated text can be presented as text output or converted into speech for user convenience.

4. Customer Service-
Customer service interactions, including chat support or voice-based assistance, are available in multiple languages. Language-specific customer support ensures effective communication and issue resolution, fostering trust and satisfaction among users.

## REQUIREMENTS:
Hardware:
- A device with internet connectivity (computer, smartphone, tablet)
- Microphone for voice input (optional)
- Camera for image input (optional)

Software:
- Operating System: Windows, macOS, Linux (for desktop) or Android, iOS (for mobile)
- Web browser for accessing the e-commerce platform
- Python runtime>=3.0 for executing the script
- Required Python libraries: 
  * tkinter (usually included with python)
  * Pandas
  * Easy OCR
  * First install PyTorch, then Easy OCR
    ```
    pip install torch
    ```
    ```
    pip install easyocr
    ```
  * Open CV
    ```
    pip install opencv-python
    ```
  * googletrans
    ```
    pip install googletrans
    ```
  * SpeechRecognition
    ```
    pip install speechrecognition
    ```
  * langdetect
    ```
    pip install langdetect
    ```
  * gtts
    ```
    pip install gtts
    ```
  * os

Language Support:
- Bengali
- English
- Gujarati
- Hindi
- Kannada
- Malayalam
- Marathi
- Nepali
- Odia
- Punjabi
- Sindhi
- Tamil
- Telugu
- Urdu
  
## CONCLUSION:
The Multilingual E-Commerce Assistant aims to revolutionize the way users engage with online commerce platforms, making the experience more accessible and inclusive. By incorporating text, voice, and image interfaces with multilingual support, the project addresses the diverse linguistic needs of users, thereby contributing to increased e-commerce adoption worldwide.
