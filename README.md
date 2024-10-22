# Simulating Solverbot person Follower with ROS 1 and Gazebo

![imagen mostrando el funcionamiento](https://github.com/mmvs1985/solver_ws/blob/main/image-in-action.png)
## Descripción

Este repositorio contiene el código fuente del simulador desarrollado para el proyecto "Creación de un robot de servicio en simulación Gazebo-ROS", según lo detallado en la tesis de Marcos Viera. El objetivo principal de este proyecto es desarrollar un robot de servicio simulado, capaz de asistir a personas mayores, utilizando las plataformas Gazebo y ROS (Robot Operating System).

## Características

- **Simulación en Gazebo**: Modelado preciso del robot Solverbot en un entorno virtual para pruebas y desarrollo.
- **Integración con ROS**: Uso de ROS para la gestión de nodos, comunicación y control del robot.
- **Visión Computacional**: Implementación de detección de personas utilizando OpenCV y algoritmos de Histogramas de Gradientes Orientados (HOG).
- **Interacción Humano-Robot**: El robot es capaz de seguir a una persona en el entorno simulado, manteniendo una distancia segura.
- **Interacción Humano-Robot**: El robot es capaz de seguir a una persona en el entorno simulado, manteniendo una distancia segura.

## Verlo en acción

[aqui](https://youtu.be/-oqxYBeqeW4?si=y1y5I2vw5ApOIhRW) 

## Instalación

1. **Pre-requisitos**: Asegúrate de tener instalado Ubuntu 20.04 y ROS Noetic. 
   - Instala Gazebo y ROS siguiendo las instrucciones en [Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu) y [ROS](http://wiki.ros.org/noetic/Installation/Ubuntu).

2. **Clona el repositorio**:
   ```bash
   git clone git@github.com:mmvs1985/solver_ws.git
    ```

3. **Configura el entorno de trabajo:**:
    ```bash
    cd ~/solver_ws/
    catkin_make
    source devel/setup.bash
    ```

# Uso

Para lanzar la simulación, ejecuta los siguientes comandos en tu terminal:


    roslaunch solver_description launcher_colision_actor.launch

Esto iniciará Gazebo con el modelo del Solverbot, permitiéndote interactuar con el robot en el entorno simulado.
Recuerda que escucha el topico cmd_vel por lo cual es perfectamente manejable con el paquete *teleop_twist_
teleop_twist_joy*  o  *teleop_twist_keyboard*

Los mismos se pueden correr con los comandos:

    rosrun teleop_twist_keyboard teleop_twist_keyboard.py

    rosrun teleop_twist_joy teleop_node
# Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor sigue estos pasos:
Haz un fork del repositorio.
Crea una rama para tu función (git checkout -b feature/AmazingFeature).
Realiza tus cambios y haz commit de ellos (git commit -m 'Add some AmazingFeature').
Empuja tus cambios a la rama (git push origin feature/AmazingFeature).
Abre una solicitud de pull.
Licencia
Este proyecto está licenciado bajo la Licencia CC BY-NC-SA - consulta el archivo LICENSE para más detalles.
Contacto
Marcos Viera
[Email](mailto://mmvsdev1985@gmail.com)