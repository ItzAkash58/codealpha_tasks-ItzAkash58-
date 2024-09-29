import os
import shutil

root_dir = 'D:\Personal-2\Test Sub'
Organization = 'D:\Personal-2\Test Sub\Organization'

folders = {
    'txt': 'Text Files',
    'pdf': 'PDF Files',
    'jpeg': 'Image Files(JPEG)',
    'jpg' :  'Image Files(JPG)',
    'png': 'Image Files(PNG)',
    'mp3': 'Audio Files',
    'mp4': 'Video Files',
    'docx': 'Word Documents',
    'xlsx': 'Excel Files',
    'pptx': 'PowerPoint Files',
}

for filename in os.listdir(root_dir):
    file_ext = os.path.splitext(filename)[1][1:]

    if file_ext in folders:
        folder_path = os.path.join(Organization, folders[file_ext])
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        shutil.move(os.path.join(root_dir, filename), folder_path)

print("File organization complete!")