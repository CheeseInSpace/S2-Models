from pathlib import Path
import subprocess
import os

for file in Path(".").rglob("*mrao*.png"):
    temp = file.with_name(file.stem + "_temp.png")

    subprocess.run([
        "magick",
        str(file),
        "-channel", "RGB",
        "-separate",
        "(",
        "+clone",
        ")",
        "-swap", "0,2",
        "-delete", "3",
        "-combine",
        str(temp)
    ], check=True)

    os.replace(temp, file)
    print(f"Converted: {file}")