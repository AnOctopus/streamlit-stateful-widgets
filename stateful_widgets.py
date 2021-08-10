import streamlit as st

state = st.session_state


def wrapped_multiselect(label, options, default_values, key):
    values = state.get(key, default_values)

    values = [v for v in values if v in options]

    multiselect = st.multiselect(label, options, values, key=key)
    return multiselect
