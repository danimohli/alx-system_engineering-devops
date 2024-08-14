# This Puppet manifest fixes file permissions for Apache's document root

file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  recurse => true,
}

service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html'],
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
