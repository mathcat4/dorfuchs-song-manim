# Dorfuchs Song Manim Animations

- Manim: https://docs.manim.community/en/stable/index.html

## Usage

1. Clone this repo
2. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) (Python package manager).
3. Install the corresponding LaTeX distribution packages for your OS
4. If you're using linux, then additionally install these packages

```bash
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev
```

5. Run `uv sync`
6. Run `uv run manim -pql [FILE] [SCENE]` for a low-quality preview (e.g. `uv run manim -pql project/main.py MainSketch`)
