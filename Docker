FROM nginx:alpine

# Copia nossa configuração personalizada para o Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Remove a página padrão do Nginx antes de copiar os nossos arquivos
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do site
COPY . /usr/share/nginx/html

# Expõe a porta 80
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
