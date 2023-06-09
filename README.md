# Virtual Euclides

## **Description**

This project is a mobile application that allow the users to visualize and
interact with geometric 2D objects. The application is developed using Kivy,
a Python framework, which allows the application to be deployed on Android,
iOS, Windows or Linux devices. The application is designed to be used as a
complement for an introductory course of Euclidean Geometry or similar
subjects.

The teacher can use it to explain the initial concepts of Geometry and the
students can use the application to visualize and interact with the objects.

This is part of the thesis project for the Master degree in Teaching
Mathematics at the Universidad Tecnológica de Pereira (UTP).

<p align="center">
  <img src="https://leocjj.github.io/logo_utp_small.png" alt="Sticker">
</p>

## **Development requirements (Ubuntu)**

Install miniconda (Python environment handler)

```sh
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
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
    python ~/miniconda3/envs/kivy/share/kivy-examples/demo/showcase/main.py
```

## **Development requirements (Windows)**

Install miniconda (Python environment handler)

1. Download https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe
2. Execute Miniconda3-latest-Windows-x86_64.exe
3. Run the following commands in Anaconda Powershell Prompt:

```sh
    conda create -n kivy python=3.8
    conda activate kivy
```

Install kivy (Cross platform Python library for mobile development of applications)

```sh
    conda install kivy -c conda-forge  # Or use kivy=2.1.0 instead just kivy
    conda install black  # Optional for code styling
```

Test kivy

```
    python C:\Users\<user>\AppData\Local\miniconda3\envs\kivy\share\kivy-examples\demo\showcase\main.py
```

## **Deployment requirements (Ubuntu)**

Requires a USB port available to connect a mobile or a bluetooth connection.

Install buildozer (only in Linux or WSL)

```
    pip install buildozer
    pip install --upgrade Cython==0.29.19 virtualenv

    # Install Android SDK
```

Run buildozer

```sh
    cd <project_folder>
    buildozer init  # Create buildozer.spec file, only the first time.
    nano buildozer.spec  # Update data in buildozer.spec

    # Instalar Android Studio
    # https://developer.android.com/studio/install

    # Option 1
    # Plug in your android device by USB cable and run:
    buildozer android debug deploy run
    # or
    buildozer android debug deploy

    # Option 2:
    buildozer android debug
```

```sh
    # Seguir los siguientes pasos SOLO la primera vez:
    # https://developer.android.com/studio/publish/app-signing.html#generate-key
    export P4A_RELEASE_KEYALIAS=upload
    export P4A_RELEASE_KEYALIAS_PASSWD=12345678
    export P4A_RELEASE_KEYSTORE=~/thesis/keystores/upload-keystore.jks
    export P4A_RELEASE_KEYSTORE_PASSWD=12345678

    # https://kivy.org/doc/stable/guide/packaging-android.html#release-on-the-market
    # https://developer.android.com/studio/publish/app-signing.html#signing-manually
    # https://developer.android.com/

    buildozer android release

    # Go to: https://play.google.com/apps/publish
    ####  And then copy the file created in /bin/ folder into the smartphone
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
