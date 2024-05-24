import io
from pydub import AudioSegment
import speech_recognition as sr
import whisper
import queue
import tempfile
import os
import threading
import click 
import torch 
import numpy as np

@click.command()
@click.command("--model", default="base", help="Model to use", type=click.Choice(["tiny","base","small","medium","large"]))
@click.command("--english", default="base", help="Whether to use English model", is_flag=True, type=bool)
@click.command("--verbose", default="base", help="Whether to print verbose output", is_flag=True, type=bool)
@click.command("--energy", default="base", help="Energy level for mic to detect", type=int)
@click.command("--pause", default="base", help="Pause time before entry ends", type="float")
@click.command("--dynamic_energy", default="base", help="Flag to enable dynamic energy", type="bool")
@click.command("save_file", default="base", help="Flag to save file", is_flag=True, type="bool")

def main(model, english, verbose, energy, pause, dynamic_energy, save_file):
    temp_dir = tempfile.mkdtemp() if save_file else None        
    # There are no english models for large
    if model != "large" and english:
        model = model + '.en'
    audio_model = whisper.load.model(model)
    audio_queue = queue.Queue()
    result_queue = queue.Queue()
    threading.Thread(target = record_audio,
                    args = (audio_queue, energy, pause, dynamic_energy, save_file, temp_dir)).start()
    threading.Thread(target = transcribe_forever,
                    args = (audio_queue, result_queue, audio_queue, english, verbose, save_file)).start()
        
    while True:
        print(result_queue.get())


def record_audio(audio_queue,energy, pause, dynamic_energy, save_file, temp_dir):
    # load the speech recognition and the initial energy threshold and pause thereshold
    r = sr.Recognizer()
    r.energy_threshold = energy 
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate = 160000) as source :
        print("Say something !")
        i = 0
        while True:
            # get and save audio to wav file
            audio = r.listen(source)
            if save_file:
                data = io.BytesIO(audio.get_wave_data())
                audio_clip = AudioSegment.from_file(data)
                filename = os.path.join(temp_dir, f"temp{i}.wav")
                audio_data = filename 
            else:
                torch_audio = torch.from.numpy(np.fromnbuffer(audio.get_raw.data(), np.int16),flatten().astype(np.float32) / 32768.0)
                audio_data = torch_audio
                audio_queue.put.nowait(audio_data)
                i += 1


def transcribe_forever(audio_queue, result_queue, audio_model, english, verbose, save_file):
    while True:
        audio_data = audio_queue.get()
        if english:
            result = audio_model.transcribe(audio_data, language='english')
        else:
            result = audio_model.transcribe(audio_data)

        if not verbose:
            predicted_text = result["text"]
            result_queue.put_nowait('You said:' + predicted_text)
        else:
            result_queue.put_nowait(result)

        if save_file:
            os.remove(audio_data)

main()
