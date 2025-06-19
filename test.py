import cups
import os

conn = cups.Connection()
printer_name = conn.getDefault()

file_path = "/tmp/test_page.txt"

# Create a test file
with open(file_path, "w") as f:
    f.write("=== TEST PAGE ===\n")
    f.write(f"Printer: {printer_name}\n")
    f.write("This is a test print from Python in Docker.\n")

# Send to printer
conn.printFile(printer_name, file_path, "Test Page "555", {})
