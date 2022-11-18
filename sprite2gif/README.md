# Sprite2Gif

## What is it?

Sprite2Gif is a simple tool to convert a sprite sheet into a gif animation.

## How to use it?

### Install

```bash
pip install -r requirements.txt
```

### Use

```bash
python -m sprite2gif -a 3 -o 1,0,1,2 input-sprites.png output.gif
```

```bash
python -m sprite2gif -a 3 -o 1,0,1,2 ./input ./output
```

### Options

```bash
-h, --help                  Usage information
-w, --width <int>           Width of the sprite sheet tiles in pixels
-a, --amount <int>          Delay between frames in seconds (default: 1)
-r, --repeat <bool>         Repeat the animation (default: True)
-t, --timing <int>          Timing of the animation in milliseconds (default: 200)
-o, --order <list[int]>     Order of the frames (default: 0,1,2,...)
```
