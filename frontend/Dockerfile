FROM httpd:2.4

RUN mv /usr/local/apache2/conf/httpd.conf /usr/local/apache2/conf/original-httpd.conf

# Copy custom Apache config to enable CORS
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

# Copy your static site content
COPY ./index.html /var/www/templates/

# Copy entrypoint script
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

# Ensure directory writable by arbitrary UID/group at runtime
RUN chown -R 1001:0 /usr/local/apache2 && \
    chmod -R g+rwX /usr/local/apache2 && \
    chmod a+x /usr/local/bin/entrypoint.sh && \
    apt-get update && apt-get install -y gettext-base && rm -rf /var/lib/apt/lists/*

# Switch to non-root (arbitrary UID allowed on OpenShift)
USER 1001

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
