import psutil


def get_process_using_file(file_path):
    for proc in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            for file in proc.open_files():
                if file.path == file_path:
                    return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return None


# Example usage
file_path = r'X:\mobeserv_projects\Keyword_extraction\Uploads\Genetics Explained in 3 Minutes.mp4'
process = get_process_using_file(file_path)

if process:
    print(f"Process {process.pid} ({process.name()}) is using the file.")
else:
    print("No process is using the file.")


def stop_ffmpeg():
    # Find the ffmpeg process by name
    for process in psutil.process_iter():
        if process.name() == 'ffmpeg':
            process.terminate()
            break
