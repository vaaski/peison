def read_file_into_string(file_path):
  with open(file_path, 'r') as file:
    file_contents = file.read()
  return file_contents
