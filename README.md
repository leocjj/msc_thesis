# Virtual Euclides

<p align="center">
  <img src="https://leocjj.github.io/app_icon.png" alt="icon">
</p>

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
  <img src="https://leocjj.github.io/logo_utp_small.png" alt="UTP">
</p>

The Android version is already published here:

<p align="center">
  <a href="https://play.google.com/store/apps/details?id=co.edu.utp.virtualeuclides">
    <img src="https://leocjj.github.io/google-play-badge.png"
    alt="Get it on Google Play"
    width="200" height="80">
  </a>
</p>

---

---

# **Development requirements (Ubuntu)**

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

# **Development requirements (Windows)**

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

# **Deployment requirements (Ubuntu)**

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

---

---

# **Development and deployment alternative paths - In case of errors**

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

---

---

# Academic proposal - (Espanish version)

# Virtual Euclides

El principal objetivo de esta aplicación es **mejorar el proceso de aprendizaje
de la Geometría aplicada**, principalmente en estudiantes de ingeniería, para
lo cual se implementó una **metodología constructivista basada en la
interacción virtual** de objetos geométricos, usando la funcionalidad de touch
screen de los dispositivos modernos.

En resumen, esta metodología brinda al estudiante objetos gráficos que puede
manipular para obtener diferentes resultados, los cuales son explicados en cada
momento, con el fin de generar un **proceso inductivo** que va desde la
construcción de los elementos más básicos como **puntos y líneas,** hasta
llegar a la construcción de **superficies**.

## Propuesta

Con esta aplicacióno se pretende, entre otras cosas:

- Realizar un **proceso constructivista de objetos geométricos** basado en un
  proceso visual interactivo en plataformas móviles.
- Brindar una **ayuda didáctica de la Geometría desde sus bases más
  fundamentales**, durante el proceso de enseñanza-aprendizaje, de tal forma
  que permitan una mayor apropiación de los conceptos que son expuestos por
  medios tradicionales de una forma estática y contemplativa, versus una nueva
  forma dinámica e interactiva.
- **Aplicar una metodología de aprendizaje** que permite diferenciarla por un
  lado con aplicaciones que solo brindan un listado de fórmulas y/o
  calculadoras de objetos geométricos, o que solo muestran los conceptos con
  texto e imágenes estáticas. Incluso una combinación de estos dos tipos de
  aplicaciones no permite un aprendizaje desde la construcción del
  conocimiento, sino solo una apropiación de ideas no siempre conexas.

## Código abierto

Al crear esta aplicación como código abierto, usando tecnologías de fácil
aprendizaje por un entusiasta de la programación, la ingeniería o las ciencias
exactas, se deja una plataforma para futuros desarrollos que permitan ampliar
el alcance con respecto a la Geometría, o incluso explorar otras áreas del
conocimiento usando el mismo principio de aprendizaje constructivista por
interacción virtual.

---

# Recomendaciones iniciales

- Realizar el estudio de los contenidos presentados de forma secuencial, debido
  a que estos tienen una interrelación directa y de forma progresiva.

- Esta aplicación es una ayuda didáctica al proceso de aprendizaje, por lo cual
  el estudiante debe tener la responsabilidad de usarla adecuadamente de forma
  complementaria a un curso formal de Matemáticas, Geometría, dibujo de
  ingeniería o similares.

- A lo largo de los capítulos, secciones y páginas en los cuales están
  divididos los contenidos, se proponen temas, conceptos, nombres, ideas o
  actividades que pueden realizarse de forma complementaria y opcional. Se
  verán con diferente color en la siguiente forma: (`Actividad...`\_).

---

# Geometría

La definición de esta rama de la Matemática, una de las más antiguas junto con
la Aritmética, se dará de forma natural con el desarrollo de la propuesta
presentada en esta aplicación (`Consultar qué son los Elementos de Euclides`\_).

Es por esto que se omite intencionalmente una definición formal
(`Intentar dar una definición de Geometría al final de cada capítulo`\_) y esta
podrá darse por parte del Profesor de considerarse necesaria.

Es el principal interés en este punto poder presentar al estudiante, la forma
de trabajo recomendada y como explorar el contenido de los capítulos.

---

# Estructura general del contenido

El contenido se presenta dividido en capítulos, secciones (de capítulo) y
páginas (de sección).

## Capítulos

    Los capítulos se presentan en el **menú superior** a través de los cuales
    se puede **navegar usando las flechas** izquierda (ir al capítulo anterior)
    y derecha (ir al capítulo siguiente) en la parte superior derecha de la
    pantalla.

    Cada capítulo **tiene varias secciones asociadas** las cuales se despliegan
    al selecionarlo en este menú superior.

## Secciones

    Las secciones son las partes que **constituyen un capítulo** y cada una
    presenta **un tema específico**, el cual puede contener una o más páginas.

    Se accede a estas seleccionando (presionando o dando clic) sobre el espacio
    donde aparece el título del capítulo; allí se despliegan las secciones
    correspondientes y luego seleccionando la deseada.

## Páginas

    Por lo general, **cada sección contiene varias páginas** a través de las
    cuales se puede navegar usando las flechas izquierda (ir a la página
    anterior) y derecha (ir a la página siguiente) **en la parte superior**
    derecha de la pantalla.

    Al inicio del texto de cada página aparecerá un mensaje indicando el
    capítulo, la sección y la página actual.  Por ejemplo, en esta página
    aparace **Cap. 1 Sec. 0 Pag.2** al comienzo de este texto.

---

# Método recomendado

Cada página tiene por lo general la siguiente estructura, la cual se recomienda
seguir en el orden presentado (primero el espacio de interacción y luego el
espacio de lectura).

## Espacio de interacción

En la **mitad superior de la pantalla** se presenta un espacio gráfico el cual
contará con diferentes controles para interactuar con los objetos geométricos
presentados.

Los controles pueden ser de varios tipos pero fundamentalmente lo que buscan es
cambiar uno o más parámetros del gráfico y de esta forma interactuar con los
objetos.

**Es en el punto de partida de cada página**, donde el estudiante debe
interactuar para ver como cambian los objetos, buscando entender los conceptos
que se quieren presentar y revisando el texto dinámico que presenta información
importante sobre estos.

Por ejemplo, al mover los controles a un valor de 90 (por ejemplo grados) podría
mostrarse un texto y un valor de 180, o sea otro diferente. Se recomienda
intentar encontrar todos los casos posibles.

## Espacio de lectura

Este segundo espacio en la **mitad inferior de la pantalla**, muestra un
contenido que pretende presentar los objetos con los cuales se interactuó
previamente, explicar las situaciones especiales y dar los conceptos
importantes que refuerzan la actividad realizada.

---

# Descargo de responsabilidad (disclaimer)

Por otro lado hay ciertos aspectos que se deben mencionar, los cuales no son
parte del alcance del presente trabajo:

- Esta aplicación no pretende presentar un proceso demostrativo de los
  conceptos y no sustituye el estudio formal del contenido de un curso que
  implique los conceptos básicos de la Geometría Euclidiana.

- No se presenta una rigurosidad Matemática en la descripción de los objetos
  matemáticos, la cual hace parte de la responsabilidad del Profesor y no se
  pretende sustituirlo en su función.

- No contiene todos los objetos geométricos de estudio, ni se presenta como una
  lista exhaustiva de temas, solo se trabajan aquellos que el autor considera
  importantes (incluyendo el orden) para construir unas bases conceptuales
  sólidas que permitan al estudiante poder abordar otros objetos o conceptos
  geométricos.

- Por lo tanto, el orden de presentación de los conceptos sigue el orden que el
  autor consideró adecuado desde un punto de vista constructivista, inductivo,
  a partir de la experiencia con la interacción virtual de objetos geométricos.
  Y de este modo se recomienda seguir el orden propuesto para tener una mayor
  coherencia entre capítulos y secciones.

- En el contenido se presentan definiciones, postulados y nociones comunes del
  libro I de los Elementos de Euclides (de allí el nombre de la aplicación)
  pero no se pretende hacer una presentación completa y detallada al respecto,
  sino utilizar estos como referente conceptual para ahondar en la experiencia
  de interacción.

- Cuando se realizan cálculos matemáticos como resultado de la interacción
  gŕafica, en algunos momentos se pueden generar imprecisiones en algunos
  decimales debidos al cálculo mismo. Esto no debería interferir con el proceso
  de análisis de los conceptos presentados.

- Se utilizará la palabra **Geometría** para referirse a la Geometría Euclidiana
  en el plano, es decir, a la Geometría que cumple con los cinco postulados de
  Euclides y se trabajó solo en dos dimensiones (`Consulta cuáles son los cinco
postulados de Euclides`\_).

---

**RECUERDA**
!Seguir el orden propuesto, repasar cada sección y ... divertirte aprendiendo!

---
