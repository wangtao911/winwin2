import streamlit as st
import  random

txt = st.text_area(
    "请输入人员名单，从",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )
number = st.number_input('Insert a number',value=3)

txt_lines_list = txt.split(";")


def simple_lottery(participants, num_winners):
    """
    A simple lottery program where a specified number of winners are drawn from a list of participants.
    
    :param participants: A list of participants.
    :param num_winners: The number of winners to draw.
    :return: A list of winners.
    """
    if num_winners > len(participants):
        return "Number of winners cannot exceed the number of participants."

    return random.sample(participants, num_winners)

# Example usage
participants = txt_lines_list
num_winners = number

simple_lottery(participants, num_winners)


st.write(simple_lottery(participants, num_winners))
