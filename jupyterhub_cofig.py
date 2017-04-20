c.JupyterHub.ssl_key = 'jupyterhub.key'
c.JupyterHub.ssl_cert = 'jupyterhub.crt'
c.JupyterHub.port = 443


# set of users allowed to use the Hub
c.Authenticator.whitelist = {'xcite' }
# set of users who can administer the Hub itself
c.Authenticator.admin_users = {'xcite'}


#for using OAuth from github
from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
c.LocalGitHubOAuthenticator.create_system_users = True


#for using docker 
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner


from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner
# The Hub's API listens on localhost by default,
# but docker containers can't see that.
# Tell the Hub to listen on its docker network:
import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']


DockerSpawner.container_image = 'jupyterhub/singleuser'

