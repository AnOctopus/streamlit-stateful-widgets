import streamlit as st

state = st.session_state


def wrapped_multiselect(label, options, default_values, key):
    values = state.get(key, default_values)

    values = [v for v in values if v in options]

    multiselect = st.multiselect(label, options, values, key=key)
    return multiselect

def stateful(widget_fn):
    def stateful_widget(*args, options, value, key, **kwargs):
        values = state.get(key, value)

        values = [v for v in values if v in options]
        return widget_fn(*args, options, values, key=key, **kwargs)
    return stateful_widget

@stateful
def wrapped_multiselect_2(*args, **kwargs):
    return st.multiselect(*args, **kwargs)
