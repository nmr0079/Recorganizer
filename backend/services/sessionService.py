from entities import Session
from fileService import *


class SessionService:
    
    def __init__(self, session: Session, base_path: str='./Recordings'):
        self.session = session        
        # Check that there are no other video files in the base folder
        assert len(video_recordings(base_path)) == 0, f'{base_path} contains some video files already! Ensure that they are placed in the correct location.'
        self.base_path = base_path


    def start(self):
        """        
        Opens the VLC app for recording.
        """        
        pass


    def set_destination_path(self):
        """
        Sets the destination folder for the recordings.
        """
        sub_dirs = [str(self.session.department), str(self.session.patient.id), str(self.session.date)]
        destination = construct_path(self.base_path, sub_dirs)
        return destination
    
        
    def end(self):
        """
        Transfers the recordings from `src` to `dest` and organizes them.           
        """
        src, dest = self.base_path, self.set_destination_path()
        organize_recorded_files(src, dest)        