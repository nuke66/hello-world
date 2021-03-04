# hello-world
"Hello world" project in micropython for Rasp Pi Pico using VS Code with linting (micropython-cli)

The setup is based on this tutorial.  However there is an error in one of the steps, "micropy stubs add micropython-rp2-1_13-290" is wrong as it doesn't exist in his solution, instead change "micropython-rp2-1_13-290" to the full path of the ...\Pico-Stub\dist\micropy-cli director.
https://medium.com/all-geek-to-me/developing-for-the-raspberry-pi-pico-in-vs-code-getting-started-6dbb3da5ba97


I'm assuming you have Python set up, with NodeJS and VS Code installed and you're working in Windows 

Install these packages (on the command line):
```
pip install micropy-cli
pip install pylint
```

Download this project (with the zip or clone the repo):
```
https://github.com/cpwood/Pico-Stub
```

Run this command on the command line but changing the path to the ..\Pico-Stub\dist\micropy-cli directory to wherever it is located on your computer:
```
micropy stubs add Z:\dev\Pico-Stub\dist\micropy-cli
```

In VS Code install these extensions:
```
ms-python.python
VisalStudioExptTeam.vscodeintellicode
Pico-Go
```

Download this repo (download the zip or clone it)

In the main folder for the project (i.e. the ...\Hello-word directory) run this on the command line:
```
micropy init
```

Now in VS Code you should see intellisense code completion happening, and when you plug in your rasp pi you should see it connect in the terminal window

![screenshot](https://user-images.githubusercontent.com/23091874/109891367-a51d3d80-7cd4-11eb-8cde-c947a83ed1f8.png)
