exec { 'wordpress_fixing':
  'command': 'sed /s/phpp/php/g /var/www/html/wp-settings.php'
  'path': '/usr/local/bin/:/bin',
}
