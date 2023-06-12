from utils import ui # User Interface
import menu


class App:
    def __init__(self):
        self._name = 'Recorganizer'
        self._menu = ['Recording Session, About']
        self._departments = ['Opthalmology', 'Urology', 'Cardiology']        
    
    
    def run(self):
        ui.set_title(self._name)
        menu_option = ui.select_menu_option('Menu', self._menu)        
        
        if menu_option == self._menu[0]:
            session = menu.create_recording_session(self._departments)            
            if ui.click('Start Session'):
                session_service = menu.start_session(session)
            if ui.click('End Session'):
                menu.end_session(session_service)
        
        elif menu_option == self._menu[1]:
            menu.show_about_page()
        

# Run the app
if __name__ == "__main__":
    app = App()
    app.run()
