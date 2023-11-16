import streamlit as st
import  random
image='https://images.pexels.com/photos/15401444/pexels-photo-15401444.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
st.image(image)

txt = st.text_area(
    "请输入人员名单，从企微群中直接copy即可",
    "我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；"
    "我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；我要中奖；",
    )
number = st.number_input('中奖人数',value=3)

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







st.button("Reset", type="primary")
if st.button('开始抽奖'):
    simple_lottery(participants, num_winners)
    st.write(simple_lottery(participants, num_winners))
    
else:
    st.write('祝愿好运')