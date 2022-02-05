FROM httpd

COPY ./docker/web/public_html /usr/local/apache2/htdocs
COPY ./docker/web /web
RUN cp /web/httpd.conf /usr/local/apache2/conf/httpd.conf