# coding=utf-8
import random

final_confirmations = [
    "I got your deets down, will be in touch..."
]

stage_confirmations = {
    "club": ["Oh geez, good choice, one of my favorites."],
}

stage_questions = {
    "groupSize": ["What's your group size, m8?"]
}

def get_stage_confirmation(stage):
    if stage in stage_confirmations:
        return random.choice(stage_confirmations[stage])
    return None


def get_final_confirmation():
    return random.choice(final_confirmations)

def get_stage_question(stage):
    if stage in stage_questions:
        return random.choice(stage_questions[stage])
    return None