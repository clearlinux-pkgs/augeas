#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xA2357646FC6E8A22 (lutter@apache.org)
#
Name     : augeas
Version  : 1.11.0
Release  : 19
URL      : http://download.augeas.net/augeas-1.11.0.tar.gz
Source0  : http://download.augeas.net/augeas-1.11.0.tar.gz
Source99 : http://download.augeas.net/augeas-1.11.0.tar.gz.sig
Summary  : A library for changing configuration files
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: augeas-bin = %{version}-%{release}
Requires: augeas-data = %{version}-%{release}
Requires: augeas-lib = %{version}-%{release}
Requires: augeas-license = %{version}-%{release}
Requires: augeas-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : flex
BuildRequires : glibc-locale
BuildRequires : libc6-locale
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : readline-dev

%description
A library for programmatically editing configuration files. Augeas parses
configuration files into a tree structure, which it exposes through its
public API. Changes made through the API are written back to the initially
read files.

The transformation works very hard to preserve comments and formatting
details. It is controlled by ``lens'' definitions that describe the file
format and the transformation into a tree.

%package bin
Summary: bin components for the augeas package.
Group: Binaries
Requires: augeas-data = %{version}-%{release}
Requires: augeas-license = %{version}-%{release}
Requires: augeas-man = %{version}-%{release}

%description bin
bin components for the augeas package.


%package data
Summary: data components for the augeas package.
Group: Data

%description data
data components for the augeas package.


%package dev
Summary: dev components for the augeas package.
Group: Development
Requires: augeas-lib = %{version}-%{release}
Requires: augeas-bin = %{version}-%{release}
Requires: augeas-data = %{version}-%{release}
Provides: augeas-devel = %{version}-%{release}

%description dev
dev components for the augeas package.


%package lib
Summary: lib components for the augeas package.
Group: Libraries
Requires: augeas-data = %{version}-%{release}
Requires: augeas-license = %{version}-%{release}

%description lib
lib components for the augeas package.


%package license
Summary: license components for the augeas package.
Group: Default

%description license
license components for the augeas package.


%package man
Summary: man components for the augeas package.
Group: Default

%description man
man components for the augeas package.


%prep
%setup -q -n augeas-1.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542067908
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542067908
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/augeas
cp COPYING %{buildroot}/usr/share/package-licenses/augeas/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/augmatch
/usr/bin/augparse
/usr/bin/augtool
/usr/bin/fadot

%files data
%defattr(-,root,root,-)
/usr/share/augeas/lenses/dist/access.aug
/usr/share/augeas/lenses/dist/activemq_conf.aug
/usr/share/augeas/lenses/dist/activemq_xml.aug
/usr/share/augeas/lenses/dist/afs_cellalias.aug
/usr/share/augeas/lenses/dist/aliases.aug
/usr/share/augeas/lenses/dist/anacron.aug
/usr/share/augeas/lenses/dist/approx.aug
/usr/share/augeas/lenses/dist/apt_update_manager.aug
/usr/share/augeas/lenses/dist/aptcacherngsecurity.aug
/usr/share/augeas/lenses/dist/aptconf.aug
/usr/share/augeas/lenses/dist/aptpreferences.aug
/usr/share/augeas/lenses/dist/aptsources.aug
/usr/share/augeas/lenses/dist/authorized_keys.aug
/usr/share/augeas/lenses/dist/automaster.aug
/usr/share/augeas/lenses/dist/automounter.aug
/usr/share/augeas/lenses/dist/avahi.aug
/usr/share/augeas/lenses/dist/backuppchosts.aug
/usr/share/augeas/lenses/dist/bbhosts.aug
/usr/share/augeas/lenses/dist/bootconf.aug
/usr/share/augeas/lenses/dist/build.aug
/usr/share/augeas/lenses/dist/cachefilesd.aug
/usr/share/augeas/lenses/dist/carbon.aug
/usr/share/augeas/lenses/dist/ceph.aug
/usr/share/augeas/lenses/dist/cgconfig.aug
/usr/share/augeas/lenses/dist/cgrules.aug
/usr/share/augeas/lenses/dist/channels.aug
/usr/share/augeas/lenses/dist/chrony.aug
/usr/share/augeas/lenses/dist/clamav.aug
/usr/share/augeas/lenses/dist/cobblermodules.aug
/usr/share/augeas/lenses/dist/cobblersettings.aug
/usr/share/augeas/lenses/dist/collectd.aug
/usr/share/augeas/lenses/dist/cpanel.aug
/usr/share/augeas/lenses/dist/cron.aug
/usr/share/augeas/lenses/dist/cron_user.aug
/usr/share/augeas/lenses/dist/crypttab.aug
/usr/share/augeas/lenses/dist/csv.aug
/usr/share/augeas/lenses/dist/cups.aug
/usr/share/augeas/lenses/dist/cyrus_imapd.aug
/usr/share/augeas/lenses/dist/darkice.aug
/usr/share/augeas/lenses/dist/debctrl.aug
/usr/share/augeas/lenses/dist/desktop.aug
/usr/share/augeas/lenses/dist/device_map.aug
/usr/share/augeas/lenses/dist/dhclient.aug
/usr/share/augeas/lenses/dist/dhcpd.aug
/usr/share/augeas/lenses/dist/dns_zone.aug
/usr/share/augeas/lenses/dist/dnsmasq.aug
/usr/share/augeas/lenses/dist/dovecot.aug
/usr/share/augeas/lenses/dist/dpkg.aug
/usr/share/augeas/lenses/dist/dput.aug
/usr/share/augeas/lenses/dist/erlang.aug
/usr/share/augeas/lenses/dist/ethers.aug
/usr/share/augeas/lenses/dist/exports.aug
/usr/share/augeas/lenses/dist/fai_diskconfig.aug
/usr/share/augeas/lenses/dist/fonts.aug
/usr/share/augeas/lenses/dist/fstab.aug
/usr/share/augeas/lenses/dist/fuse.aug
/usr/share/augeas/lenses/dist/gdm.aug
/usr/share/augeas/lenses/dist/getcap.aug
/usr/share/augeas/lenses/dist/group.aug
/usr/share/augeas/lenses/dist/grub.aug
/usr/share/augeas/lenses/dist/grubenv.aug
/usr/share/augeas/lenses/dist/gshadow.aug
/usr/share/augeas/lenses/dist/gtkbookmarks.aug
/usr/share/augeas/lenses/dist/host_conf.aug
/usr/share/augeas/lenses/dist/hostname.aug
/usr/share/augeas/lenses/dist/hosts.aug
/usr/share/augeas/lenses/dist/hosts_access.aug
/usr/share/augeas/lenses/dist/htpasswd.aug
/usr/share/augeas/lenses/dist/httpd.aug
/usr/share/augeas/lenses/dist/inetd.aug
/usr/share/augeas/lenses/dist/inifile.aug
/usr/share/augeas/lenses/dist/inittab.aug
/usr/share/augeas/lenses/dist/inputrc.aug
/usr/share/augeas/lenses/dist/interfaces.aug
/usr/share/augeas/lenses/dist/iproute2.aug
/usr/share/augeas/lenses/dist/iptables.aug
/usr/share/augeas/lenses/dist/iscsid.aug
/usr/share/augeas/lenses/dist/jaas.aug
/usr/share/augeas/lenses/dist/jettyrealm.aug
/usr/share/augeas/lenses/dist/jmxaccess.aug
/usr/share/augeas/lenses/dist/jmxpassword.aug
/usr/share/augeas/lenses/dist/json.aug
/usr/share/augeas/lenses/dist/kdump.aug
/usr/share/augeas/lenses/dist/keepalived.aug
/usr/share/augeas/lenses/dist/known_hosts.aug
/usr/share/augeas/lenses/dist/koji.aug
/usr/share/augeas/lenses/dist/krb5.aug
/usr/share/augeas/lenses/dist/ldif.aug
/usr/share/augeas/lenses/dist/ldso.aug
/usr/share/augeas/lenses/dist/lightdm.aug
/usr/share/augeas/lenses/dist/limits.aug
/usr/share/augeas/lenses/dist/login_defs.aug
/usr/share/augeas/lenses/dist/logrotate.aug
/usr/share/augeas/lenses/dist/logwatch.aug
/usr/share/augeas/lenses/dist/lokkit.aug
/usr/share/augeas/lenses/dist/lvm.aug
/usr/share/augeas/lenses/dist/mailscanner.aug
/usr/share/augeas/lenses/dist/mailscanner_rules.aug
/usr/share/augeas/lenses/dist/masterpasswd.aug
/usr/share/augeas/lenses/dist/mcollective.aug
/usr/share/augeas/lenses/dist/mdadm_conf.aug
/usr/share/augeas/lenses/dist/memcached.aug
/usr/share/augeas/lenses/dist/mke2fs.aug
/usr/share/augeas/lenses/dist/modprobe.aug
/usr/share/augeas/lenses/dist/modules.aug
/usr/share/augeas/lenses/dist/modules_conf.aug
/usr/share/augeas/lenses/dist/mongodbserver.aug
/usr/share/augeas/lenses/dist/monit.aug
/usr/share/augeas/lenses/dist/multipath.aug
/usr/share/augeas/lenses/dist/mysql.aug
/usr/share/augeas/lenses/dist/nagioscfg.aug
/usr/share/augeas/lenses/dist/nagiosobjects.aug
/usr/share/augeas/lenses/dist/netmasks.aug
/usr/share/augeas/lenses/dist/networkmanager.aug
/usr/share/augeas/lenses/dist/networks.aug
/usr/share/augeas/lenses/dist/nginx.aug
/usr/share/augeas/lenses/dist/nrpe.aug
/usr/share/augeas/lenses/dist/nslcd.aug
/usr/share/augeas/lenses/dist/nsswitch.aug
/usr/share/augeas/lenses/dist/ntp.aug
/usr/share/augeas/lenses/dist/ntpd.aug
/usr/share/augeas/lenses/dist/odbc.aug
/usr/share/augeas/lenses/dist/opendkim.aug
/usr/share/augeas/lenses/dist/openshift_config.aug
/usr/share/augeas/lenses/dist/openshift_http.aug
/usr/share/augeas/lenses/dist/openshift_quickstarts.aug
/usr/share/augeas/lenses/dist/openvpn.aug
/usr/share/augeas/lenses/dist/oz.aug
/usr/share/augeas/lenses/dist/pagekite.aug
/usr/share/augeas/lenses/dist/pam.aug
/usr/share/augeas/lenses/dist/pamconf.aug
/usr/share/augeas/lenses/dist/passwd.aug
/usr/share/augeas/lenses/dist/pbuilder.aug
/usr/share/augeas/lenses/dist/pg_hba.aug
/usr/share/augeas/lenses/dist/pgbouncer.aug
/usr/share/augeas/lenses/dist/php.aug
/usr/share/augeas/lenses/dist/phpvars.aug
/usr/share/augeas/lenses/dist/postfix_access.aug
/usr/share/augeas/lenses/dist/postfix_main.aug
/usr/share/augeas/lenses/dist/postfix_master.aug
/usr/share/augeas/lenses/dist/postfix_passwordmap.aug
/usr/share/augeas/lenses/dist/postfix_sasl_smtpd.aug
/usr/share/augeas/lenses/dist/postfix_transport.aug
/usr/share/augeas/lenses/dist/postfix_virtual.aug
/usr/share/augeas/lenses/dist/postgresql.aug
/usr/share/augeas/lenses/dist/properties.aug
/usr/share/augeas/lenses/dist/protocols.aug
/usr/share/augeas/lenses/dist/puppet.aug
/usr/share/augeas/lenses/dist/puppet_auth.aug
/usr/share/augeas/lenses/dist/puppetfile.aug
/usr/share/augeas/lenses/dist/puppetfileserver.aug
/usr/share/augeas/lenses/dist/pylonspaste.aug
/usr/share/augeas/lenses/dist/pythonpaste.aug
/usr/share/augeas/lenses/dist/qpid.aug
/usr/share/augeas/lenses/dist/quote.aug
/usr/share/augeas/lenses/dist/rabbitmq.aug
/usr/share/augeas/lenses/dist/radicale.aug
/usr/share/augeas/lenses/dist/rancid.aug
/usr/share/augeas/lenses/dist/redis.aug
/usr/share/augeas/lenses/dist/reprepro_uploaders.aug
/usr/share/augeas/lenses/dist/resolv.aug
/usr/share/augeas/lenses/dist/rhsm.aug
/usr/share/augeas/lenses/dist/rmt.aug
/usr/share/augeas/lenses/dist/rsyncd.aug
/usr/share/augeas/lenses/dist/rsyslog.aug
/usr/share/augeas/lenses/dist/rtadvd.aug
/usr/share/augeas/lenses/dist/rx.aug
/usr/share/augeas/lenses/dist/samba.aug
/usr/share/augeas/lenses/dist/schroot.aug
/usr/share/augeas/lenses/dist/securetty.aug
/usr/share/augeas/lenses/dist/sep.aug
/usr/share/augeas/lenses/dist/services.aug
/usr/share/augeas/lenses/dist/shadow.aug
/usr/share/augeas/lenses/dist/shells.aug
/usr/share/augeas/lenses/dist/shellvars.aug
/usr/share/augeas/lenses/dist/shellvars_list.aug
/usr/share/augeas/lenses/dist/simplelines.aug
/usr/share/augeas/lenses/dist/simplevars.aug
/usr/share/augeas/lenses/dist/sip_conf.aug
/usr/share/augeas/lenses/dist/slapd.aug
/usr/share/augeas/lenses/dist/smbusers.aug
/usr/share/augeas/lenses/dist/solaris_system.aug
/usr/share/augeas/lenses/dist/soma.aug
/usr/share/augeas/lenses/dist/spacevars.aug
/usr/share/augeas/lenses/dist/splunk.aug
/usr/share/augeas/lenses/dist/squid.aug
/usr/share/augeas/lenses/dist/ssh.aug
/usr/share/augeas/lenses/dist/sshd.aug
/usr/share/augeas/lenses/dist/sssd.aug
/usr/share/augeas/lenses/dist/star.aug
/usr/share/augeas/lenses/dist/strongswan.aug
/usr/share/augeas/lenses/dist/stunnel.aug
/usr/share/augeas/lenses/dist/subversion.aug
/usr/share/augeas/lenses/dist/sudoers.aug
/usr/share/augeas/lenses/dist/sysconfig.aug
/usr/share/augeas/lenses/dist/sysconfig_route.aug
/usr/share/augeas/lenses/dist/sysctl.aug
/usr/share/augeas/lenses/dist/syslog.aug
/usr/share/augeas/lenses/dist/systemd.aug
/usr/share/augeas/lenses/dist/termcap.aug
/usr/share/augeas/lenses/dist/tests/test_access.aug
/usr/share/augeas/lenses/dist/tests/test_activemq_conf.aug
/usr/share/augeas/lenses/dist/tests/test_activemq_xml.aug
/usr/share/augeas/lenses/dist/tests/test_afs_cellalias.aug
/usr/share/augeas/lenses/dist/tests/test_aliases.aug
/usr/share/augeas/lenses/dist/tests/test_anacron.aug
/usr/share/augeas/lenses/dist/tests/test_approx.aug
/usr/share/augeas/lenses/dist/tests/test_apt_update_manager.aug
/usr/share/augeas/lenses/dist/tests/test_aptcacherngsecurity.aug
/usr/share/augeas/lenses/dist/tests/test_aptconf.aug
/usr/share/augeas/lenses/dist/tests/test_aptpreferences.aug
/usr/share/augeas/lenses/dist/tests/test_aptsources.aug
/usr/share/augeas/lenses/dist/tests/test_authorized_keys.aug
/usr/share/augeas/lenses/dist/tests/test_automaster.aug
/usr/share/augeas/lenses/dist/tests/test_automounter.aug
/usr/share/augeas/lenses/dist/tests/test_avahi.aug
/usr/share/augeas/lenses/dist/tests/test_backuppchosts.aug
/usr/share/augeas/lenses/dist/tests/test_bbhosts.aug
/usr/share/augeas/lenses/dist/tests/test_bootconf.aug
/usr/share/augeas/lenses/dist/tests/test_build.aug
/usr/share/augeas/lenses/dist/tests/test_cachefilesd.aug
/usr/share/augeas/lenses/dist/tests/test_carbon.aug
/usr/share/augeas/lenses/dist/tests/test_ceph.aug
/usr/share/augeas/lenses/dist/tests/test_cgconfig.aug
/usr/share/augeas/lenses/dist/tests/test_cgrules.aug
/usr/share/augeas/lenses/dist/tests/test_channels.aug
/usr/share/augeas/lenses/dist/tests/test_chrony.aug
/usr/share/augeas/lenses/dist/tests/test_clamav.aug
/usr/share/augeas/lenses/dist/tests/test_cobblermodules.aug
/usr/share/augeas/lenses/dist/tests/test_cobblersettings.aug
/usr/share/augeas/lenses/dist/tests/test_collectd.aug
/usr/share/augeas/lenses/dist/tests/test_cpanel.aug
/usr/share/augeas/lenses/dist/tests/test_cron.aug
/usr/share/augeas/lenses/dist/tests/test_cron_user.aug
/usr/share/augeas/lenses/dist/tests/test_crypttab.aug
/usr/share/augeas/lenses/dist/tests/test_csv.aug
/usr/share/augeas/lenses/dist/tests/test_cups.aug
/usr/share/augeas/lenses/dist/tests/test_cyrus_imapd.aug
/usr/share/augeas/lenses/dist/tests/test_darkice.aug
/usr/share/augeas/lenses/dist/tests/test_debctrl.aug
/usr/share/augeas/lenses/dist/tests/test_desktop.aug
/usr/share/augeas/lenses/dist/tests/test_device_map.aug
/usr/share/augeas/lenses/dist/tests/test_dhclient.aug
/usr/share/augeas/lenses/dist/tests/test_dhcpd.aug
/usr/share/augeas/lenses/dist/tests/test_dns_zone.aug
/usr/share/augeas/lenses/dist/tests/test_dnsmasq.aug
/usr/share/augeas/lenses/dist/tests/test_dovecot.aug
/usr/share/augeas/lenses/dist/tests/test_dpkg.aug
/usr/share/augeas/lenses/dist/tests/test_dput.aug
/usr/share/augeas/lenses/dist/tests/test_erlang.aug
/usr/share/augeas/lenses/dist/tests/test_ethers.aug
/usr/share/augeas/lenses/dist/tests/test_exports.aug
/usr/share/augeas/lenses/dist/tests/test_fai_diskconfig.aug
/usr/share/augeas/lenses/dist/tests/test_fonts.aug
/usr/share/augeas/lenses/dist/tests/test_fstab.aug
/usr/share/augeas/lenses/dist/tests/test_fuse.aug
/usr/share/augeas/lenses/dist/tests/test_gdm.aug
/usr/share/augeas/lenses/dist/tests/test_getcap.aug
/usr/share/augeas/lenses/dist/tests/test_group.aug
/usr/share/augeas/lenses/dist/tests/test_grub.aug
/usr/share/augeas/lenses/dist/tests/test_grubenv.aug
/usr/share/augeas/lenses/dist/tests/test_gshadow.aug
/usr/share/augeas/lenses/dist/tests/test_gtkbookmarks.aug
/usr/share/augeas/lenses/dist/tests/test_host_conf.aug
/usr/share/augeas/lenses/dist/tests/test_hostname.aug
/usr/share/augeas/lenses/dist/tests/test_hosts.aug
/usr/share/augeas/lenses/dist/tests/test_hosts_access.aug
/usr/share/augeas/lenses/dist/tests/test_htpasswd.aug
/usr/share/augeas/lenses/dist/tests/test_httpd.aug
/usr/share/augeas/lenses/dist/tests/test_inetd.aug
/usr/share/augeas/lenses/dist/tests/test_inifile.aug
/usr/share/augeas/lenses/dist/tests/test_inittab.aug
/usr/share/augeas/lenses/dist/tests/test_inputrc.aug
/usr/share/augeas/lenses/dist/tests/test_interfaces.aug
/usr/share/augeas/lenses/dist/tests/test_iproute2.aug
/usr/share/augeas/lenses/dist/tests/test_iptables.aug
/usr/share/augeas/lenses/dist/tests/test_iscsid.aug
/usr/share/augeas/lenses/dist/tests/test_jaas.aug
/usr/share/augeas/lenses/dist/tests/test_jettyrealm.aug
/usr/share/augeas/lenses/dist/tests/test_jmxaccess.aug
/usr/share/augeas/lenses/dist/tests/test_jmxpassword.aug
/usr/share/augeas/lenses/dist/tests/test_json.aug
/usr/share/augeas/lenses/dist/tests/test_kdump.aug
/usr/share/augeas/lenses/dist/tests/test_keepalived.aug
/usr/share/augeas/lenses/dist/tests/test_known_hosts.aug
/usr/share/augeas/lenses/dist/tests/test_koji.aug
/usr/share/augeas/lenses/dist/tests/test_krb5.aug
/usr/share/augeas/lenses/dist/tests/test_ldap.aug
/usr/share/augeas/lenses/dist/tests/test_ldif.aug
/usr/share/augeas/lenses/dist/tests/test_ldso.aug
/usr/share/augeas/lenses/dist/tests/test_lightdm.aug
/usr/share/augeas/lenses/dist/tests/test_limits.aug
/usr/share/augeas/lenses/dist/tests/test_login_defs.aug
/usr/share/augeas/lenses/dist/tests/test_logrotate.aug
/usr/share/augeas/lenses/dist/tests/test_logwatch.aug
/usr/share/augeas/lenses/dist/tests/test_lokkit.aug
/usr/share/augeas/lenses/dist/tests/test_lvm.aug
/usr/share/augeas/lenses/dist/tests/test_mailscanner.aug
/usr/share/augeas/lenses/dist/tests/test_mailscanner_rules.aug
/usr/share/augeas/lenses/dist/tests/test_masterpasswd.aug
/usr/share/augeas/lenses/dist/tests/test_mcollective.aug
/usr/share/augeas/lenses/dist/tests/test_mdadm_conf.aug
/usr/share/augeas/lenses/dist/tests/test_memcached.aug
/usr/share/augeas/lenses/dist/tests/test_mke2fs.aug
/usr/share/augeas/lenses/dist/tests/test_modprobe.aug
/usr/share/augeas/lenses/dist/tests/test_modules.aug
/usr/share/augeas/lenses/dist/tests/test_modules_conf.aug
/usr/share/augeas/lenses/dist/tests/test_mongodbserver.aug
/usr/share/augeas/lenses/dist/tests/test_monit.aug
/usr/share/augeas/lenses/dist/tests/test_multipath.aug
/usr/share/augeas/lenses/dist/tests/test_mysql.aug
/usr/share/augeas/lenses/dist/tests/test_nagioscfg.aug
/usr/share/augeas/lenses/dist/tests/test_nagiosobjects.aug
/usr/share/augeas/lenses/dist/tests/test_netmasks.aug
/usr/share/augeas/lenses/dist/tests/test_networkmanager.aug
/usr/share/augeas/lenses/dist/tests/test_networks.aug
/usr/share/augeas/lenses/dist/tests/test_nginx.aug
/usr/share/augeas/lenses/dist/tests/test_nrpe.aug
/usr/share/augeas/lenses/dist/tests/test_nslcd.aug
/usr/share/augeas/lenses/dist/tests/test_nsswitch.aug
/usr/share/augeas/lenses/dist/tests/test_ntp.aug
/usr/share/augeas/lenses/dist/tests/test_ntpd.aug
/usr/share/augeas/lenses/dist/tests/test_odbc.aug
/usr/share/augeas/lenses/dist/tests/test_opendkim.aug
/usr/share/augeas/lenses/dist/tests/test_openshift_config.aug
/usr/share/augeas/lenses/dist/tests/test_openshift_http.aug
/usr/share/augeas/lenses/dist/tests/test_openshift_quickstarts.aug
/usr/share/augeas/lenses/dist/tests/test_openvpn.aug
/usr/share/augeas/lenses/dist/tests/test_oz.aug
/usr/share/augeas/lenses/dist/tests/test_pagekite.aug
/usr/share/augeas/lenses/dist/tests/test_pam.aug
/usr/share/augeas/lenses/dist/tests/test_pamconf.aug
/usr/share/augeas/lenses/dist/tests/test_passwd.aug
/usr/share/augeas/lenses/dist/tests/test_pbuilder.aug
/usr/share/augeas/lenses/dist/tests/test_pg_hba.aug
/usr/share/augeas/lenses/dist/tests/test_pgbouncer.aug
/usr/share/augeas/lenses/dist/tests/test_php.aug
/usr/share/augeas/lenses/dist/tests/test_phpvars.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_access.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_main.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_master.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_passwordmap.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_sasl_smtpd.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_transport.aug
/usr/share/augeas/lenses/dist/tests/test_postfix_virtual.aug
/usr/share/augeas/lenses/dist/tests/test_postgresql.aug
/usr/share/augeas/lenses/dist/tests/test_properties.aug
/usr/share/augeas/lenses/dist/tests/test_protocols.aug
/usr/share/augeas/lenses/dist/tests/test_puppet.aug
/usr/share/augeas/lenses/dist/tests/test_puppet_auth.aug
/usr/share/augeas/lenses/dist/tests/test_puppetfile.aug
/usr/share/augeas/lenses/dist/tests/test_puppetfileserver.aug
/usr/share/augeas/lenses/dist/tests/test_pylonspaste.aug
/usr/share/augeas/lenses/dist/tests/test_pythonpaste.aug
/usr/share/augeas/lenses/dist/tests/test_qpid.aug
/usr/share/augeas/lenses/dist/tests/test_quote.aug
/usr/share/augeas/lenses/dist/tests/test_rabbitmq.aug
/usr/share/augeas/lenses/dist/tests/test_radicale.aug
/usr/share/augeas/lenses/dist/tests/test_rancid.aug
/usr/share/augeas/lenses/dist/tests/test_redis.aug
/usr/share/augeas/lenses/dist/tests/test_reprepro_uploaders.aug
/usr/share/augeas/lenses/dist/tests/test_resolv.aug
/usr/share/augeas/lenses/dist/tests/test_rhsm.aug
/usr/share/augeas/lenses/dist/tests/test_rmt.aug
/usr/share/augeas/lenses/dist/tests/test_rsyncd.aug
/usr/share/augeas/lenses/dist/tests/test_rsyslog.aug
/usr/share/augeas/lenses/dist/tests/test_rtadvd.aug
/usr/share/augeas/lenses/dist/tests/test_rx.aug
/usr/share/augeas/lenses/dist/tests/test_samba.aug
/usr/share/augeas/lenses/dist/tests/test_schroot.aug
/usr/share/augeas/lenses/dist/tests/test_securetty.aug
/usr/share/augeas/lenses/dist/tests/test_services.aug
/usr/share/augeas/lenses/dist/tests/test_shadow.aug
/usr/share/augeas/lenses/dist/tests/test_shells.aug
/usr/share/augeas/lenses/dist/tests/test_shellvars.aug
/usr/share/augeas/lenses/dist/tests/test_shellvars_list.aug
/usr/share/augeas/lenses/dist/tests/test_simplelines.aug
/usr/share/augeas/lenses/dist/tests/test_simplevars.aug
/usr/share/augeas/lenses/dist/tests/test_sip_conf.aug
/usr/share/augeas/lenses/dist/tests/test_slapd.aug
/usr/share/augeas/lenses/dist/tests/test_smbusers.aug
/usr/share/augeas/lenses/dist/tests/test_solaris_system.aug
/usr/share/augeas/lenses/dist/tests/test_soma.aug
/usr/share/augeas/lenses/dist/tests/test_spacevars.aug
/usr/share/augeas/lenses/dist/tests/test_splunk.aug
/usr/share/augeas/lenses/dist/tests/test_squid.aug
/usr/share/augeas/lenses/dist/tests/test_ssh.aug
/usr/share/augeas/lenses/dist/tests/test_sshd.aug
/usr/share/augeas/lenses/dist/tests/test_sssd.aug
/usr/share/augeas/lenses/dist/tests/test_star.aug
/usr/share/augeas/lenses/dist/tests/test_strongswan.aug
/usr/share/augeas/lenses/dist/tests/test_stunnel.aug
/usr/share/augeas/lenses/dist/tests/test_subversion.aug
/usr/share/augeas/lenses/dist/tests/test_sudoers.aug
/usr/share/augeas/lenses/dist/tests/test_sysconfig.aug
/usr/share/augeas/lenses/dist/tests/test_sysconfig_route.aug
/usr/share/augeas/lenses/dist/tests/test_sysctl.aug
/usr/share/augeas/lenses/dist/tests/test_syslog.aug
/usr/share/augeas/lenses/dist/tests/test_systemd.aug
/usr/share/augeas/lenses/dist/tests/test_termcap.aug
/usr/share/augeas/lenses/dist/tests/test_thttpd.aug
/usr/share/augeas/lenses/dist/tests/test_tmpfiles.aug
/usr/share/augeas/lenses/dist/tests/test_trapperkeeper.aug
/usr/share/augeas/lenses/dist/tests/test_tuned.aug
/usr/share/augeas/lenses/dist/tests/test_up2date.aug
/usr/share/augeas/lenses/dist/tests/test_updatedb.aug
/usr/share/augeas/lenses/dist/tests/test_util.aug
/usr/share/augeas/lenses/dist/tests/test_vfstab.aug
/usr/share/augeas/lenses/dist/tests/test_vmware_config.aug
/usr/share/augeas/lenses/dist/tests/test_vsftpd.aug
/usr/share/augeas/lenses/dist/tests/test_webmin.aug
/usr/share/augeas/lenses/dist/tests/test_wine.aug
/usr/share/augeas/lenses/dist/tests/test_xendconfsxp.aug
/usr/share/augeas/lenses/dist/tests/test_xinetd.aug
/usr/share/augeas/lenses/dist/tests/test_xml.aug
/usr/share/augeas/lenses/dist/tests/test_xorg.aug
/usr/share/augeas/lenses/dist/tests/test_xymon.aug
/usr/share/augeas/lenses/dist/tests/test_xymon_alerting.aug
/usr/share/augeas/lenses/dist/tests/test_yaml.aug
/usr/share/augeas/lenses/dist/tests/test_yum.aug
/usr/share/augeas/lenses/dist/thttpd.aug
/usr/share/augeas/lenses/dist/tmpfiles.aug
/usr/share/augeas/lenses/dist/trapperkeeper.aug
/usr/share/augeas/lenses/dist/tuned.aug
/usr/share/augeas/lenses/dist/up2date.aug
/usr/share/augeas/lenses/dist/updatedb.aug
/usr/share/augeas/lenses/dist/util.aug
/usr/share/augeas/lenses/dist/vfstab.aug
/usr/share/augeas/lenses/dist/vmware_config.aug
/usr/share/augeas/lenses/dist/vsftpd.aug
/usr/share/augeas/lenses/dist/webmin.aug
/usr/share/augeas/lenses/dist/wine.aug
/usr/share/augeas/lenses/dist/xendconfsxp.aug
/usr/share/augeas/lenses/dist/xinetd.aug
/usr/share/augeas/lenses/dist/xml.aug
/usr/share/augeas/lenses/dist/xorg.aug
/usr/share/augeas/lenses/dist/xymon.aug
/usr/share/augeas/lenses/dist/xymon_alerting.aug
/usr/share/augeas/lenses/dist/yaml.aug
/usr/share/augeas/lenses/dist/yum.aug
/usr/share/vim/vimfiles/ftdetect/augeas.vim
/usr/share/vim/vimfiles/syntax/augeas.vim

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libaugeas.so
/usr/lib64/libfa.so
/usr/lib64/pkgconfig/augeas.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libaugeas.so.0
/usr/lib64/libaugeas.so.0.24.1
/usr/lib64/libfa.so.1
/usr/lib64/libfa.so.1.5.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/augeas/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/augmatch.1
/usr/share/man/man1/augparse.1
/usr/share/man/man1/augtool.1
