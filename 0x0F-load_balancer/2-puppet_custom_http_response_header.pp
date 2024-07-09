# Puppet manifest to install Nginx and configure a custom HTTP header response

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => File['/etc/nginx/sites-available/default'],
}

# Get the hostname
$hostname = inline_template('<%= @hostname %>')

# Configure the custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => epp('
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;
    root /var/www/html;

    # Add the custom HTTP header
    add_header X-Served-By <%= $hostname %>;

    index index.html index.htm index.nginx-debian.html;

    location / {
        try_files $uri $uri/ =404;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        internal;
    }
}
  '),
  require => Package['nginx'],
}

# Ensure the configuration is linked in sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure  => link,
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service to apply the configuration
exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
