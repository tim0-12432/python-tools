import argparse
from PIL import Image
import os

def get_args() -> None:
    parser = argparse.ArgumentParser(prog="sprite2gif", description="Convert a sprite sheet to a gif")
    parser.add_argument("sprite", type=str, help="path to sprite file/folder")
    parser.add_argument("gif", type=str, help="path to gif file/folder")
    parser.add_argument("-w", "--width", type=int, default=None, help="width of one sprite tile")
    parser.add_argument("-a", "--amount", type=int, default=None, help="amount of sprite tiles")
    parser.add_argument("-r", "--repeat", type=bool, default=True, help="repeat animation")
    parser.add_argument("-t", "--timing", type=int, default=200, help="time of a single tile in ms")
    parser.add_argument("-o", "--order", type=str, default=None, help="order of sprite tiles")
    return parser.parse_args()

def crop_sprite(sprite: Image, width: int, amount: int) -> list:
    sprite_width, sprite_height = sprite.size
    sprite_tiles = []
    count = 0
    crop_width = 0
    if width:
        count = sprite_width // width
        crop_width = width
    elif amount:
        count = amount
        crop_width = sprite_width // amount
    else:
        count = 1
        crop_width = sprite_width
    for i in range(count):
        sprite_tiles.append(sprite.crop((i * crop_width, 0, (i + 1) * crop_width, sprite_height)))
    return sprite_tiles

def print_args(args: argparse.Namespace) -> None:
    print("\n--- sprite2gif ---")
    print("input: " + args.sprite)
    print("output: " + args.gif)
    print("width: " + str(args.width) + ("px" if args.width else ""))
    print("amount: " + str(args.amount))
    print("repeat: " + str(args.repeat))
    print("timing: " + str(args.timing) + "ms")
    print("order: [" + str(args.order) + "]")
    print("------------------\n")

def reorder_sprites(sprite_tiles: list, order: list) -> list:
    reordered = []
    for i in [int(x) for x in order]:
        reordered.append(sprite_tiles[i])
    return reordered

def main() -> None:
    args = get_args()
    path = args.sprite
    print_args(args)
    if path.endswith(".png") or path.endswith(".jpg"):
        sprite = Image.open(path)
        sprite_tiles = crop_sprite(sprite, args.width, args.amount)
        if args.order:
            sprite_tiles = reorder_sprites(sprite_tiles, args.order.split(","))
        sprite_tiles[0].save(args.gif, save_all=True, append_images=sprite_tiles[1:], loop=0 if args.repeat else 1, optimize=False, duration=args.timing, disposal=2)
    else:
        paths = os.listdir(path)
        for sprite_path in paths:
            sprite = Image.open(path + "\\" + sprite_path)
            print("... " + path + "/" + sprite_path)
            sprite_tiles = crop_sprite(sprite, args.width, args.amount)
            if args.order:
                sprite_tiles = reorder_sprites(sprite_tiles, args.order.split(","))
            if not os.path.exists(args.gif):
                os.mkdir(args.gif)
            sprite_tiles[0].save(args.gif + "\\" + sprite_path.replace(".png", ".gif").replace(".jpg", ".gif"), save_all=True, append_images=sprite_tiles[1:], loop=0 if args.repeat else 1, optimize=False, duration=args.timing, disposal=2)

if __name__ == '__main__':
    main()
