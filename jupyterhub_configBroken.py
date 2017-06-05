# jupyterhub_configBroken.py                                                                                                                                                                                      
c = get_config()

import os
pjoin = os.path.join

runtime_dir = os.path.join('/srv/jupyterhub')
ssl_dir = pjoin(runtime_dir, 'ssl')
if not os.path.exists(ssl_dir):
    os.makedirs(ssl_dir)


# Allows multiple single-server per user                                                                                                                                                                    
c.JupyterHub.allow_named_servers = True

# https on :443                                                                                                                                                                                             
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/fullchain.pem'

# put the JupyterHub cookie secret and state db                                                                                                                                                             
# in /var/run/jupyterhub                                                                                                                                                                                    
c.JupyterHub.cookie_secret_file = pjoin(runtime_dir, 'cookie_secret')
c.JupyterHub.db_url = pjoin(runtime_dir, 'jupyterhub.sqlite')
# or `--db=/path/to/jupyterhub.sqlite` on the command-line                                                                                                                                                  

# put the log file in /var/log                                                                                                                                                                              
c.JupyterHub.extra_log_file = '/var/log/jupyterhub.log'

# use GitHub OAuthenticator for local users                                                                                                                                                                 

c.JupyterHub.authenticator_class = 'oauthenticator.LocalGitHubOAuthenticator'
c.GitHubOAuthenticator.client_secret = '5362c66ccff1766756910fc6c506fba99623458c'
c.GitHubOAuthenticator.oauth_callback_url = 'https://appsvr.asrc.cestm.albany.edu/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = 'e28b956b838b69ebffcf'

# create system users that don't exist yet                                                                                                                                                                  
c.LocalAuthenticator.create_system_users = True

# specify users and admin                                                                                                                                                                                   
c.Authenticator.whitelist = {'xcite', 'arnold', 'mark',"arnoldas500"}
c.Authenticator.admin_users = {'xcite', 'arnold', 'mark',"arnoldas500"}

from dockerspawner import DockerSpawner                                                                                                                                                                    \

c.JupyterHub.spawner_class = DockerSpawner                                                                                                                                                                 \

                                                                                                                                                                                                           \

# The Hub's API listens on localhost by default, # but docker containers can't see that.                                                                                                                    
# Tell the Hub to listen on its docker network:                                                                                                                                                             
import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']

