# Pebble Dev ARM Linux Docker Image

A Docker image for working with the Pebble SDK (for Pebble watches) on ARM Linux systems.  
Includes Pebble SDK + emulator + debugging tools + helper scripts.


## Features

* Runs the Pebble SDK in a container on ARM Linux systems.
* Ability to use `pebble` command just like on Linux
* **Working graphical emulator** (`pebble install --emulator ...` command)
* **Debugging support** — includes `gdb-multiarch`, so `pebble gdb ...` command works.


## Limitations

⚠️ **Important**: Not all functionality is implemented:

* **JavaScript engine is not working** — The JavaScript runtime (STPyV8) has been replaced with a lightweight Duktape-based alternative for ARM compatibility, but it doesn't fully support all PebbleKit JS features.
* **Phone-side code emulation is not working** — Code that runs on the phone (PebbleKit JS) cannot be emulated.
* **Configuration pages are not working** — The `pebble emu-app-config ...` command does not work due to missing JavaScript engine support.


## How it works

The `pebble` script provides seamless container management, so you don't need to worry about Docker commands.

When you run `pebble`, it automatically:
  * Makes up a container name based on the current directory path (your project path), so it's unique for each project, even if you use a single `pebble` file
  * Creates a new container if one doesn't exist for the current directory, mounts the current directory (project directory) into the container
  * Starts the container if it exists but is stopped
  * Uses the running container to execute `pebble` command, automatically passes all command line arguments to the Pebble SDK inside the container
  * Automatically stops the container if `pebble` command is not used for some time (30 minutes by default, configurable via `STOP_AFTER` environment variable)

It also has additional command line arguments:
  * `pebble docker-stop` — stops the container
  * `pebble docker-rm` — removes the container
  * `pebble docker-purge` — removes all containers created by this image
  * `pebble docker-purge-all` — removes all containers and images created by this project

This design ensures containers don't consume resources when idle, while keeping them ready for immediate use when you're actively developing. Multiple `pebble` command instances can communicate with each other inside the container, so you can run `pebble install --emulator ...` and then `pebble gdb ...`.


## Prerequisites

Before using this image, please ensure you have the following set up:


### 1. Docker installed

Make sure Docker is installed and running on your ARM Linux system.


### 2. X11 forwarding (for emulator)

If you want to use the graphical emulator, X11 forwarding is required. **The `pebble` script handles all X11 setup automatically** — you don't need to configure anything manually.

The script automatically:
* Sets `DISPLAY` environment variable (defaults to `:0` if not set)
* Mounts X11 socket (`/tmp/.X11-unix`)
* Mounts X11 authority (`~/.Xauthority`)
* Allows X11 connections (`xhost +SI:localuser:root`)

Just make sure you have an X server running (if using a desktop environment, it's usually already running).


## Usage

Download a file named `pebble` on the [GitHub Releases page](https://github.com/ClusterM/pebble-dev-arm-linux/releases).

Make it executable:
```bash
chmod +x pebble
```

Place this file either:
* In your project directory (so you can run it locally) or
* In a folder included in your `PATH` (so you can invoke `pebble` from anywhere).


### Use the `pebble` CLI exactly like on x86 Linux

Examples:
* `pebble build` – compiles your project.
* `pebble install --emulator basalt` – installs the built app into the emulator.
* `pebble install --phone 10.13.14.15` – installs the app to a real Pebble watch connected via phone (use your phone IP).
* `pebble new-project MyWatchApp` – creates new project.
* `pebble gdb` – starts debugging session (requires `-it` flag, handled automatically).


## Support the Developer and the Project

* [GitHub Sponsors](https://github.com/sponsors/ClusterM)
* [Buy Me A Coffee](https://www.buymeacoffee.com/cluster)
* [Sber](https://messenger.online.sberbank.ru/sl/Lnb2OLE4JsyiEhQgC)
* [Donation Alerts](https://www.donationalerts.com/r/clustermeerkat)
* [Boosty](https://boosty.to/cluster)
