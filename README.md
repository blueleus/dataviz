## Visualización de datos
### Proyecto
Para analizar datos de un archivo CSV o Excel y trazarlo con matplotlib. Los ejemplos incluyen: analizar los datos de la delincuencia local y visualizar con qué frecuencia ocurre la delincuencia los lunes frente a los jueves, etc.

Sigue el tutorial completo [aquí](http://newcoder.io/dataviz)

### Instala los paquetes requeridos.
```bash
sudo apt-get install python3-dev python3-pip python3-virtualenv python3 python3-tk
```

### Porque no se puede instalar python3-tk con pip
No puede instalar python-tk usando pip!
Como tk es TkInter (-> Interfaz a TK, que está escrito en C(++)), debe instalar el TK de la biblioteca de C(++).

no puede instalar esta biblioteca usando pip, ya que pipestá diseñado para instalar (principalmente) paquetes de python puros.
Fuente [aquí](https://askubuntu.com/questions/505141/unable-to-install-import-tkinter)