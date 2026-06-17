# TRABAJO PRÁCTICO INTEGRADOR: ORGANIZACIÓN EMPRESARIAL
## Optimización y Automatización de Procesos - Asistente Virtual Kiosco "El Paso"

### Integrantes:
Agustin Schmaedke



### Descripción del Proyecto
Este proyecto de simulación consiste en la reingeniería y automatización del proceso crítico de **Toma de Pedidos y Reserva de Stock** para el Maxikiosco "El Paso". El objetivo principal es transformar un modelo de atención tradicional e ineficiente (As-Is) en un flujo digital optimizado (To-Be). 

A través de un Asistente Virtual desarrollado en Python, el sistema ejecuta reglas de negocio en tiempo real: validación de identidad del cliente, consulta dinámica de inventario (bloqueo por quiebre de stock) y asignación automática de beneficios comerciales (Descuentos VIP).



### Arquitectura Técnica y Componentes
El software fue diseñado bajo los lineamientos metodológicos de la cátedra, garantizando una traducción directa entre el modelo BPMN 2.0 y el código fuente:

1. **Persistencia de Datos (Simulada):** Estructuras de datos indexadas (Diccionarios) que emulan tablas relacionales de Clientes e Inventario con actualización de existencias en tiempo real.
2. **Máquina de Estados Finita (FSM):** Gestión de estados lógicos (`INICIO`, `ESPERANDO_CLIENTE`, `MENU_PRODUCTOS`, `CONFIRMACION`) que le otorgan "memoria" a la sesión del usuario.
3. **Control del "Camino Infeliz":** El sistema cuenta con mecanismos de robustez para la mitigación de errores de entrada por parte del usuario (formatos de ID incorrectos, opciones fuera de rango) y excepciones de negocio (quiebre de stock de productos).



### Instrucciones de Ejecución del Simulador

Para inicializar y testear el comportamiento del chatbot interactivo en entorno de consola, siga estos pasos:

1. Asegúrese de contar con **Python 3.x** instalado en su sistema operativo.
2. Descargue o clone el archivo `bot_soporte.py` presente en este repositorio.
3. Abra su terminal o consola de comandos en la ruta donde se encuentra el archivo.
4. Ejecute el siguiente comando:
   ```bash
   python bot_soporte.py
