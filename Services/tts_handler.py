import os
import torch
from openvoice.api import BaseSpeakerTTS, ToneColorConverter
from melo.api import TTS

class TTSHandler:
    def __init__(self, language, output_dir='outputs_v2'):
        self.language = language
        self.output_dir = output_dir
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        os.makedirs(output_dir, exist_ok=True)

        if self.language == "EN":
            en_ckpt_base = 'Resources/checkpoints/base_speakers/EN'
            en_source_default_se = torch.load(f'{en_ckpt_base}/en_default_se.pth').to(self.device)
            # en_source_style_se = torch.load(f'{en_ckpt_base}/en_style_se.pth').to(self.device)

            self.tts_model = TTS(language="EN", device=self.device)
            self.source_se = en_source_default_se
        elif self.language == "ES":

            pth_name = "es.pth"
            en_ckpt_base = 'Resources/checkpoints/base_speakers/EN'
            ckpt_converter = 'Resources/checkpoints_v2/converter'

            self.en_base_speaker_tts = BaseSpeakerTTS(f'{en_ckpt_base}/config.json', device=self.device)
            self.en_base_speaker_tts.load_ckpt(f'{en_ckpt_base}/checkpoint.pth')
            self.tone_color_converter = ToneColorConverter(f'{ckpt_converter}/config.json', device=self.device)
            self.tone_color_converter.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

            en_source_default_se = torch.load(os.path.join('Resources/checkpoints_v2/base_speakers/ses', pth_name)).to(self.device)
            # en_source_style_se = torch.load(os.path.join('Resources/checkpoints_v2/base_speakers/ses', pth_name)).to(self.device)

            self.tts_model = TTS(language="ES", device=self.device)

    def tts_to_file(self, text):
        output_path = os.path.join(self.output_dir, f"output_{self.language.lower()}.wav")
        self.tts_model.tts_to_file(text, speaker_id=0, output_path=output_path)
        return output_path
