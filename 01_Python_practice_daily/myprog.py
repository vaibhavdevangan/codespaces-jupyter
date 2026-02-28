import sys

if len(sys.argv) != 3:
    print ('Usage: python myprog.py name age\n')
    sys.exit (1) # Exit the program, indicating an error with 1.

name = sys.argv [1]
age = int (sys.argv [2])

print (f'Hello {name} .')
print (f'{age} is a great age.\n')


#========How to run this program in terminal========
# 1. Open terminal and navigate to the directory where myprog.py is located.
# 2. Run the program using the command: python myprog.py Alice 30

# EXAMPLE OUTPUT
# PS C:\Daily_Python_class\codespaces-jupyter> cd C:\Daily_Python_class\codespaces-jupyter\Python_practice_daily          
# PS C:\Daily_Python_class\codespaces-jupyter\Python_practice_daily> dir 


# Directory: C:\Daily_Python_class\codespaces-jupyter\Python_practice_daily


# Mode                 LastWriteTime         Length Name
# ----                 -------------         ------ ----
# -a----        17-02-2026     11:47           1444 01_first.ipynb
# -a----        17-02-2026     11:47           1336 02_variables&identifiers.ipynb
# -a----        17-02-2026     11:47           1660 03_python_expressions.ipynb
# -a----        17-02-2026     11:47           1061 04_division_&_modulo.ipynb
# -a----        17-02-2026     11:47           1452 04_text_representation.ipynb
# -a----        17-02-2026     11:47           3377 05_dictionaries.ipynb
# -a----        17-02-2026     11:47           2691 06_if_else_if.ipynb
# -a----        20-02-2026     14:18       19918181 07_While_loops.ipynb
# -a----        20-02-2026     14:18           4296 08_for_loops.ipynb
# -a----        17-02-2026     11:47           2992 09_break_continue.ipynb
# -a----        17-02-2026     11:47           3172 10_phone_number_program.ipynb
# -a----        17-02-2026     11:47           2002 11_loop_else.ipynb
# -a----        17-02-2026     11:47           2185 12_enumerate().ipynb
# -a----        17-02-2026     16:11          11289 13_functions.ipynb
# -a----        19-02-2026     17:45          13558 14_Strings.ipynb
# -a----        23-02-2026     12:37          19401 15_Lists_in_py.ipynb
# -a----        24-02-2026     12:25           6959 16_Dictionary_data_type.ipynb
# -a----        24-02-2026     12:56            266 myprog.py
# -a----        19-02-2026     17:47           3452 Problem.ipynb


# PS C:\Daily_Python_class\codespaces-jupyter\Python_practice_daily> python myprog.py vaibhav 20
# Hello vaibhav .
# 20 is a great age.
