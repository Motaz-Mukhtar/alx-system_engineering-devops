# Fixing Error that exists in php file

exec { 'wordpress_fixing':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin/local/:/bin',
}
