# asciinema-tools
An application to trim, annotate, and edit asciinemi casts after recording

# How to use
Just clone the repo, `git clone https://github.com/Decagon/asciinema-tools` and run python app.py inside of the directory. You can change the defaults by editing app.py (configuration is at the top of the file.)

# Features
- automatically trim the "exit" word from your casts (when you press <Ctrl-D> or type "exit" to exit.) They're everywhere!
- automatically trim empty space in the beginning of the cast, so that you can get right into action.
- compression: built-in compression to make file sizes smaller, compatible with asciinema, no extra configuration needed (enabled by default.)
- 
# Roadmap
- custom slicing (removal of frames)
- stretching: increase or decrease time of frames (e.g. to add a bit more time to explain a command after you've casted it with audio overlay.)
- annotation: (e.g. Chapter Two: Title of Chapter Two here.)
- support for `biome` to keep your environment variables consistent
