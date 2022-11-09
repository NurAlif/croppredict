import streamlit as st
import time
'Menjalankan computation...'

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.03)
bar.success('Done!')\

# Updates the state
st.write("before : "+st.session_state['key'])
st.session_state.key = 'value2' # Attribute API
st.session_state['key'] = 'value2' # Dictionary like API
st.write("After : "+st.session_state['key'])