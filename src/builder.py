import sys
import os
import pathlib

def print_usage():
    print("python builder.py <file.c> <width> <height> <emcc_parameters>")

if len(sys.argv) < 4:
    print_usage()
    exit(1)

# set pathes
FILE_PATH =  pathlib.Path(__file__)
WAPHICS_C_HOME = FILE_PATH.parent.parent

current_dir = pathlib.Path(os.getcwd())
try:
    file_c_input = pathlib.Path(sys.argv[1])
except:
    print("Invalid path")
    exit(1)
try:
    width = int(sys.argv[2])
except:
    print("Invalid width")
    exit(1)
try:
    height = int(sys.argv[3])
except:
    print("Invalid width")
    exit(1)

if not os.path.exists(current_dir / file_c_input):
    print(f"Invalid path, the file {current_dir / file_c_input} doesn't exist")
    exit(1)

file_c_path = current_dir / file_c_input

# set strings
if len(sys.argv) != 4:
    emcc_parameters = ' '.join(sys.argv[4:len(sys.argv)])
else:
    emcc_parameters = ''

emcc_command = f"emcc {file_c_path} -sEXPORTED_FUNCTIONS=_render,_init -sEXPORTED_RUNTIME_METHODS=ccall"
output_html = f"<script src='a.out.js'></script><script>\nlet width = {width};\nlet height = {height};\nlet channels = 4;\n</script><canvas id='canvas' width={width} height={height}></canvas><script src='waphics.js'></script>"

with open(WAPHICS_C_HOME / 'src/waphics.js', 'r') as reader_waphics_js:
    waphics_js = reader_waphics_js.read()

# output stuff
with open(file_c_path.parent / 'waphics.js', 'w') as writer:
    writer.write(waphics_js)

with open(file_c_path.parent / 'index.html', 'w') as writer:
    writer.write(output_html)

os.chdir(file_c_path.parent)
os.system(emcc_command)
os.chdir(current_dir)
