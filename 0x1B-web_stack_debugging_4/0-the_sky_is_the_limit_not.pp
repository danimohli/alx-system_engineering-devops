# Increase Nginx's file descriptor limit to handle more requests

exec { 'modify_nginx_file_descriptor_limit':
  command => 'sed -i "s/^#*worker_rlimit_nofile.*/worker_rlimit_nofile 10000;/" /etc/nginx/nginx.conf && systemctl restart nginx',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
  onlyif  => 'grep -q "^worker_rlimit_nofile 10000;" /etc/nginx/nginx.conf',
}
