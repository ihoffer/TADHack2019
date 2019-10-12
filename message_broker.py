# coding=utf-8
import random

final_confirmations = [
    "I got your deets down, will be in touch..."
]

stage_confirmations = {
    "club": ["Oh geez, good choice, one of my favorites"],
}
def get_stage_confirmation(info):
    if info in stage_confirmations:
        return random.choice(stage_confirmations[info])
    return None

def get_final_confirmation():
    return random.choice(final_confirmations)