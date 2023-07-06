[![logo2-Green-In-House.png](https://i.postimg.cc/QCYF3fSH/logo2-Green-In-House.png)](https://postimg.cc/7J7H1MFk)

# Green In House

Green In House es una maceta educativa que utiliza la tecnología para facilitar el cultivo de plantas de manera interactiva y didáctica.

## Descripción

Este proyecto consiste en una maceta educativa que utiliza una Raspberry Pi y diversos sensores para monitorear y controlar el entorno de crecimiento de las plantas. La aplicación principal está desarrollada en Python, utilizando la librerías SQLAlchemy para gestionar su servicio de base de datos, OpenAPI para gestionar su servidor API REST, AdaFruit CircuitPython interactuar con los sensores y TKinter para generar una aplicación gráfica pensada para ser desplega en una pantalla táctil. 

Además, se ha desarrollado una aplicación móvil utilizando Flutter para brindar una interfaz intuitiva y accesible para los usuarios, la cual esta accesible desde el siguiente repositorio:
https://github.com/ove1001/GreenInHouse_MobileApp

La documentación técnica completa de Green In House se puede encontrar en el siguiente repositorio:
https://github.com/ove1001/GreenInHouse_Doc

## Funcionalidades

- Monitoreo de la temperatura, humedad y luminosidad del entorno y humedad de la tierra de la maceta.
- Registro y análisis histórico de los registros de los factores del entorno que afectan al crecimiento de las plantas.
- Posibilidad de añadir nuevos sensores al sistema , crear plantas para diferenciar históricos y crear y personalizar consejos de cuidado de tus plantas a través del servidor API REST


## Instalación

1. Clona este repositorio en tu Raspberry.
2. Accede a la carpeta de scripts
   
**cd ./GreenInHouse_PlantPot/scripts**

3. Ejecuta el siguiente comando para instalar el sistema completo:
   
**sudo ./GIH-install.sh**

4. Cuando Green In House se termine de instalar, tu raspberry se reiniciará.
5. Al encender, Green In House se terminará de configurar y se arrancarán automáticamente todas sus funcionalidades.

Para conocer más en profundidad como funciona el sistema y todas las posibilidades que ofre, se recomienda acudir a la documentación técnica alojada en el repositorio antes mencionado.

## Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas de mejora, sugerencias o encuentras algún problema, no dudes en abrir un issue o enviar un pull request.

## Contacto

Si tienes alguna pregunta, necesitas más información o quieres colaborar con migo, puedes contactarme a través de mi dirección de correo electrónico: ove1001@alu.ubu.es.

## Licencia

MIT License

Derechos de autor (c) [Año] [Nombre del titular de los derechos de autor]

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricciones, incluyendo, sin limitación, los derechos de uso, copia, modificación, fusión, publicación, distribución, sublicencia y/o venta de copias del Software, y para permitir a las personas a las que se les proporcione el Software hacerlo, sujetas a las siguientes condiciones:

El presente aviso de derechos de autor y el siguiente aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO, PERO NO LIMITADO A, LAS GARANTÍAS DE COMERCIABILIDAD, APTITUD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, QUE SURJA DE O EN RELACIÓN CON EL SOFTWARE O EL USO U OTROS NEGOCIOS EN EL SOFTWARE.
