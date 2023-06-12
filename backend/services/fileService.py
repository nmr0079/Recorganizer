import os
import glob
import shutil


def video_recordings(self, path: str, video_formats=['mp4']) -> list[str]:
    """
    Returns a list of video files present in the given `path`.
    """
    video_files = []
    for format_pattern in self.video_formats:
        video_files.extend(glob.glob(os.path.join(path, f'*.{format_pattern}')))
    return video_files
    

def construct_path(self, base_path: str, sub_dirs: str) -> str:
    """
    Creates a path by concatenating the `base_path` and the sub directories, `sub_dirs`, in a platform-independent way.
    """
    return os.path.join(base_path, sub_dirs)


def organize_recorded_files(self, src_path: str, dest_path: str) -> None:
    """
    Moves the recordings from `src_path` to `dest_path`;
    Maintains the order in which the recordings were created;
    Renames the files with natural numbers in order.
    """
    # Create the destination folder if does not already exist. 
    os.makedirs(dest_path, exist_ok=True)

    # Get a list of recorded files in the source directory.
    current_session_files = self.video_recordings(src_path)

    # Sort the recorded files based on their creation time.
    current_session_files.sort(key=os.path.getctime)

    # Get the highest file number already present in the destination directory.
    prev_files = self.video_recordings(dest_path)
    highest_number = len(prev_files)

    # Move and rename the recorded files to the destination directory.
    for i, file_path in enumerate(current_session_files):
        # Rename the file with the next available number.
        new_file_name = str(highest_number + (i+1)) + os.path.splitext(file_path)[1]
        new_file_path = os.path.join(dest_path, new_file_name)
        shutil.move(file_path, new_file_path)



if __name__ == '__main__':
    pass