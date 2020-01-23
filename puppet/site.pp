# Load modules and classes
lookup('classes', {merge => unique}).include

exec {'install docker':
  command   => "/vagrant/puppet/scripts/install-docker.sh",
  logoutput =>  true,
}

# Mount 100GiB NFS storage
nsidc_nfs::sharemount { '/share/appdata/qgreenland':
  options => 'rw',
  project => 'appdata',
  share   => "qgreenland",
}
