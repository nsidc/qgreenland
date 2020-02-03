# Load modules and classes
lookup('classes', {merge => unique}).include

file {'qgreenland.sh':
  ensure => file,
  path   => '/etc/profile.d/qgreenland.sh',
  source => '/vagrant/puppet/files/qgreenland.sh',
}

exec {'install unzip':
  command   => '/usr/bin/apt-get install unzip',
  logoutput => true,
}

exec {'install docker':
  command   => '/vagrant/puppet/scripts/install-docker.sh',
  logoutput => true,
}

# 100GiB network storage
nsidc_nfs::sharemount { '/share/appdata/qgreenland':
  options => 'rw',
  project => 'appdata',
  share   => 'qgreenland',
}

exec {'start luigi':
  command   => '/usr/local/bin/docker-compose up -d',
  cwd       => '/vagrant/luigi',
  timeout   => 600,
  logoutput => true,
  require   => [
    Exec['install docker'],
    Nsidc_nfs::Sharemount['/share/appdata/qgreenland'],
  ],
}

if $::environment == 'dev' {
	exec {'create conda env':
    command => '/opt/miniconda/bin/conda env create',
    cwd     => '/vagrant',
    user    => vagrant,
    require => Nsidc_miniconda::Install['/opt/miniconda'],
  }
}

