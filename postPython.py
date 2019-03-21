from git import Repo
path = 'D://Users//JaeW//OneDrive - Onyx Reporting//Documents//GitHub//learnNLTK'
repo = Repo(path)

repo.untracked_files

repo.index.add(['postPython.py'])  
repo.index.commit("Added a new file in the past - for later merege")


repo.git.pull('origin')
repo.git.push('origin')

origin = repo.remote(name='origin')
origin.push()