# This Puppet manifest installs Flask version 2.1.0 and a compatible version of Werkzeug using pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.0.3',
  unless  => '/usr/bin/pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}
