from entities import Session
from fileService import FileService

class SessionService:
    
    def __init__(self, session: Session, base_path: str='./Recordings'):
        self.session = session
        self.fs = FileService()
        # Check that there are no other video files in the base folder
        assert len(self.fs.recordings(base_path)) == 0, f'{base_path} contains some video files already! Ensure that they are placed in the correct location.'
        self.base_path = base_path


    def start_session(self):
        """        
        Opens the VLC app for recording.
        """        
        pass            


    def set_destination_path(self):
        """
        Sets the destination folder for the recordings.
        """
        sub_dirs = [str(self.session.patient.id), str(self.session.date)]
        destination = self.fs.construct_path(self.base_path, sub_dirs)
        return destination
    
        
    def end_session(self):
        """        
        1. Transfers and organizes the recordings there.
        2. Closes VLC.
        """
        src, dest = self.base_path, self.set_destination_path()
        self.fs.organize_recorded_files(src, dest)        