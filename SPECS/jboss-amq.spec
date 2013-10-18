%global _name          jboss-a-mq
%global _version       6.0.0.redhat.024

# To avoid the following error during rpm build:
# Arch dependent binaries in noarch package 
%define _binaries_in_noarch_packages_terminate_build   0

# select the right architecture
%define fusearch  unknown
%define fuseother unknown
%ifarch i386
%define fusearch  32
%define fuseother 64
%endif
%ifarch x86_64
%define fusearch  64
%define fuseother 32
%endif

# I'm running the spec and SOURCES from within an eclipse
# workspace, so I've set the topdir
%define _topdir %(echo $PWD)/

# Lets set the jbos-amq in /opt.
# I've defined a libdir, but for the moment lets keep it in the
# home folder.
%define homedir /opt
%define libdir /opt/%{_name}-%{version}/lib
%define datadir /var/amqdata/%{_name}
%define logdir /var/log/%{_name}
%define docsdir /usr/share/doc/%{name}-%{version}

Summary: JBoss A-MQ
Name: %{_name}
Version: %{_version}
Release: 1%{?dist}
License: ASL 2.0
Group: System Environment/Daemons
URL: http://activemq.apache.org/
Source0: jboss-a-mq-6.0.0.redhat.024.zip
Source1: activemq.init.rh
Source2: activemq.xml
Source3: log4j.properties
Source4: jetty.xml
Source5: system.properties
Source6: jetty-realm.properties
Source7: activemq-wrapper.conf
Source8: users.properties
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch
Requires: tanukiwrapper >= 3.5.9
Requires: java >= 0:1.5.0

%description
Fuse Message Broker is an open source messaging platform based on
Apache ActiveMQ that is productized and supported by the people who
wrote the code. Fuse Message Broker is the JMS platform of choice for
scalable, high-performance SOA infrastructure to connect processes
across heterogeneous systems.

%prep
%setup -c jboss-a-mq-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{homedir}
mv * %{buildroot}%{homedir}

# Config files
install %{SOURCE2} %{buildroot}%{homedir}/%{name}-%{version}/etc/activemq.xml
install %{SOURCE3} %{buildroot}%{homedir}/%{name}-%{version}/etc/log4j.properties
install %{SOURCE4} %{buildroot}%{homedir}/%{name}-%{version}/etc/jetty.xml
install %{SOURCE5} %{buildroot}%{homedir}/%{name}-%{version}/etc/system.properties
install %{SOURCE6} %{buildroot}%{homedir}/%{name}-%{version}/etc/jetty-realm.properties
install %{SOURCE7} %{buildroot}%{homedir}/%{name}-%{version}/etc/activemq-wrapper.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{homedir}





