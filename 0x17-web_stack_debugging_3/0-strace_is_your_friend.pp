# Restart Mysql service and copy class-wp-locale.php to class-wp-locale.phpp
# Not a clean fix
exec {'start-mysql':
  command  => '/etc/init.d/mysql restart',
  provider => shell,
}
exec {'fix-wordpress':
  command  => 'sudo cp /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  provider => shell,
}
