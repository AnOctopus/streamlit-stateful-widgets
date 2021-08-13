import streamlit as st

state = st.session_state


def persistent_multiselect(label, options, default_values, key):
    """A persistent multiselect widget, to demonstrate writing one on top of
    regular multiselect and session state.
    """
    values = state.get(key, default_values)

    values = [v for v in values if v in options]

    multiselect = st.multiselect(label, options, values, key=key)
    return multiselect








# I wrote this to see how a decorator approach would work, but writing this kind
# of wrapper function that works for generic widgets would be a lot of work for
# not much gain. Also it doesn't make sense to use it as an actual decorator,
# because that only exists to simplify the wrapper function pattern when you're
# defining a new function, not when you already have one.
def stateful(widget_fn):
    def stateful_widget(*args, options, value, key, **kwargs):
        values = state.get(key, value)

        values = [v for v in values if v in options]
        return widget_fn(*args, options, values, key=key, **kwargs)
    return stateful_widget

@stateful
def wrapped_multiselect_2(*args, **kwargs):
    return st.multiselect(*args, **kwargs)

wrapped_multiselect_3 = stateful(st.multiselect)
