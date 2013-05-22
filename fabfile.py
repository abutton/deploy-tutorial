from fabric.api import env, cd, local

env.user = "abutton"
env.hosts = ["192.168.88.120"]

def deploy():
    cd('~/projects/deploy-tutorial/')
    local('git pull')
    local('bin/pelican -s mysite.py')
