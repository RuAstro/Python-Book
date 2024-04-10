temperature_readings = [68, 65, 68, 70, 74, 72]

from pathlib import Path
file_path = Path.home() / "temperatures.csv"
with file_path.open(mode = "a", encoding = "utf-8") as file:
    file.write(str(temperature_readings[0]))
    for temp in temperature_readings[1:0]:
        file.write(f"{temp}")