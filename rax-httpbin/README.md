# rax-httpbin

Set of sample playbooks to deploy httpbin on Rackspace

## Configure

1. Upload your ssh public key to rackspace (This can be done via the mycloud portal)
1. Edit `group_vars/all`, and replace `~/.ssh/id_rsa` for `ansible_ssh_private_key_file` with the path to your private key
1. Edit `group_vars/all`, and configure the region you want to deploy to
1. Edit `group_vars/all`, and change the domain you want to use for DNS

## Using

The new site will be available at httpbin.YOURDOMAIN.COM.  Each server will be bin0[1-3].YOURDOMAIN.COM.

nginx is configured to listen on 0.0.0.0:80 and proxy to localhost:5001.  gunicorn is listening on 0.0.0.0:5001.  The Cloud Load balancer is configured to listen on port 80 and proxy to each of the 3 created cloud servers.
