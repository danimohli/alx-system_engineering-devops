# Increase Nginx's file descriptor limit to handle more requests

exec { 'modify_nginx_file_descriptor_limit':
  command => command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  onlyif  => 'grep -q "s/15/10000/" /etc/nginx/nginx.conf',
}
