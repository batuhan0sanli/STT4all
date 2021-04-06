# STT4all
Speech recognition for meeting etc. with support for several engines and APIs, online and offline.
It works well for audio recording or zoom video recording.

**Speech recognition engine/API:**
 - [CMU Sphinx](http://cmusphinx.sourceforge.net/wiki/)  (works offline)
 -   Google Speech Recognition
 -   [Google Cloud Speech API](https://cloud.google.com/speech/)
 -   [Wit.ai](https://wit.ai/)
 -   [Microsoft Azure Speech](https://azure.microsoft.com/en-us/services/cognitive-services/speech/)
 -   [Microsoft Bing Voice Recognition (Deprecated)](https://www.microsoft.com/cognitive-services/en-us/speech-api)
 -   [Houndify API](https://houndify.com/)
 -   [IBM Speech to Text](http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/speech-to-text.html)

**Supported file types:**

 - .wav
 - .mp3
 - .ogg
 - .flv
 - .mp4
 - .wma
 - .aiff
 - .aac



## Usage

 1. Install requirements
	`pip install -r requirements.txt`
 2. Edit `config.txt` file.
It is described below.
 3. Copy your files to the 'source' folder.
 4. Run `main.py`
 5. Enjoy it!

### How do I edit the `config.txt` file?

 - **LANGUAGE:** Use [ISO 639-1](https://www.andiamo.co.uk/resources/iso-language-codes/) standard language codes. For example, if your language/dialect is British English, it is better to use  "en-GB"  as the language rather than  "en-US".
 - **NOISE_REDUCTION:** Recommended to turn it on if it is in a noisy environment. Otherwise, turn it off for a better result. (only supports several engines and APIs)
 - **BUFFER_SIZE:** Long files may time out. That's why speeches are processed by cutting. This is the buffer size in seconds. (default: 60 sec)
- **SERVICE:** Select the engine or API you want to use. It is described below.

## Supported Services

 -   `SPHINX`
	 - Offline
 -   `GOOGLE_SPEECH_RECOGNITION`
	 - If `USE_DEFAULT_API = true`, you don't need any API key. Otherwise you need Google Speech Recognition API key
 -   `GOOGLE_CLOUD_SPEECH`
	 - You need JSON credentials file path
 -   `WIT_AI`
	 - You need WIT.AI API key
 -   `AZURE_SPEECH`
	 - You need Azure Speech API key
 -   `BING`
	 - You need Bing API key
 -   `HOUNDIFY`
	 - You need Houndify Client ID and Houndify Client Key
 -   `IBM`
	 - You need IBM STT Username and IBM STT Password

## Requirements

 - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): for speech recognition
 - [pydub](https://pypi.org/project/pydub/): for audio format and manipulation operations
 - [tqdm](https://pypi.org/project/tqdm/): for progress bar

## License

The MIT License (MIT)

Copyright (c) 2021 [Batuhan ŞANLI](https://www.batuhansanli.com/)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
