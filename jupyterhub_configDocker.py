# Configuration file for jupyterhub.                                                                                                                                                                        

#ssl encryption using letsencrypt self ser                                                                                                                                                                  
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/fullchain.pem'
c.JupyterHub.port = 443

#set of users allowed to use the hub                                                                                                                                                                       \
                                                                                                                                                                                                            
c.Authenticator.whitelist = {'xcite', 'arnold', 'mark'}

#set of admins allowed to use the hub                                                                                                                                                                      \
                                                                                                                                                                                                            
c.Authenticator.admin_users = {'xcite', 'arnold', 'mark'}

#for github oauthentication                                                                                                                                                                                 
#from oauthenticator.github import LocalGitHubOAuthenticator                                                                                                                                                
#c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator                                                                                                                                               

####TESTING without github oauth                                                                                                                                                                            
#from oauthenticator.github import GitHubOAuthenticator                                                                                                                                                     
#c.JupyterHub.authenticator_class = GitHubOAuthenticator                                                                                                                                                    

from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner

# The Hub's API listens on localhost by default, # but docker containers can't see that.                                                                                                                    
# Tell the Hub to listen on its docker network:                                                                                                                                                             
import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']
