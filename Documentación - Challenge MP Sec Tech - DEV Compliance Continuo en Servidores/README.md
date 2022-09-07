**Challenge MP Sec Tech - DEV Compliance Continuo en Servidores**

Con el fin de utilizar la solución ***CI/CD*** para cumplir con el reto de generar un agente que pueda recolectar la información de los servidores, tales como información sobre el procesador, listado de los procesos activos, usuarios con una sesión activa, nombre del sistema operativo, versión del sistema operativo, se explicará la arquitectura implementada.

**Arquitectura de la solución**

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.001.png)


**Explicación arquitectura**

1. Se utiliza GitHub Actions para desplegar la plataforma de Docker en el cual, se van a ejecutar las aplicaciones-agentes (Cliente/Servidor) y la Base de Datos donde se almacenará la información recolectada (Contenedores).
1. Se utilizará AWS CloudFormation como herramienta de despliegue de la infraestructura, la cual, estará integrada con GitHub por medio de API KEY y API SECRET.
1. Para el despliegue de la arquitectura se utilizará el repositorio ***https://github.com/aorrego17/challenge.git,*** el cual contiene los documentos y la lógica de aprovisionamiento. Para este caso, se tendrá como sistema operativo base Debian 11 y en él correrá el servicio de Docker.
1. En el Docker se desplegará el contenedor donde se alojará la API REST FUL que tendrá la lógica del reto, utilizando los métodos GET y POST como buenas prácticas de desarrollo (Agente).
1. La Base de Datos que se utilizará para persistir la información obtenida de cada servidor, por medio de la API, será MongoDB y esta será desplegada en <https://cloud.mongodb.com/>. Con esto, garantizamos el buen manejo de la información bajo los pilares de Confidencialidad, Integridad, Disponibilidad.
1. El usuario que requiera conocer la información almacenada en la Base de Datos, puede consultarlo por medio del endpoint <https://3.237.93.91:3000/list> 

***Nota:** Por temas prácticos del laboratorio se utilizaron certificados digitales autofirmados, por lo que antes de consumir el servicio, se debe instalar el certificado que se encuentra en la ruta del repositorio “challenge/challenge/cert”. Tener presente que en ambiente de producción esta no es muy buena práctica, por lo que se deben generar los certificados con entidades certificadoras oficiales.*

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.002.png)

A continuación, se describirán uno a uno los scripts utilizados en la solución.

**Documentación de los servicios y repositorios**

En la ruta: *challenge/.github/workflows* del repositorio, se encuentra el archivo ***”main.yml”*** que contiene:

1. La integración con GitHub por medio de ACCESS\_KEY\_ID y SECRET\_ACCESS\_KEY para el despliegue por medio de la funcionalidad Actions
1. La configuración del entorno y el aprovisionamiento de la instancia EC2 donde correrá la infraestructura Docker, ***“despliegueec2.yml*”**. Este será desplegado por AWS CloudFormation.

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.003.png)

En la raíz del repositorio se encuentra el archivo ***“despliegueec2.yml*”**, el cual contiene las características del Docker tales como:

1. AMI Debian 11 (ami-02c27944e9187fdb0).
1. Configuración de VPC y Subnets en donde correrán las instancias.
1. SecurityGroups para segregar los permisos de acceso, partiendo del mínimo privilegio.
1. Para la administración de la instancia se habilitaron dos opciones: Session Manager con roles de IAM y llave privada para acceso por ssh.

***Nota:** Para efectos del ejercicio, la regla del security group de administración (puerto 22-SSH) tiene configurado el acceso desde cualquier origen. Es una mala práctica contener reglas tipo any; sin embargo, se tiene el control de no publicar la llave privada.*

1. Parametrización del userdata. Este apartado de código es utilizado para personalizar la instancia de manera que pueda ejecutar los servicios de Docker. Como buenas prácticas de seguridad, se procede a crear el usuario **dockerlabmeli** quien cuenta con los privilegios para levantar el servicio de Docker y así, restringir el uso del usuario **root.**

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.004.png)

En la raíz del repositorio, también se encuentran los archivos ***“Dockerfile”*** y ***”Docker-compose.yml”*** los cuales tienen la lógica del despliegue de la infraestructura Docker.

`	`![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.005.png)

***Dockerfile***

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.006.png)

***docker\_compose.yml***

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.007.png)

En la ruta *“challenge/challenge”* se encuentra el archivo oculto **.env** en el cual reposan las credenciales de acceso a la Base de Datos y el nombre de la instancia que va a dejar corriendo; lo anterior, cumpliendo con el pilar de Confidencialidad de la información y buenas prácticas de desarrollo, evitando colocarlas en texto claro en los archivos de configuración.

Por último, se tiene el archivo **app.py** en la ruta *“challenge/challenge.* Este contiene toda la lógica de desarrollo y el cual, detallaremos a continuación:

1. Se tiene la configuración para conectarse a la Base de Datos Cloud Mongo, utilizando las variables de entorno que se comentaron en el punto anterior. 
1. Se crearon dos endpoint, uno para la obtención de la información sobre los servidores y el otro para la inserción de los mismos en la Base de Datos.

***Nota:** Por temas del laboratorio y para no generar inconvenientes, se deja corriendo el entorno para conservar la IP pública de consumo*

[*https://3.237.93.91:3000/list](https://3.237.93.91:3000/list)* 

[*https://3.237.93.91:3000/add](https://3.237.93.91:3000/add) *Utilizada sólo en los agentes*

1. Se creó un fragmento de código el cual consiste en identificar qué tipo de kernel tiene instalado y con base a ello, ejecuta la función.

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.008.png)


**Prueba de automatización**

Abrimos la URL del proyecto <https://github.com/aorrego17/challenge> y damos clic en las opciones que se enmarcan en la imagen.

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.009.png)

Luego de ejecutado el pipeline desde GitHub, se debe garantizar que cada tarea haya terminado sin inconvenientes. Esta actividad puede tardar de 5 a 7 min. Aproximadamente.

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.010.png)

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.011.png)

En la consola de AWS CloudFormation se puede observar el progreso

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.012.png)

Luego, se muestra que el despliegue fue satisfactorio, tanto en el GitHub Actions como en AWS CloudFormation

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.013.png)

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.014.png)

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.015.png)

Recordemos que, por temas del laboratorio se están usando certificados autofirmado y no es una buena práctica.

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.016.png)![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.017.png)

![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.018.png)![](Aspose.Words.a159813b-eda4-43ae-a9c0-65bb489fa9cf.019.png)

