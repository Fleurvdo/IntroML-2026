# Setting up a Python environment with uv

## What is uv?

uv is a simple and fast way to manage Python environments. It is significantly faster than conda and it is easier to use. The installation process is over the terminal but it is generally easier than installing conda. 

The main advantage of conda over uv is that conda can also manage things beyond Python packages — for example, NVIDIA graphics card drivers, which become important in advanced machine learning work.



## Installing uv


On **Windows**:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

```

On **Mac / Linux**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

In both cases you need to close and reopen the terminal (or VsCode to make uv available).

If you want to know more, you can follow the installation instructions on the [official uv website](https://docs.astral.sh/uv/getting-started/installation/) based on the operating system that you are using.


## Load the Packages

Open the terminal in the root directory of the lecture and type
```bash
uv sync
```
After that uv will install all packages and uv should be available as a kernel in your jupyter. The name of the kernel is always the name of the folder. In our case the class name of the current year YYYY: **IntroML-YYYY**

# More uv information
This was enough to follow the class and install all the packages. If you are interested you can read on.

## Activating the environment
Just like conda you can activate the environment manually if you are not using the VSCode jupyter kernel:

On **Mac / Linux**:
```bash
source .venv/bin/activate
```

On **Windows**:
```powershell
.venv\Scripts\activate
```

Your terminal prompt will show `(.venv)` to confirm the environment is active.


## Launching Jupyter Lab

```bash
jupyter lab
```

Shut it down with **Ctrl+C** in the terminal when you are done.

## Re-opening JupyterLab in future sessions

Each time you open a new terminal, reactivate your environment before launching Jupyter:

```bash
cd path/to/your/project
source .venv/bin/activate        # Mac / Linux
# or: .venv\Scripts\activate     # Windows
jupyter lab
```
