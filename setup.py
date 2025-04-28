from setuptools import setup, find_packages

setup(
    name='django-auth-goblin',  # Nombre de tu paquete
    version='0.1',  # Versión inicial
    description='Paquete de autenticación basico personalizado para Django',  # Descripción breve
    long_description=open('README.md').read(),  # Contenido más detallado del paquete
    long_description_content_type='text/markdown',  # Formato del archivo README.md
    author='Daniel Perdomo',  # Tu nombre
    author_email='daniel.perdomo.1987@gmail.com',  # Tu correo electrónico
    url='https://github.com/GoblinSwarm/django-auth-goblin',  # Enlace a tu repositorio de GitHub (si tienes)
    packages=find_packages(),  # Busca automáticamente todos los paquetes en el proyecto
    include_package_data=True,  # Incluir archivos estáticos y plantillas
    install_requires=[  # Las dependencias necesarias para tu paquete
        'django>=3.0',  # Django 3.0 o superior
    ],
    classifiers=[  # Clasificación del paquete
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',  # Versión de Python requerida
)
