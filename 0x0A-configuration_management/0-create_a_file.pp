# Create a fil in /tmp

file { 'school':
  path    => '/tmp/school',
  mode    => '0477',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
