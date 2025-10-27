#!/bin/bash
set -e
envsubst < /var/www/templates/index.html > /usr/local/apache2/htdocs/index.html

exec httpd-foreground
