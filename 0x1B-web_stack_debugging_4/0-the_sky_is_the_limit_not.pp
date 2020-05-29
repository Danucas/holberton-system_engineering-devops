# ulimit

service {'nginx'
  ensure => 'running',
  enable => true,
}

file {
  ensure => present,
} -> exec {
  notify  => Service['nginx'],
  path    => '/bin/',
  command => "sed -i 's/15/4096/g' /etc/default/nginx"
}