from fabric.api import env, cd, local

env.user = "abutton"

def deploy():
    cd('~/projects/deploy-tutorial/')
    local('git pull')
    local('bin/pelican -s mysite.py')
