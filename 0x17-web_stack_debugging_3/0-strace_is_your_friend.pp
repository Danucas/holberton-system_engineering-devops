# Restart Mysql service and copy class-wp-locale.php to class-wp-locale.phpp
# Not a clean fix
exec {'fix-wordpress':
  command  => 'service mysql restart && cp /var/www/html/wp-include/class-wp-locale.php /var/www/html/wp-include/class-wp-locale.phpp',
  provider => shell
}