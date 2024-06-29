# Define class for SSH client configuration
class ssh_config {

  # Ensure SSH client configuration file exists
  file { '/etc/ssh/ssh_config':
    ensure => file,
  }

  # Manage SSH client configuration options
  file_line { 'ssh_private_key':
    path    => '/etc/ssh/ssh_config',
    line    => '    IdentityFile ~/.ssh/school',
    ensure  => present,
    require => File['/etc/ssh/ssh_config'],
  }

  file_line { 'ssh_no_password_authentication':
    path    => '/etc/ssh/ssh_config',
    line    => '    PasswordAuthentication no',
    ensure  => present,
    require => File['/etc/ssh/ssh_config'],
  }
}

# Apply the ssh_config class
include ssh_config

