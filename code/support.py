import pygame as pg
import os, sys

    
def load_sheet(filename, frame_width, frame_height, num_frames):
    sheet = pg.image.load(filename).convert_alpha()
    return [
        sheet.subsurface(pg.Rect(0, y * frame_height, frame_width, frame_height))
        for y in range(num_frames)
    ]

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