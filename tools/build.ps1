pyinstaller --distpath ./build/build --distpath ./build/install --specpath ./build --noconsole -D ./src/datasets_tools.py

Copy-Item ./src/page ./build/install/datasets_tools -recurse -force

# -i ../resource/main.ico --key 'lolikonloli' 