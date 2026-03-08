import re

log_file = "auth_logs.txt"

with open(log_file, "r") as file:
    logs = file.readlines()

for line in logs:
    if "failed login" in line.lower():
        print("Suspicious activity detected:", line)
