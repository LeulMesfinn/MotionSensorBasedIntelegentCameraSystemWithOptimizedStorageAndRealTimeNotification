
import subprocess

# Execute the first Python script
subprocess.call(["python", "motion_detect_rec.py"])

# Execute the second Python script
subprocess.call(["python", "rec_compress.py"])

# Execute the third Python script
subprocess.call(["python", "email_notify.py"])

# All scripts have finished executing
print("all is done")

