RPA de Verificación de Stock - Demo
Este proyecto es un Robot de Procesos Automatizados (RPA) que verifica el stock de productos en línea usando Selenium y Google App Engine. Se ha desarrollado como un demo para un webinar, donde se muestra cómo automatizar la consulta de stock de un producto en un sitio web como MercadoLibre o Amazon. Los resultados son enviados por correo electrónico y almacenados en Google Firestore para su registro.

**Tecnologías Utilizadas**
1. **Python** 3.12
2. **Flask:** Framework ligero para la creación de APIs y manejo de solicitudes.
3. **Selenium:** Para automatizar la navegación y scraping en los sitios web.
**Google Cloud Platform (GCP):**
5. **App Engine:** Para desplegar y ejecutar el RPA.
6. **Secret Manager:** Almacenamiento seguro de credenciales y secretos.
7. **Firestore:** Para registrar los resultados de la verificación de stock.
8. **Gunicorn:** Servidor WSGI para la producción.

**Funcionalidades Principales**
- **Verificación de Stock:** El RPA accede a la página de un producto en línea, verifica si hay stock disponible y obtiene el estado actual.
- **Almacenamiento en Firestore:** Cada consulta de stock se guarda en Firestore para su historial.
- **Envío de Correo:** Si se detecta un cambio en el stock, se envía una notificación por correo.
- **Seguridad:** Las credenciales y secretos se almacenan de forma segura usando Google Secret Manager.
