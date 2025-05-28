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

Parar contenedores:

docker compose down

Reconstruir contenedores:

docker compose up -d --build

