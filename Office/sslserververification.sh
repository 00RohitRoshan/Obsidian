docker run --name nginx-file-server -p 8080:80 \
  -v $(pwd)/:/usr/share/nginx/html/.well-known/pki-validation/:ro \
  -v $(pwd)/default.conf:/etc/nginx/conf.d/default.conf:ro \
  -d nginx
