# Puppet manifest to install and configure Nginx

# Ensure the nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Create the Hello World page
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

# Create the 404 error page
file { '/var/www/html/404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

# Create the Nginx site configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => @("EOF"),
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
| EOF
  notify  => Service['nginx'],
}
