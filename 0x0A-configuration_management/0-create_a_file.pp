# Creates a holberton file in /tmp directory with permissions 
file{'/tmp/holberton':
    path    =>  '/tmp/holberton',
    content =>  'I love Puppet',
    mode    =>  '0744',
    group   =>  'www-data',
    owner   =>  'www-data'
}
