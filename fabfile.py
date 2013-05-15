from fabric.api import env, run, cd

env.user = "abutton"
env.hosts = ["pycourse.com"]

def deploy():
    cd('~/blog')
    run('git pull')
    run('bin/pelican -s mysite.py')
