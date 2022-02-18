# Virtual Environment configuration desktop to dependences on python

```shell
(environment_oscar-env) [uaemex@fedora virtual_environment]$ python --version
Python 3.10.2
(environment_oscar-env) [uaemex@fedora virtual_environment]$ sudo dnf install python3-pip
Última comprobación de caducidad de metadatos hecha hace 1:11:29, el jue 17 feb 2022 16:39:28.
El paquete python3-pip-21.2.3-4.fc35.noarch ya está instalado.
Dependencias resueltas.
Nada por hacer.
¡Listo!
(environment_oscar-env) [uaemex@fedora virtual_environment]$ pip3 install --upgrade pip
Requirement already satisfied: pip in ./environment_oscar-env/lib/python3.10/site-packages (21.2.3)
Collecting pip
  Using cached pip-22.0.3-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.3
    Uninstalling pip-21.2.3:
      Successfully uninstalled pip-21.2.3
Successfully installed pip-22.0.3
(environment_oscar-env) [uaemex@fedora virtual_environment]$ pip3 install opencv-python
Collecting opencv-python
  Using cached opencv_python-4.5.5.62-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (60.4 MB)
Collecting numpy>=1.19.3
  Using cached numpy-1.22.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
Installing collected packages: numpy, opencv-python
Successfully installed numpy-1.22.2 opencv-python-4.5.5.62
(environment_oscar-env) [uaemex@fedora virtual_environment]$ pip3 install opencv-contrib-python
Collecting opencv-contrib-python
  Using cached opencv_contrib_python-4.5.5.62-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (66.6 MB)
Requirement already satisfied: numpy>=1.19.3 in ./environment_oscar-env/lib/python3.10/site-packages (from opencv-contrib-python) (1.22.2)
Installing collected packages: opencv-contrib-python
Successfully installed opencv-contrib-python-4.5.5.62
(environment_oscar-env) [uaemex@fedora virtual_environment]$ cd..
bash: cd..: command not found...
(environment_oscar-env) [uaemex@fedora virtual_environment]$ cd ..
(environment_oscar-env) [uaemex@fedora projects]$ ls
computerVision  virtual_environment  workshop_projects
(environment_oscar-env) [uaemex@fedora projects]$ cd computerVision

```
