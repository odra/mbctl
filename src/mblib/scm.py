import tempfile

import git


def get_latest_commit(repo, branch):
  """
  Retrieves latest commit hash (sha1) from a repository.

  It will:

  * clone the repository locally into a temporary folder
  * reset the repository to the specified branch
  * Get the latest commit hash
  * Delete the temporary directory
  """
  local_dir = tempfile.mkdtemp()
  repo = git.Repo.clone_from(repo, local_repo_dir, depth=1)
  sha = repo.rev_parse(f'origin/{branch}')
  shutil.rmtree(local_dir)

  return sha