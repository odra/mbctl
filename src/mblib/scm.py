import tempfile

import git


def get_latest_commit(repo, branch):
  local_dir = tempfile.mkdtemp()
  repo = git.Repo.clone_from(repo, local_repo_dir, depth=1)
  sha = repo.rev_parse(f'origin/{branch}')
  shutil.rmtree(local_dir)

  return sha
