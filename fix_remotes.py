import os
import subprocess
import sys

def find_git_repos(base_dir):
    git_repos = []
    for root, dirs, files in os.walk(base_dir):
        if ".git" in dirs:
            git_repos.append(root)
            dirs[:] = []  # Don't descend into subdirectories of a git repo
    return git_repos

def get_remote_url(repo_path):
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

def set_remote_url(repo_path, new_url):
    subprocess.run(["git", "-C", repo_path, "remote", "set-url", "origin", new_url])

def update_remotes(base_dir):
    repos = find_git_repos(base_dir)
    updated = 0

    for repo in repos:
        url = get_remote_url(repo)
        if url and "github.com-personal:" in url:
            new_url = url.replace("github.com-personal:", "github.com:")
            print(f"\n📁 Repo: {repo}")
            print(f"🔄 Updating remote:")
            print(f"   Old: {url}")
            print(f"   New: {new_url}")
            set_remote_url(repo, new_url)
            updated += 1

    if updated == 0:
        print("\n✅ No remotes needed updating.")
    else:
        print(f"\n✨ Updated {updated} remotes.")

if __name__ == "__main__":
    # Use command line argument if provided, otherwise use current directory
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
        if not os.path.isdir(base_path):
            print(f"Error: The path '{base_path}' is not a valid directory.")
            sys.exit(1)
    else:
        base_path = os.getcwd()
        
    print(f"🔍 Scanning repos in: {base_path}")
    update_remotes(base_path)
