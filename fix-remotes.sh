#!/bin/bash

echo "🔍 Scanning for Git repos using github.com-personal..."

find . -type d -name ".git" | while read gitdir; do
  repo_dir=$(dirname "$gitdir")
  cd "$repo_dir" || continue

  remote_url=$(git remote get-url origin 2>/dev/null)

  if [[ "$remote_url" == *"github.com-personal:"* ]]; then
    new_url="${remote_url/github.com-personal:/github.com:}"
    
    echo "📁 Repo: $repo_dir"
    echo "🔄 Updating remote:"
    echo "   Old: $remote_url"
    echo "   New: $new_url"

    git remote set-url origin "$new_url"
    echo "✅ Done"
    echo
  fi

  cd - >/dev/null
done

echo "✨ All matching remotes updated."
