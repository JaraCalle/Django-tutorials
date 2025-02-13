# Monorepositorio de Tutoriales - Tópicos de Ingeniería de Software

Este repositorio contiene una colección de proyectos desarrollados en **Django**, organizados como un **monorepositorio**. Cada carpeta padre representa un tutorial del curso **Tópicos de Ingeniería de Software**, y dentro de cada una se encuentra el proyecto Django correspondiente.

## 📂 Estructura del Repositorio

```
monorepo-tutoriales/
│-- tutorial-1/
│   ├── manage.py
│   ├── myapp/
│   ├── db.sqlite3
│   ├── requirements.txt
│   └── ...
│-- tutorial-2/
│   ├── manage.py
│   ├── myapp/
│   ├── db.sqlite3
│   ├── requirements.txt
│   └── ...
│-- tutorial-3/
│   ├── manage.py
│   ├── myapp/
│   ├── db.sqlite3
│   ├── requirements.txt
│   └── ...
│-- README.md
```

Cada carpeta contiene un **proyecto Django independiente**, con sus propios archivos de configuración, base de datos y dependencias.

## 🚀 Instalación y Configuración

Para ejecutar un proyecto de un tutorial en particular:

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/monorepo-tutoriales.git
   cd monorepo-tutoriales/tutorial-X
   ```

2. **Crear un entorno virtual y activarlo**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar migraciones y levantar el servidor**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. **Acceder al proyecto**
   Abre el navegador en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🛠 Dependencias
Cada proyecto puede tener sus propias dependencias, listadas en el archivo `requirements.txt`. Para asegurarte de instalar todo correctamente, usa el comando:
```bash
pip install -r requirements.txt
```

## 📌 Notas
- Cada proyecto Django es independiente.
- Se recomienda usar entornos virtuales para evitar conflictos de dependencias.
- Puedes cambiar de proyecto fácilmente navegando a la carpeta correspondiente y activando su entorno virtual.

## 📜 Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

---

**¡Feliz desarrollo! 🚀**

