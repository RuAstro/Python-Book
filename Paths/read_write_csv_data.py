temperature_readings = [68, 65, 68, 70, 74, 72]

from pathlib import Path
file_path = Path.home() / "temperatures.csv"                        #creates file in home directory
with file_path.open(mode = "a", encoding = "utf-8") as file:        #opens it in append mode
    file.write(str(temperature_readings[0]))                        
    for temp in temperature_readings[1:0]:                          #each remaining value in the list is written, preceded by a comma, to the same line
        file.write(f"{temp}")
        
temperature_readings = [68, 65, 68, 70, 74, 72]     

with file_path.open(mode = "r", encoding = "utf-8")as file:
    text = file.read()
    
text
    
temperatures = text.split(",")
temperatures