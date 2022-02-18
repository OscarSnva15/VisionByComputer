# Git generando rama apuntando a repositorio remoto

```shell
[uaemex@fedora computerVision]$ git init
ayuda: Usando 'master' como el nombre de la rama inicial. Este nombre de rama predeterminado
ayuda: está sujeto a cambios. Para configurar el nombre de la rama inicial para usar en todos
ayuda: de sus nuevos repositorios, reprimiendo esta advertencia, llama a:
ayuda: 
ayuda: 	git config --global init.defaultBranch <nombre>
ayuda: 
ayuda: Los nombres comúnmente elegidos en lugar de 'master' son 'main', 'trunk' y
ayuda: 'development'. Se puede cambiar el nombre de la rama recién creada mediante este comando:
ayuda: 
ayuda: 	git branch -m <nombre>
Inicializado repositorio Git vacío en /home/uaemex/Escritorio/projects/computerVision/.git/
[uaemex@fedora computerVision]$ git clone https://github.com/NoeVG/tracking-analytics
Clonando en 'tracking-analytics'...
Username for 'https://github.com': oscarsnva15
Password for 'https://oscarsnva15@github.com': 
remote: Enumerating objects: 185, done.
remote: Counting objects: 100% (185/185), done.
remote: Compressing objects: 100% (140/140), done.
remote: Total 185 (delta 75), reused 131 (delta 34), pack-reused 0
Recibiendo objetos: 100% (185/185), 23.28 MiB | 592.00 KiB/s, listo.
Resolviendo deltas: 100% (75/75), listo.
[uaemex@fedora computerVision]$ git branch -M ramaOscar
[uaemex@fedora computerVision]$ git remote add origin https://github.com/NoeVG/tracking-analytics
[uaemex@fedora computerVision]$ 


```
