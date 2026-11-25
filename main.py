"""One Star, Written in Sap — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The review: one star — watered monthly, expected to thrive, and I am not a cactus.
TEXT = "One star. My human waters me once a month and still expects me to thrive. I am not a cactus, and I am not impressed."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
