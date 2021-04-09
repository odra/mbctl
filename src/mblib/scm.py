import shutil
import tempfile

from . import errors

import git


def get_latest_commit(repo, branch):
  """
  Retrieves latest commit hash (sha1) from a repository.

  It will:

  * clone the repository locally into a temporary folder
  * reset the repository to the specified branch
  * Get the latest commit hash
  * Delete the temporary directory

  Parameters
  ----------
  repo: str
    A valid public git repository url.

  branch: str
    A valid and existing branch name of the given repository.

  Returns
  -------
  str:
    The most recent commit hash (sha1)
  """
  local_dir = tempfile.mkdtemp()
  try:
    repo = git.Repo.clone_from(repo, local_dir, depth=1)
    sha = repo.rev_parse(f'origin/{branch}')
  except git.exc.GitCommandError as e:
    raise errors.MBError(str(e))
  finally:
    shutil.rmtree(local_dir)

  return sha
