# msc_thesis

## **Development requirements (Ubuntu)**

Install miniconda (Python environment handler)

```sh
    wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.11.0-Linux-x86_64.sh
    bash Miniconda3-py38_4.11.0-Linux-x86_64.sh
    conda create -n kivy python=3.8     # kivy=2.1.0
    conda activate kivy
```

Install kivy (Cross platform Python library for mobile development of applications)

```sh
    conda install kivy -c conda-forge
    conda install black # Optional for code styling
```

Test kivy

```
    python ~/miniconda3/envs/kivy5/share/kivy-examples/demo/showcase/main.py
```

## **Deployment requirements (Ubuntu)**

Requires a USB port available to connect a mobile or a bluetooth connection.

Install buildozer

```
    pip install buildozer
    pip install --upgrade Cython==0.29.19 virtualenv
```

Run buildozer

```sh
    cd <project_folder>
    buildozer init
    # Update data in buildozer.spec
    nano buildozer.spec

    # Option 1
    # Plug in your android device by USB cable and run:
    buildozer android debug deploy run
    # or
    buildozer android debug deploy

    # Option 2:
    buildozer android debug
    # or
    buildozer android release
    # And then copy the file created in /bin/ folder into the smartphone
    # by using bluetooth or USB cable.
```

VS Code extensions
```
    Monk3yDev.kvlang
    haddiebakrie.material-kv
```

## **Development and deployment alternative paths**

ALTERNATIVE PATHS

Install Python

```
    sudo apt-get install -y \
    python3-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
```

Install kivy

```
    python -m pip install --upgrade pip setuptools virtualenv
    python -m virtualenv kivy_venv
    source kivy_venv/bin/activate
    python -m pip install "kivy[base]" kivy_examples # or kivy[full]
```

Test kivy

```
    python ~/miniconda3/envs/kivy5/share/kivy-examples/demo/showcase/main.py
```

Install buildozer

```
    git clone https://github.com/kivy/buildozer.git
    cd buildozer
    sudo python setup.py install
    sudo apt update
    sudo apt install -y git zip unzip openjdk-13-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    pip install --upgrade Cython==0.29.19 virtualenv
    # add the following line at the end of your ~/.bashrc file
    export PATH=$PATH:~/.local/bin/
```

Run buildozer

```
    which buildozer
    cd <project_folder>
    buildozer init
    buildozer -v android debug
    buildozer android deploy run logcat
    [buildozer -v android deploy run logcat | grep python
    to see application’s print() messages and python’s error messages]
    buildozer -v android debug deploy run logcat [> my_log.txt]
    [buildozer setdefault android debug deploy run logcat
    # now just type buildozer, and it will do the default command
    buildozer]
```
