# Generate a cheat sheet using Docker

You can create a cheat sheet using Docker. The following sections explain how to create
a Docker image and then containerize and attach this image to Visual Studio Code for
cheat sheet generation. Using Docker in this manner allows you to generate a cheat
sheet without worrying about dependencies and environment setup.

## Prerequisites
You must install all of the following prerequisites, ensuring that the Visual Studio Code
extensions are authored by Microsoft. After installation, ensure that these prerequisites
are enabled and working. For more information, see the documentation for each of the
prerequisites.

- Basic environment setup for Python development, which is described in the
  [Contributing to PyAnsys](https://github.com/ansys-internal/pyansys-trainings/raw/main/material/06-pyansys-examples/Contributing_to_PyAnsys_v1.0.pptx) PowerPoint file.
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Visual Studio Code Docker extension](https://code.visualstudio.com/docs/containers/overview)
- [Rancher Desktop app](https://rancherdesktop.io/)
- [Visual Studio Code WSL extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)
- [Visual Studio Code Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)


## Set up and use Docker to generate a cheat sheet:
#. Clone the ``pyansys-cheat-sheet`` with this command:

    ```bash
    git clone https://github.com/ansys/pyansys-cheat-sheet.git
    ```
#. Open the repository in Visual Studio Code and then open a new terminal.
#. Build the Docker image with this command:

    ```bash
    docker build -t pyansys-cheatsheet-dev-env:1.0 -f docker\Dockerfile .
    ```

   It takes approximately 15 to 25 minutes to build the Docker image. This process downloads
   all dependencies and installs them in the Docker image.    

#. Ensure that the Docker image is created with this command:

    ```bash
    docker image ls
    ```      
#. Run the Docker image with this command, which names the container `dev`:

    ```bash
    docker run --name dev -ti pyansys-cheatsheet-dev-env:1.0
    ```    
#. Ensure that the Docker container created in the Docker extension is active, as shown in this image.:<br>
![Docker Container](images/docker_container.png)<br>
#. In the bottom left corner of the Visual Studio Code window, click the WSL extension to open the command palette.<br>
![WSL VS Code Extenstion](images/wsl_vscode.png)<br>
#. Select `Attached to Running Container` and then select the `dev` container to open it in a new Visual Studio Code window.<br>
![Command Palette](images/wsl_vscode_options.png)<br>

   Now that this window is attached to the Docker container, you can use it for cheat sheet generation.<br>
![VS Code Attached Container Instance](images/vscode_container_instance.png)<br>
#. In the new Visual Studio Code window, go to the root directory of the repository and open the ``pyansys-cheat-sheet`` folder. This folder is mounted from the Docker container.
#. In this window, create, generate, and deploy the cheat sheet as indicated in the ``README.rst`` file for the repository.<br>
