# Puppet manifest to configure http response on nginx

exec{'update':
    command => 'apt-get -y update',
    path    => ['/usr/bin'],
}

package{'nginx':
    ensure  =>  'installed',
    require =>  Exec['update'],
}

file_line {'redirect_me':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'location /redirect_me {return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;}',
    require => Package['nginx'],

}

file_line {'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'add_header X-Served-By "$(hostname)";',
    require => Package['nginx'],
}

file {'/var/www/html/index.html':
    content => 'Holberton School for the win!',
    require => Package['nginx']
}

service {'nginx':
    ensure  => running,
    require => Package['nginx'],
}