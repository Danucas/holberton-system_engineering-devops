# Puppet manifest to kill the 'killmenow process'
exec{'stop killmenow':
    command =>   'pkill -15 killmenow',
    path    =>   [ '/bin/bash', '/usr/bin' ]
}