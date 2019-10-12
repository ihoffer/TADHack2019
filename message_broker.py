# coding=utf-8
import random

final_confirmations = [
    "I got your deets down, will be in touch...", "Peak. Let me gather the intel for you...",
    "No worries bossman, give me a minute..."
]

stage_confirmations = {
    "club": ["Oh geez, good choice, one of my favorites.", "Top choice from a top man.", "Legend."],
}

stage_questions = {
    "groupSize": ["What's your group size, m8?", "How many of ya?", "What's the size of your crowd?"]
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
