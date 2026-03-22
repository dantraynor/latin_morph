import streamlit as st

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

st.warning("The answer submission process has been streamlined: you now only need to press 'Check Answer' (or hit the Return key) in order to submit and check your answer.")

st.markdown("""
            :construction:
            Currently, nouns, verbs, and pronouns are functional. 
            Next up will be adjectives and adverbs.
            :construction:
            
            """)

