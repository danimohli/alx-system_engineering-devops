# This Puppet manifest installs Flask version 2.1.0 using pip3

exec {'pip3 install flask':
  require => Exec['python-installed'],
  command => '/usr/bin/pip3 install flask==2.1.0'
}

exec {'python-installed':
  command => '/usr/bin/which python3'
}
