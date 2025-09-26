#!/bin/bash

pip --version

python3 -m venv myenv

if [ -d "local_lib" ]
then
    rm -rf local_lib
    echo "Removed existing local_lib directory."
fi
mkdir -p local_lib

./myenv/bin/pip install path.py --target=local_lib > install.log 2>&1

python3 my_program.py
echo "Installation complete. Check install.log for details."
