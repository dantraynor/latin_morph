import streamlit as st

# if "balloon_box" not in st.session_state:
#     st.session_state.balloon_box = st.session_state.balloons
# if "balloons" in st.session_state:
#     st.session_state.balloons = st.session_state.balloons

page_id = "main_page"
st.session_state.curr_page_id = page_id


st.markdown("""
            # Welcome to Latin Morph!
            
            **Latin Morph!** is a site for practicing your Latin morphology. 
            It takes its inspiration from [the Latin Driller Killer](https://hcmc.uvic.ca/project/latin/killer/index.htm) 
            but is not associated with any particular textbook, 
            and unlike the Latin Driller Killer, it has all five noun declensions 
            and all four verb moods (indicative, subjunctive, imperative, and infinitive).
            """)

# st.warning("The answer submission process has been streamlined: you now only need to press 'Check Answer' (or hit the Return key) in order to submit and check your answer.")

st.markdown("""
            :construction:
            All parts of speech should be fully operational! If you encounter any errors, please [report them](https://forms.gle/xT8hQ27sjposeXPc9).
            :construction:
            
            """)

# def balloon_toggle():
#     if st.session_state.curr_page_id == "main_page":
#         st.session_state.balloons = st.session_state.balloon_box

# st.checkbox("Do you want to see celebration balloons every time you get a question right? If so, select this box!", key="balloon_box", on_change=balloon_toggle)
# st.write(st.session_state.balloons)