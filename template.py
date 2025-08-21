import os

# Directories to create
directories = [
    "src",
    "research"
]

# Files to create
files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "requirements.txt"
]

def create_directories(dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def create_files(file_list):
    for f in file_list:
        # Ensure parent directory exists
        if os.path.dirname(f):
            os.makedirs(os.path.dirname(f), exist_ok=True)
        # Create file if it doesn't exist
        if not os.path.exists(f):
            with open(f, "w") as fp:
                pass  # leave empty

if __name__ == "__main__":
    create_directories(directories)
    create_files(files)
    print("Directory and files created successfully!.")
