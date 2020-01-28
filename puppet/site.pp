# Load modules and classes
lookup('classes', {merge => unique}).include

exec {'install unzip':
  command   => '/usr/bin/apt-get install unzip',
  logoutput => true,
}

exec {'install docker':
  command   => '/vagrant/puppet/scripts/install-docker.sh',
  logoutput => true,
}

# Mount 100GiB NFS storage
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
