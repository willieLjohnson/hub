import shutil
import os
import subprocess

def copy_folder(source_folder, destination_folder):
  """Copies a folder to a new location.

  Args:
    source_folder: The path to the source folder.
    destination_folder: The path to the destination folder.
  """

  shutil.copytree(source_folder, destination_folder)

def rename_folder(folder_path, new_name):
  """Renames a folder.

  Args:
    folder_path: The path to the folder to rename.
    new_name: The new name for the folder.
  """

  os.rename(folder_path, os.path.join(os.path.dirname(folder_path), new_name))

def main():
  """The main function."""

  project_name = input("Enter the project name: ")
  source_folder = "/home/wen/hub/templates/raylibgame"
  destination_folder = os.path.join(os.getcwd(), project_name)

  copy_folder(source_folder, destination_folder)
  rename_folder(destination_folder, project_name)
  print(destination_folder)

  txt_file_path = os.path.join(destination_folder, "CMakeLists.txt")
  with open(txt_file_path, "r") as txt_file:
    content = txt_file.read()
    content = content.replace("REPLACE_NAME", project_name)
  with open(txt_file_path, "w") as txt_file:
    txt_file.write(content)

  new_folder_path = os.path.join(destination_folder, "build")
  os.mkdir(new_folder_path)
  os.chdir(new_folder_path)
  subprocess.run(["bash", "-c", "cmake .. && cmake --build ."])

if __name__ == "__main__":
  main()


