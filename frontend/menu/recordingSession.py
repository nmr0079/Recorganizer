from utils import ui
from backend.entities import Patient, Session
from backend.services import SessionService


def create_recording_session(departments):
    """
    Creates a recording `Session` (for which a `Patient` is first created).
    """    
    p_id = ui.get_text_input('Patient ID')
    p_name = ui.get_text_input('Patient Name')    
    patient = Patient(p_id, p_name)
    # Can add more details about the patient here.
    # Eg: If you want to add information about the whereabouts of the patient:
    # p_place = ui.get_text_input('Place')
    # patient = Patient(p_id, p_name, p_place)
    
    selected_dept = ui.select_option('Select Department', departments)
    session = Session(patient, department=selected_dept)
    # Can add more fields here.
    # For each field, the template is `ui.select_option(<field_name>, <field_options>)`.
    # Eg: If you want to add a field for the type of video being recorded:
    # field_name = 'Video category'
    # field_options = ['Surgery', 'Education', 'Testimonial']
    # selected_category = ui.select_option(field_name, field_options)
    # session = Session(patient, department=selected_dept, category=selected_category)
    return session


def start_session(session):
    session_service = SessionService(session)   
    session_service.start()
    return session_service


def end_session(session_service):
    session_service.end()