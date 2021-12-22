# Troubleshooting

## "Too many open files" on Linux

Your system may have multiple ways of limiting open files in different
contexts. To check your limits:

```
ulimit -Sn  # soft limit
ulimit -Hn  # hard limit
```

Edit the `/etc/security/limits.conf` to add or update rules that apply to your
user. If there are no rules, you can try adding:

```
* soft nofile 20480
* hard nofile 1048576
```

If your system uses `systemd`, also edit the `/etc/systemd/system.conf` and
`/etc/systemd/user.conf` files to ensure the following variable is set to a
large value in *both* files:

```
DefaultLimitNOFILE=20480
```

After applying these changes, you may find that new terminal windows are not
affected. Reboot your computer to make the changes permanent.


## I see `ERROR: Too many connections: max 64` in my terminal

We don't think this is an issue. This started happening when we switched to
GeoPackages for vector data, but we've observed no negative impact of this
error message.


## QGIS won't start on OSX Catalina

QGIS is currently not "notarized" for Mac OSX. If you receive `The developer of
this app needs to update it to work with this version of macOS. Contact the
developer for more information.`, then, in your OSX menus, try:

- "Security and Privacy"
- "Allow apps downloaded from..."
- "App Store and identified developers"
- Locate QGIS here and select "Open anyway"
