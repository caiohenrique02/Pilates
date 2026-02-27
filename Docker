FROM nginx:alpine

# Remove a página padrão do Nginx antes de copiar os nossos arquivos
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do site para o diretório padrão do Nginx
COPY . /usr/share/nginx/html

# Expõe a porta 80
EXPOSE 80

# Inicia o Nginx
CMD ["nginx", "-g", "daemon off;"]
