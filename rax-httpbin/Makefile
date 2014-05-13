site:
	RAX_CREDS_FILE=~/.rackspace_cloud_credentials RAX_REGION=ORD ansible-playbook -i inventory/ -v site.yml

listhosts:
	RAX_CREDS_FILE=~/.rackspace_cloud_credentials RAX_REGION=ORD ansible all -i inventory/ -v --list-hosts -m ping
