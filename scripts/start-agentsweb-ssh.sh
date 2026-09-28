#!/usr/bin/env bash
set -euo pipefail

test -n "${AGENTSWEB_SSH_PUBLIC_KEY:-}"
ssh_dir="${RUNNER_TEMP}/agentsweb-ssh"
name="awesome-claude-${GITHUB_RUN_ID}-issue-ssh"
install -d -m 700 "$ssh_dir" "$HOME/.ssh"
printf '%s\n' "$AGENTSWEB_SSH_PUBLIC_KEY" > "$HOME/.ssh/authorized_keys"
chmod 600 "$HOME/.ssh/authorized_keys"
sudo apt-get update -qq
sudo apt-get install -y -qq openssh-server
git clone --depth 1 --filter=blob:none --sparse https://github.com/agents-dev/agent-workspace.git "$ssh_dir/agent-workspace"
git -C "$ssh_dir/agent-workspace" sparse-checkout set lolgames_tunnel
sudo mkdir -p /run/sshd
sudo /usr/sbin/sshd -D -e -p 2222 \
  -o PasswordAuthentication=no -o PermitRootLogin=no -o PubkeyAuthentication=yes \
  > "$ssh_dir/sshd.log" 2>&1 &
echo $! > "$ssh_dir/sshd.pid"
for _ in {1..60}; do
  ss -ltn | grep -q ':2222 ' && break
  sleep 1
done
ss -ltn | grep -q ':2222 '
requested_port=$((32000 + GITHUB_RUN_ID % 1000))
nohup env PYTHONPATH="$ssh_dir/agent-workspace" \
  python3 -m lolgames_tunnel client 127.0.0.1:2222 \
  --server agentsweb.space --name "$name" --public-port "$requested_port" \
  > "$ssh_dir/tunnel.log" 2>&1 < /dev/null &
echo $! > "$ssh_dir/tunnel.pid"
for _ in {1..60}; do
  grep -q '^ssh://' "$ssh_dir/tunnel.log" && break
  kill -0 "$(cat "$ssh_dir/tunnel.pid")" 2>/dev/null || break
  sleep 1
done
endpoint="$(sed -nE 's#^ssh://([^:[:space:]]+):([0-9]+).*$#\1 \2#p' "$ssh_dir/tunnel.log" | head -n 1)"
read -r host port <<< "$endpoint"
test -n "$host" && test -n "$port"
{
  echo '## Owner SSH debugging'
  echo
  echo 'Connect during analysis and for 30 minutes after it finishes or fails:'
  echo
  echo '```sh'
  echo "ssh -tt -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i ~/.ssh/aiplay-agentsweb -p $port runner@$host"
  echo '```'
} >> "$GITHUB_STEP_SUMMARY"
