# "Mittelungleichungen" Manimations

Animations using manim for the Dorfuchs song
"Mittelungleichungen".

- Manim Docs: https://docs.manim.community/en/stable/index.html

## Setup

1. Clone this repo using `git clone https://github.com/mathcat4/dorfuchs-song-manim.git`.
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) (Python package manager).
3. Install the corresponding LaTeX distribution packages for your OS.
4. If you're using linux, then additionally install these packages:

```bash
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev
```

5. Run `uv sync` to load python modules.

Steps 2 to 4 are also outlined in the official [manim installation guide](https://docs.manim.community/en/stable/installation/uv.html).

# Usage

- Move the audio file to `media/Audio/audio.wav` to render with sound.
- Execute `uv run manim -pql [FILE] [SCENE]` for a low-quality preview
- The main animation is rendered using (e.g. `uv run manim -pqh project/main.py MainSketch`).

## Debug

- If met with the error
  ```
  [Errno 2] No such file or directory: 'media/Tex'
  ```
  while running manim for the first time, create an empty directory called `media` in the main folder.
