# Fixing Error at default nginx_config file

exec {'fix_nginx_config_file':
  command => 'sed -i s/\'$uri\'/\'http:\/\/localhost\/index.html\'/g /etc/nginx/sites-available/default',
  path    => 'usr/bin/local/:/bin',
}

exec {'restart_nginx_server':
  command => 'nginx restart',
  path    => '/etc/init.d',
}
