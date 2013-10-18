%global _name          jboss-a-mq
%global _version       6.0.0.redhat.024

# To avoid the following error during rpm build:
# Arch dependent binaries in noarch package 
%define _binaries_in_noarch_packages_terminate_build   0

# select the right architecture
%define fusearch  noarch
%ifarch i386
%define fusearch  i386
%endif
%ifarch x86_64
%define fusearch  x86_64
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
Source1: activemq.xml
Source2: log4j.properties
Source3: jetty.xml
Source4: system.properties
Source5: jetty-realm.properties
Source6: users.properties
Source7: jboss-amq
Source8: karaf-wrapper.jar
Source9: karaf-wrapper-main.jar
Source10: libwrapper.so
Source11: jboss-amq-wrapper.conf
Source12: jboss-amq-wrapper
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: %{fusearch}
Requires:	java >= 0:1.5.0
Requires:	jpackage-utils

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
install %{SOURCE1} %{buildroot}%{homedir}/%{name}-%{version}/etc/activemq.xml
install %{SOURCE2} %{buildroot}%{homedir}/%{name}-%{version}/etc/log4j.properties
install %{SOURCE3} %{buildroot}%{homedir}/%{name}-%{version}/etc/jetty.xml
install %{SOURCE4} %{buildroot}%{homedir}/%{name}-%{version}/etc/system.properties
install %{SOURCE5} %{buildroot}%{homedir}/%{name}-%{version}/etc/jetty-realm.properties
install %{SOURCE6} %{buildroot}%{homedir}/%{name}-%{version}/etc/users.properties

# Copy the service script to the bin directory
install -m 0755 %{SOURCE7} %{buildroot}%{homedir}/%{name}-%{version}/bin/jboss-amq

# Copy the wrapper stuff
install -m 0755 %{SOURCE8} %{buildroot}%{homedir}/%{name}-%{version}/lib/karaf-wrapper.jar
install -m 0755 %{SOURCE9} %{buildroot}%{homedir}/%{name}-%{version}/lib/karaf-wrapper-main.jar
install -m 0755 %{SOURCE10} %{buildroot}%{homedir}/%{name}-%{version}/lib/libwrapper.so
install -m 0755 %{SOURCE11} %{buildroot}%{homedir}/%{name}-%{version}/etc/jboss-amq-wrapper.conf
install -m 0755 %{SOURCE12} %{buildroot}%{homedir}/%{name}-%{version}/bin/jboss-amq-wrapper


%post
# Add the service
ln -s %{homedir}/%{name}-%{version}/bin/jboss-amq /etc/init.d/
chkconfig jboss-amq --add

%clean
rm -rf $RPM_BUILD_ROOT

%postun
rm /etc/init.d/jboss-amq

%files
%defattr(-,root,root,-)
%{homedir}
