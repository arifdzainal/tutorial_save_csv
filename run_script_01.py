import os
import csv

def get_latest_csv_file():
  """Returns the latest CSV file in the given folder."""
  files = os.listdir()
  csv_files = [f for f in files if f.endswith(".csv")]
  csv_files.sort(key=os.path.getmtime, reverse=True)
  return csv_files[0]

def read_csv_file(file_path):
  """Reads a CSV file and returns a list of rows."""
  rows = []
  with open(file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
      rows.append(row)
  return rows

def write_csv_file(file_path, rows):
  """Writes a list of rows to a CSV file."""
  with open(file_path, "w") as f:
    writer = csv.writer(f)
    for row in rows:
      writer.writerow(row)

def main():
  """Reads the latest CSV file from the given folder, opens it, and saves it back."""
  # folder_path = "K:\\My Drive\\Bill\\CIMB_CC"
  print("START THE CODE")
  file_path = get_latest_csv_file()
  rows = read_csv_file(file_path)
  
  # Open and save the file back
  write_csv_file(file_path, rows)
  print("COMPLETE SAVE THE FILES AGAIN")
if __name__ == "__main__":
  main()