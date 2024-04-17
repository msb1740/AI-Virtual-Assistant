# AssemblyAI receive input from user
# AssemblyAI send real-time transcript to OpenAI
# OpenAI send real-time tanscription to ElevenLabs
# ElevenLabs generate audio steam and send to user
# OpenAi generate response based on real-time speech to text transcript 
# AssemblyAi perform real time transcript.

1. Create AssemblyAI account
https://www.assemblyai.com/ (paid without paid subscription not working)

2. Create OpenAI account
https://platform.openai.com/ (Paid subscription)

3. Create  elevenLabs account
https://elevenlabs.io(paid subscription)


##### Step 1: Install Python libraries ######

install brew on mac
(https://mac.install.guide/homebrew/3)

brew install portaudio
pip install "assemblyai[extras]"
pip install elevenlabs==0.3.0b0
pip install --upgrade openai