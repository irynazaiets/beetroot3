def get_file_type(extension):
    match extension:
        case "txt":
            print("TXT")
            return "Text File"
        case "jpg" | "png" | "gif":
            print("Image")
            return "Image File"
        case "mp3" | "wav":
            print("Audio")
            return "Audio File"
        case "mp4" | "mkv":
            print("Video")
            return "Video File"
        case _:
            print("Unknown")
            return "Unknown File Type"

# Використання
print(get_file_type("txt"))  # Text File
print(get_file_type("mp3"))  # Audio File
print(get_file_type("exe"))  # Unknown File Type
