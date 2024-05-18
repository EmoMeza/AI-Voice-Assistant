# AI Voice Assistant

AI Voice Assistant is a Python project that combines audio recording, voice transcription, interaction with an AI-based chatbot, and text-to-speech synthesis. This project allows users to engage in conversations with a chatbot using voice as input and output.

## Features

- **Audio Recording**: Users can start and stop audio recording by simply pressing Enter.
- **Voice Transcription**: Recorded audio is transcribed into text using an AI model.
- **Chatbot Interaction**: Transcribed text is sent to an AI-based chatbot that generates a response.
- **Text-to-Speech Synthesis**: The chatbot's response is converted back into voice and played for the user.
- **Conversation Continuation**: After each interaction, the user is prompted whether to continue the conversation.

## Prerequisites

Before running the project, make sure you have the following Python libraries installed:

- whisper
- openai
- pydub

Additionally, you'll need to download two files named checkpoint.pth and checkpoint_v2.pth and move them to the Resources/checkpoints directory.

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies mentioned in the prerequisites.
3. Download the checkpoint and checkpoint_v2 folders from the following links:
   - checkpoint ([link-to-file](https://myshell-public-repo-hosting.s3.amazonaws.com/openvoice/checkpoints_1226.zip))
   - checkpoint_v2 ([link-to-file](https://myshell-public-repo-hosting.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip))
4. Move them to the Resources/ directory.
5. Run the main.py script from the command line.
6. Follow the instructions in the console to start and stop audio recording, interact with the chatbot, and listen to the generated responses.

## Contribution

Contributions are welcome! If you'd like to contribute to the project, follow these steps:

1. Fork the repository.
2. Make your changes in a separate branch.
3. Submit a pull request describing your changes.
