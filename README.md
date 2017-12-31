# asciinema-tools
An application to trim, annotate, and edit asciinema casts after recording

[![Updates](https://pyup.io/repos/github/Decagon/asciinema-tools/shield.svg)](https://pyup.io/repos/github/Decagon/asciinema-tools/) [![Python 3](https://pyup.io/repos/github/Decagon/asciinema-tools/python-3-shield.svg)](https://pyup.io/repos/github/Decagon/asciinema-tools/)

# How to use
Just clone the repo, `git clone https://github.com/Decagon/asciinema-tools` and run `python asciinema-tools.py` inside of the directory.

# Features
- automatically trim the "exit" word from your casts (when you press <Ctrl-D> or type "exit" to exit.) They're everywhere!
- automatically trim empty space in the beginning of the cast, so that you can get right into action.
- compression built-in compression to make file sizes smaller, compatible with asciinema, no extra configuration needed (enabled by default.)
 
# Roadmap
- remove parts of the cast/mistakes
- increase or decrease time of frames (e.g. to add a bit more time to explain a command after you've casted it with audio overlay.)
- annotations: (e.g. Chapter Two.)
- support for `biome` to keep your environment variables consistent so that a development environment can be easily procured
