# Detección facial en tiempo real con OpenCV

Aplicación de visión por computador en Python que detecta rostros desde la webcam
mediante un clasificador Haar Cascade de OpenCV. El procesamiento en escala de
grises ayuda a mantener una respuesta fluida en tiempo real.

## Características

- Captura de vídeo desde la cámara predeterminada.
- Detección de rostros con Haar Cascade.
- Rectángulos de detección superpuestos al vídeo.
- Mensajes claros si no se puede cargar el modelo o abrir la cámara.
- Rutas portables: el proyecto puede ejecutarse desde cualquier directorio.

## Requisitos

- Python 3.12 o superior.
- Una webcam disponible.
- Windows, macOS o Linux con los permisos de cámara concedidos a Python.

## Instalación

Clona el repositorio y crea un entorno virtual:

```bash
python -m venv .venv
```

Actívalo:

```powershell
.\.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

## Ejecución

Desde la raíz del proyecto:

```bash
python Main.py
```

Presiona `q` para cerrar la ventana. Si la cámara no abre, comprueba que esté
conectada, que el sistema haya autorizado a Python y que otra aplicación no la
esté utilizando.

## Estructura

```text
Main.py                                   # Aplicación principal
Modelos/haarcascade_frontalface_default.xml # Clasificador preentrenado
requirements.txt                          # Dependencias de Python
```

## Limitaciones

Haar Cascade es una técnica rápida y apropiada para aprendizaje y prototipos,
pero puede perder precisión con poca luz, oclusiones o rostros muy inclinados.
Para casos de producción conviene evaluar detectores modernos y medir precisión,
latencia y sesgo con datos representativos.

## Vista previa

![Detección facial en tiempo real](https://github.com/user-attachments/assets/8ee10d32-95e8-45d1-b620-e272c689be83)

Desarrollado como parte del portafolio de Ingeniería de Software de UTP.
