1.execute  the command in terminal-> git clone https://github.com/stablx/content1.stablx.com.git



2.open the cloned repository with an editor  preferably vscode.



3.execute the command in embedded terminal of the vscode -> python -m venv .



4.execute the command  windows -> ./Scripts/activate
       OR
  or in linux cd to bin folder and execute -> source activate



5.Checking cuda version onlly present in nvidia gpus
execute the command -> nvcc --version 
            OR
execute the command -> /usr/local/cuda/bin/nvcc --version
 


6.Installing the dependencies:

i)installing pytorch
 for windows without cuda support i.e (no gpu) execute
 pip install torch==1.5.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

 for linux without cuda support execute
 pip install torch==1.5.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

for mac ( MacOS Binaries dont support CUDA, install from source if CUDA is needed)
pip install torch torchvision

for windows with cuda 10.2
pip install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

for linux with cuda 10.2
pip install torch torchvision

for windows cuda 10.1
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

for linux cuda 10.1
pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

for linux cuda 9.2
pip install torch==1.6.0+cu92 torchvision==0.7.0+cu92 -f https://download.pytorch.org/whl/torch_stable.html

for windows cuda 9.2
# Follow instructions at this URL: https://github.com/pytorch/pytorch#from-source

ii)installing transformers

pip install transformers

iii)installing flask

pip install Flask


7)Inorder to change the model 
In app.py
In line no. 9 & 10 
replace "gpt2" with "gpt2-large" for 755 M model
OR
replace "gpt2" with "gpt2-xl" for 1.5B model


8)Press F1 in vscode and search for python:select Interpreter
  select the path to ./Scripts/python.exe (in windows)

  select the path to ./bin/python3.exe (in linux)

9)press ctrl+F5 in app.py to run it or python3 app.py in terminal

9)open http://localhost:5000 to view the web app


