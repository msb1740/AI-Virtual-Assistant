
import assemblyai as aai
from elevenlabs import generate, stream
from openai import OpenAI

class AI_Assistant:
    def __init__(self):
        aai.settings.api_key = "AssemblyAI API Key"
        self.openai_client  = OpenAI (api_key= "OpenAI API Key")
        self.elevenlabs_api_key = "ElevenLabs API Key"

        self.transcriber = None

        #  system Prompt
        self.full_transcript = [
            {"role":"system", "content":
                "You are an expert in sales who have immense knowledge in IT Sales domain. You can answer any questions related to IT Sales.if asking other domain like eduction, agriculture, dental, should not answer. just reply to them I don't have information for it if you asking IT related things so I can help you."},
        ]
###### Step 2: Real-Time Transcription with AssemblyAI ######
  
    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate = 16000,
            on_data = self.on_data,
            on_error = self.on_error,
            on_open = self.on_open,
            on_close = self.on_close,
            end_utterance_silence_threshold = 1000
        )

        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate =16000)
        self.transcriber.stream(microphone_stream)
    
    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        return


    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generate_ai_response(transcript)
        else:
            print(transcript.text, end="\r")


    def on_error(self, error: aai.RealtimeError):
        return


    def on_close(self):
        return

###### Step 3: Pass real-time transcript to OpenAI ######
    
    def generate_ai_response(self, transcript):

        self.stop_transcription()

        self.full_transcript.append({"role":"user", "content": transcript.text})
        print(f"\nCustomers: {transcript.text}", end="\r\n")

        response = self.openai_client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = self.full_transcript
        )

        ai_response = response.choices[0].message.content

        self.generate_audio(ai_response)

        self.start_transcription()
        print(f"\nReal-time transcription: ", end="\r\n")


###### Step 4: Generate audio with ElevenLabs ######
    def generate_audio(self, text):

        self.full_transcript.append({"role":"assistant", "content": text})
        print(f"\nAI Sales: {text}")

        audio_stream = generate(
            api_key = self.elevenlabs_api_key,
            text = text,
            voice = "Rachel",
            stream = True
        )

        stream(audio_stream)

greeting = "Thank you for calling in IT sales. My name is BELLA, how may I assist you?"
ai_assistant = AI_Assistant()
ai_assistant.generate_audio(greeting)
ai_assistant.start_transcription()

        





    



    





