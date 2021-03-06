# jupyterhub
jupyterhub for asrc

(Optional -do this only if you get a permissions denied error) delete jupyterhub_cookie_secret file after shutting down or before starting jupyterhub:
cd /srv/jupyterhub
rm jupyterhub_cookie_secret
 
To run jupyterhub:
After logging into a user account,
cd /srv/jupyterhub
source activate jupyterhubEnv
/opt/anaconda/anaconda3/envs/jupyterhubEnv/bin/jupyterhub -f /etc/jupyterhub/jupyterhub_config.py &
To bring a background process to the foreground, enter: fg
To kill a process: kill -9 processName
Url: https://appsvr.asrc.cestm.albany.edu/ 
 
R installation:
conda install -c r r-essentials
 
Docker:
Files get converted into a docker image that contain all your project code
That image can then be run as a container
Each container is sort of like its own virtual machine
You can run as many containers as you want with each having there own settings like one having R and another having python or both
Limit to how many containers can be run is till the cpu and or ram gets bottlenecked 
Each container acts like a virtual machine but actually acts more like a self contained process.
All of the containers sit on the host ubuntu server resources.
 
To edit configuration file:
sudo emacs /etc/jupyterhub/jupyterhub_config.py
 
List of jupyterhub kernels available:
https://github.com/jupyter/jupyter/wiki/Jupyter-kernels 
 
How to use conda inside jupyterhub:
Go to the drop down menu on the top right corner of the homepage where it says new after logging in. 
Press on the terminal tab.
Once in terminal then type 
conda info --envs
This will list all of the available environments:
# conda environments:
#
python2               /opt/conda/envs/python2
root                  *  /opt/conda
(the one with the star is the current default one)
To switch environments type:
source activate environment name.

Now if you do conda info --envs again you will see that the default has changed.
What ever packages you now download will be downloaded to the new environment.
To go back to the default environment simply write source deactivate or source activate newEnvName.
 
Is it okay to run jh as root and how to run jh in background?
https://github.com/jupyterhub/jupyterhub/wiki/Using-sudo-to-run-JupyterHub-without-root-privileges
https://github.com/jupyterhub/jupyterhub/wiki/Run-jupyterhub-as-a-system-service
 
Google oauth vs system lvl auth / or should i just set up custom auth
Write 2-3 page tutorial on git, jh, env, file upload process 
 
Pip install git repoName
 
 
 
JupyterHub overview:
With JupyterHub you can create a multi-user Hub which spawns, manages, and proxies multiple instances of the single-user Jupyter notebook (IPython notebook) server.
 
Why use Jupyterhub:
A jupyterhub takes that notebook and expands it. So you still have users accessing the hub from a web browser just like the jupyter notebook but now you have a server that has a database with a spawner and an authenticator for users. You can now have users log into the environment where you have all your configurations done and all your data already in there for everyone to see and use.
 
In a jupyterhub notebook you can have text blocks, note blocks and code blocks. Best part is that you can tweak and of it and run it on the fly. Good option to present people with a uniform environment.
 
Takes out the headache of having people to install all of the packages and languages that you are using, so no matter if you're using windows,linux or a mac machine everyone will be able to run everything without a glitch because all you need is a browser. Everything else like the installation, the version of the language and libraries and other dependencies are now taken care of already in the jupyterhub server by the admin.
 
Things to consider before installation:
Jupyterhub install location should be in something like /srv/jupyterhub. After creating the folder the first thing you should do is cd into it and own it by running: sudo chown xcite . < don't forget the (dot)!
Python install location and path should be: /opt/anaconda/anaconda3/envs/jupyterhubEnv/bin/python
Reason for this is so it can be accessed across all users on the server and not just the local users. Same with python 2, should have kernels for all users in the hub. To do so need to have the path be available for all users not just local ones. The JupyterHub installation must be readable plus executable by all users.
 
Make sure you have ipykernel installed and use ipython kernel install to drop the kernel spec in the right location for python2. Then ipython3 kernel install for Python3. Now you should be able to chose between the 2 kernels regardless of whether you use jupyter notebook, ipython notebook or ipython3 notebook
 
Anaconda location and path should be: /opt/anaconda/anaconda3/bin/anaconda
Again for the same reason that it needs to be available for all users. All the python packages you downloaded should be available to all users in the hub. You don't want to have to download a separate python packages individually for each user. That would be a huge pain!
 
What you can do is create an Anaconda jupyterhub environment, then lets say if you named it jupyterhubEnv you can just do source jupyterhubEnv and have the path of that environment in /opt/ also to be available to all users and now when you start jupyterhub every user will have access to the same packages and languages.
 
Another thing you will need to do is to bind allow node to bind to port 80 without using sudo. You can do this by using setcap cap_net_bind_service=+ep. Since we will have our jupyterhubEnv active we can run sudo setcap cap_net_bind_service=+ep /opt/anaconda/anaconda3/envs/jupyterhubEnv/bin/node once that is done we can then run: 
sudo /opt/anaconda/anaconda3/bin/npm install -g configurable-http-proxy which will be needed for docker to run properly. To see which ip address docker is running you can run ifconfig and you will see the address under docker0 which we will need to set in the configuration file for jupyterhub. To install the configurable-http-proxy package globally using npm: npm install -g configurable-http-proxy which is actually the better way to go about it. 
 
You will also need some sort of text editor. I choose to use emacs which i also needed to install. Git is something you will need to install to pull the latest version of jupyterhub, letsencrypt and docker spwaner. To Get letsencrypt: git clone https://github.com/letsencrypt/letsencrypt
cd letsencrypt
 Once you have letsencrypt you need to activate it by going into the folder and running ./letsencrypt-auto certonly --standalone -d appsvr.asrc.cestm.albany.edu where appsvr.asrc.cestm.albany.edu is your domain name. Once that is done it will ask for some basic info like email name organization ect. Which will then generate the cert and key you will need to use in the jupyterhub_config.py file. For letsencrypt to work automatically you will need to change the permissions of the archive and live folder which are located in /etc/letsencrypt. To do this simply cd into the folder and run the two commands:
 sudo chmod 777 -R archive/
 sudo chmod 777 -R live/
 
Once you have all the prerequisites installed then you can run jupyterhub --generate-config to generate an empty configuration file where you will customize everything from user list to using docker spawner.
 
Docker spawner installation instructions:
pip install dockerspawner
docker pull jupyterhub/singleuser
apt-cache policy docker-engine
sudo apt-get install -y docker-engine
sudo systemctl status docker
 
About Docker spawner:
Runs the JupyterHub components in a Docker container on the host
Uses DockerSpawner to spawn single-user Jupyter Notebook servers in separate Docker containers on the same host
Persists JupyterHub data in a Docker volume on the host
Persists user notebook directories in Docker volumes on the host

JupyterHub is an authenticated service - uses users login. For security you can use letsencrypt to set up SSL to use https (you shouldn't run jupyterhub without ssl because it's going to be dealing with people's passwords). 
 
Requirements:
Python 3.3 or greater (and pip) 
Netifaces for dockerspwaner
Ipykernel 
Xarray for raspPy
Gcc will also be needed for installing jupyterhub properly.
nodesjs/npm, install with: sudo apt-get install npm nodejs-legacy (install nodejs first then get npm)
Any unix server (will need to take care of security since it will be run over internet) 
TLS certificate and key for HTTPS communication
Domain name : appsvr.asrc.cestm.albany.edu
Authenticator which we are using: PAM which uses the user accounts that are stored on the server of which jupyterhub is running on. Oauth from github would of been nice but the latest release seems to have many bugs so stay away from it.
Using PAM as the authenticator means we will need to create a user account on the system for each user.
Default spawners: starts a notebook server on the same machine running under their system username (one dedicated server per user). The better option would be using Docker which would start each server in a separate container which is what I have set up.
Default proxy listens on all public intergaces on port 8000 
Folders and File Locations
/srv/jupyterhub for all security and runtime files
/etc/jupyterhub for all configuration files
/var/log for log files
The Proxy’s main IP address setting determines where JupyterHub is available to users. (to change the IP address and port):
jupyterhub --ip=192.168.1.2 --port=443
Or by setting it in the config file:
c.JupyterHub.ip = '192.168.1.2'
c.JupyterHub.port = 443
 
Security config requirements:
SSL encryption (to enable HTTPS)
After installing a key and certification that we can get for free from https://letsencrypt.org/ then we need to specify their locations in the config file as: c.JupyterHub.ssl_key = '/path/to/my.key'
       c.JupyterHub.ssl_cert = '/path/to/my.cert'
IF we use letsencrypt with default options:
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/{mydomain.tld}/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/{mydomain.tld}/fullchain.pem'
Where mydomain.tld is replaced by our fully qualified domain name
Cookie secret (a key for encrypting browser cookies)
Stored in config file : c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/cookie_secret'
The content of this file should be 32 random bytes, encoded as hex. An example would be to generate this file with: openssl rand -hex 32 > /srv/jupyterhub/cookie_secret
Should store it in /srv/jupyterhub/cookie_secret
Proxy authentication token (used for the Hub and other services to authenticate to the Proxy)
Can set up in config file: jupyterhub_config.py
Use values for file: c.JupyterHub.proxy_auth_token = '0bc02bede919e99a26de1e2a7a5aadfaf6228de836ec39a05a6c6942831d8fe5'


Creating a whitelist to restrict which users are allowed to login 
Users listed in the whitelist are added to the Hub database when the Hub is started
Authenticator.whitelist:
c.Authenticator.whitelist = {'arnold', 'mark', 'xcite', 'ect’}
c.Authenticator.admin = {'arnold', 'mark', 'xcite'}
Using Jupyterhub:
Jupyterhub will be accessed through a web browser using either an IP address or domain name of the server.
To start jupyterhub with default configuration run:
sudo /opt/anaconda/anaconda3/envs/jupyterhubEnv/bin/jupyterhub
Any user on the system with a password will be allowed to start a single user notebook server
Can reach jupyterhub through:
https://appsvr.asrc.cestm.albany.edu/
By default, starting JupyterHub will write two files to disk in the current working directory:
jupyterhub.sqlite is the sqlite database containing all of the state of the Hub. This file allows the Hub to remember what users are running and where, as well as other information enabling you to restart parts of JupyterHub separately. It is important to note that this database contains no sensitive information other than Hub usernames.
jupyterhub_cookie_secret is the encryption key used for securing cookies. This file needs to persist in order for restarting the Hub server to avoid invalidating cookies. Conversely, deleting this file and restarting the server effectively invalidates all login cookies.
Example of configuration file:
# Configuration file for jupyterhub.                                                                                                                                                                        
 
#ssl encryption using letsencrypt self ser                                                                                                                                                                  
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/appsvr.asrc.cestm.albany.edu/fullchain.pem'
c.JupyterHub.port = 443
 
#set of users allowed to use the hub                                                                                                                                                                       \
                                                                                                                                                                                                            
c.Authenticator.whitelist = {'xcite', 'arnold', 'mark', 'arnoldas500'}
 
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
 
 
 
