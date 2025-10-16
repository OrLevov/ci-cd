# Frontend: serve /app static files with Nginx
FROM nginx:alpine
# Clean default page
RUN rm -rf /usr/share/nginx/html/*
# Copy your static assets
COPY app/ /usr/share/nginx/html/
# Healthcheck path will be /
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
