FROM nginx:stable-alpine
WORKDIR /app
COPY /app/build /usr/share/nginx/html