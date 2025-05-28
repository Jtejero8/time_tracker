WorkTime Tracker

Sistema web dockerizado para registrar horas de trabajo, con backend FastAPI, frontend React + Tailwind y base de datos PostgreSQL.

📁 Estructura del proyecto

project-root/
├── backend/
├── frontend/
├── nginx/
└── docker-compose.yml

🚀 Cómo levantar el proyecto

1️⃣ Clona o copia todos los archivos en tu servidor Ubuntu 24.2️⃣ Sitúate en la raíz del proyecto:

cd project-root

3️⃣ Construye y levanta los contenedores:

docker compose up -d --build

4️⃣ Accede en el navegador a:

Frontend: http://localhost (o tu dominio)

Backend API: http://localhost/api

🔒 Activar HTTPS con Let’s Encrypt (opcional)

1️⃣ Instala certbot en tu servidor.
2️⃣ Usa certbot para generar los certificados:

sudo certbot certonly --standalone -d yourdomain.com

3️⃣ Copia los certificados a la ruta que espera Nginx:

/etc/letsencrypt/live/yourdomain.com/fullchain.pem
/etc/letsencrypt/live/yourdomain.com/privkey.pem

4️⃣ Edita el archivo nginx/default.conf, descomenta el bloque HTTPS y reinicia Nginx:

docker compose restart nginx

⚙️ Comandos útiles

Ver logs:

docker compose logs -f

Parar contenedores:

docker compose down

Reconstruir contenedores:

docker compose up -d --build

✅ Ahora tienes todos los bloques (1 al 5) entregados. Solo organiza las carpetas, empaquétalas si quieres:

zip -r worktime-tracker.zip project-root/

¡Y listo para producción!

Si quieres, puedo prepararte también un script de instalación automatizada. 🚀

=======
# time_tracker
time checking work tool
>>>>>>> 4ac7ac5d12cf2ded2c0400c37b07b36793964ec1
