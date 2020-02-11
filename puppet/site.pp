# Load modules and classes
lookup('classes', {merge => unique}).include

file {'envvars.sh':
  ensure  => file,
  content => vault_template('/vagrant/puppet/templates/qgreenland.erb'),
  path    => '/etc/profile.d/envvars.sh'
}

exec {'install utils':
  command   => '/usr/bin/apt-get install -y unzip x11-xserver-utils libgl1-mesa-glx',
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
  command   => "/bin/bash -lc '/usr/local/bin/docker-compose up -d'",
  cwd       => '/vagrant/luigi',
  timeout   => 600,
  logoutput => true,
  require   => [
    Exec['install docker'],
    File['envvars.sh'],
    Nsidc_nfs::Sharemount['/share/appdata/qgreenland'],
  ],
}

if $::environment == 'dev' {
	exec {'create conda env':
    command => '/opt/miniconda/bin/conda env create',
    cwd     => '/vagrant',
    timeout => 600,
    user    => vagrant,
    require => Nsidc_miniconda::Install['/opt/miniconda'],
  }
}
