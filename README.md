rpmbuild-jboss-amq
==================

Rpm build of JBoss A-MQ

Download jboss-a-mq-6.0.0.redhat-024.zip from http://www.jboss.org/products/amq 
 and rename it to jboss-a-mq-6.0.0.redhat.024.zip
(rpmbuild seems to have some trouble with the - in -024.zip)

Put the zip into the SOURCES folder.

Check/adapt the spec file (SPECS/jboss-amq.spec)
before running the rpm build.
Also check the config files in SOURCES, those files will
be injected into the ${jboss-amq-home}/etc folder.

If the rpm installs itself correctly, you can start with: 
service jboss-amq start

TODO's: 
Define architecture in spec file
Clean up spec file
Check the config files in SOURCES

