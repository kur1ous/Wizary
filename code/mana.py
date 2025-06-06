import pygame as pg
from settings import *

class Mana:
    def __init__(self, mana_cap):
        self.mana_cap = mana_cap
        self.current_mana = mana_cap

    def mana_use(self, use_amount):
        self.use_amount = use_amount

        if self.current_mana >= self.use_amount:
            self.current_mana -= self.use_amount
            print(f"{self.use_amount} used!")
        else: 
            print(f"Not enough mana! {self.current_mana}, tried using {self.use_amount}")

    def mana_regen(self, regen):
        self.regen = regen
        if self.current_mana <= self.mana_cap and self.current_mana != self.mana_cap:
            self.current_mana += self.regen
            if self.current_mana >= self.mana_cap:
                self.current_mana = self.mana_cap
                print(f"Mana back to {self.mana_cap}")



        