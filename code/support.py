import pygame as pg
import os, sys, random, math

def get_spawn_position(player_pos, min_distance, spawn_area):
    while True:
        x = random.randint(spawn_area.left, spawn_area.right)
        y = random.randint(spawn_area.top, spawn_area.bottom)
        
        spawn_pos = pg.Vector2(x, y)

        if spawn_pos.distance_to(player_pos) >= min_distance:
            return spawn_pos

    
def load_sheet(filename, frame_width, frame_height):
    sheet = pg.image.load(filename).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()

    frames = []
    y = 0
    while (y + 1) * frame_height <= sheet_height:
        rect = pg.Rect(0, y * frame_height, frame_width, frame_height)
        frames.append(sheet.subsurface(rect))
        y += 1

    return frames

def import_folder(folder):
    images = []
    for f in os.scandir(folder):
        if not f.is_dir():
            img = pg.image.load(f.path).convert_alpha()
            images.append(img)
    return images

def import_assets(folder):
    assets = {}
    for f in os.scandir(folder):
        if f.is_dir():
            assets[f.name] = import_folder(f.path)
    return assets

def import_folder_dict(folder):
    surface_dict = {}

    for f in os.scandir(folder):
        img = pg.image.load(f.path).convert_alpha()
        file_name = f.name.split(".")[0]
        surface_dict[file_name] = img
    return surface_dict