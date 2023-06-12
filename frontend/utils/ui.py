import streamlit as st


def set_title(title: str):
    st.title(title)


def display_text(text: str):    
    st.write(text)


def get_text_input(field: str) -> str:
    """
    Takes in information, as required by `field`,
    from the user as text input, and returns it.
    """
    return st.text_input(field)


def select_menu_option(menu: str, menu_options: list) -> str:
    """
    Returns the selected option in the `menu`.
    """
    return st.sidebar.selectbox(menu, menu_options)


def select_option(field: str, list_of_options: list) -> str:
    """
    From the `list_of_options` provided under `field`,
    the function returns the selected option.
    """
    return st.selectbox(field, list_of_options)


def click(field: str) -> bool:
    """
    Defines a button for the given `field` and
    returns if the button was clicked or not.
    """
    return st.button(field)