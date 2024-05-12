#!/bin/bash

if [ "${HTTPS_ENABLED}" = "true" ]; then
    # set the HTTPS_CONFIG environment variable to the content of the https.conf.template
    export HTTPS_CONFIG=$(envsubst < /etc/nginx/https.conf.template)

    # Substitute the HTTPS_CONFIG in the default.conf.template with content from https.conf.template
    envsubst '${HTTPS_CONFIG}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf
fi

envsubst < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf
envsubst < /etc/nginx/proxy.conf.template > /etc/nginx/proxy.conf
envsubst < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Start Nginx using the default entrypoint
exec nginx -g 'daemon off;'