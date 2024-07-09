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

# Configure the custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Use a template for the Nginx configuration
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
