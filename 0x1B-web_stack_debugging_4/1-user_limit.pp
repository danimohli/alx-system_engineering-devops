# Update OS configuration to ensure the 'holberton' user can log in and open files without errors

exec { 'update_os_security_config':
  command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
  path    => '/usr/bin:/bin:/usr/sbin',
}
