filename = 'my_file.txt'

try:
    print("Creating and writing to the file...")
    with open(filename, 'w') as file:
        file.write("First line of text.\n")
        file.write("Second line with a number: 42\n")
        file.write("Third line, more text.\n")
    print("File created and initial content written.")
except PermissionError:
    print("Permission denied: Unable to write to the file.")
except Exception as e:
    print(f"An error occurred during file creation: {e}")
finally:
    print("File creation block completed.")


try:
    print("\nReading the contents of the file...")
    with open(filename, 'r') as file:
        content = file.read()
        print("File contents:")
        print(content)
except FileNotFoundError:
    print("File not found: Unable to read the file.")
except PermissionError:
    print("Permission denied: Unable to read the file.")
except Exception as e:
    print(f"An error occurred during file reading: {e}")
finally:
    print("File reading block completed.")


try:
    print("\nAppending new lines to the file...")
    with open(filename, 'a') as file:
        file.write("Appending new line 1.\n")
        file.write("Appending new line 2.\n")
        file.write("Appending new line 3.\n")
    print("Additional lines appended to the file.")
except PermissionError:
    print("Permission denied: Unable to append to the file.")
except Exception as e:
    print(f"An error occurred during file appending: {e}")
finally:
    print("File appending block completed.")

print("\nFile handling operations completed.")
