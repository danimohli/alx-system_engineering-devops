#!/usr/bin/pup
# This Puppet manifest installs Flask version 2.1.0 using pip3

package { 'flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
