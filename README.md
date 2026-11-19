# Anti-Matrix: Alpha Omega (V0.1)

**The 100% offline execution firewall and tamper-evident flight recorder for AI coding agents.**

Built for **Claude Code**, **Cursor**, **Antigravity IDE**, and any **Model Context Protocol (MCP)** client.

**Zero cloud. Zero telemetry. Zero Docker. Zero subscriptions.**

**[Get Anti-Matrix (Alpha Omega V0.1) on Polar.sh (One-Time License)](https://buy.polar.sh/polar_cl_VNgWwqs4xBMgbacXYtQDXQJUoAMi5eWZu30ID1lUzpL)**

---

## Why Developers Need Anti-Matrix

AI coding agents run with your full local permissions. One poisoned README, one hallucinated cleanup command, or one runaway retry loop can wipe a repository, leak production credentials into a model prompt, or burn through your API budget overnight.

Anti-Matrix sits directly between your AI agent and your local operating system as a standalone native binary, enforcing deterministic, binary-level security boundaries that prompts alone cannot bypass.

---

## Why "Alpha Omega"?

- **Alpha (Clean Start):** Ships with a clean slate on your machine: zero cloud pre-training, zero shared profiles, and zero telemetry. Nothing phones home and nothing is baked in from someone else's environment.
- **Omega (Built Around Your Workflow):** Learns and adapts strictly from your local project, commands, and tool outcomes across sessions and restarts. It remembers which execution paths succeed in your codebase and avoids repeating dead ends, staying with you from your first command to your final build.

---

## Core Protections

### 1. Stops Poisoned Prompts & Prompt Injection Cold
Even if a malicious README, poisoned dependency, or tricked "Don't Ask Again" approval attempts to exfiltrate `.env` secrets or wipe your workspace, hardcoded binary-level guardrails block the action unconditionally: **zero prompt-based override possible**.

### 2. Protects Against Both Rogue Agents & Accidental Human Mistakes
Before any file operation or command touches disk, Anti-Matrix enforces strict workspace confinement (`--workspace`) and blocks:
- Destructive commands: `rm -rf`, `del`, `taskkill`, and flag-reordered variants
- Interactive shell LOLBins by default: `cmd`, `powershell`, `pwsh`, `bash`, `sh`, `zsh`, `wsl`
- Shell chaining & injection: `&&`, `|`, `;`, `:`, redirects, and null-byte smuggling
- Path escapes: `../` traversal, drive/UNC/root escapes, and escaping symlinks or junctions

### 3. Triple-Layer DLP Secret Redaction
Automatically detects and masks sensitive credentials (including `OPENAI_API_KEY`, `GITHUB_TOKEN`, `.env` secrets, `sk_live_`, `sk-proj-`, `ghp_`, `github_pat_`, `AIza`, `AKIA`, `xoxb-`, and `Bearer` tokens), replacing them with `[REDACTED]` across:
- **File reads** (`workspace_read_file`)
- **Command `stdout`**
- **Command `stderr`**
- **Local audit logs**

Child processes also execute in a stripped environment (`.env_clear()`), preventing host secrets from leaking into spawned tools.

### 4. Kills $2,000+ Runaway Retry Loops
- **3-Strike Anti-Loop Circuit Breaker (`INHIBITOR_CIRCUIT_BREAKER`):** Detects consecutive identical failing commands executed without an intervening file edit and immediately halts execution on the 3rd strike, forcing the agent to modify code or switch strategy instead of burning tokens.
- **30-Second Hung-Process Termination (`--cmd-timeout 30`):** Automatically kills stalled child processes and drains pipes cleanly so your agent session never deadlocks.

### 5. Tamper-Evident Flight Recorder
Every execution intent, policy block, and tool outcome is recorded locally in an append-only, cryptographically chained `SHA-256` audit log (`audit.log`) that can be verified at any time via `kernel_audit_verify`, alongside 100% offline execution with zero Docker, zero cloud, zero telemetry, and zero subscriptions.

### 6. Native Cross-Platform Binaries
Single standalone executables with zero runtime dependencies:
- **Windows x64** (`Anti-Matrix-Alpha-Omega-v0.1-windows-x64.zip`)
- **macOS Apple Silicon** (`Anti-Matrix-Alpha-Omega-v0.1-macos-arm64.zip`)
- **macOS Intel** (`Anti-Matrix-Alpha-Omega-v0.1-macos-x64.zip`)
- **Linux x64** (`Anti-Matrix-Alpha-Omega-v0.1-linux-x64.zip`)

---

## Battle-Tested Proof

- **62/62 automated cross-platform tests passing** across Windows, macOS (Apple Silicon & Intel), and Linux, plus blind `--mcp-stdio` startup and protocol framing checks.
- **60+ live adversarial & Red-Team probes** executed inside Antigravity IDE, verifying:
  - Workspace path-escape and symlink/junction traversal blocks
  - Interactive shell & LOLBin rejection (`cmd`, `powershell`, `bash`, etc.)
  - Triple-layer `.env` and API key DLP redaction (`[REDACTED]`)
  - 30-second hung-process timeout kill & pipe-drain recovery
  - Cross-restart state and policy persistence
  - 3-strike `INHIBITOR_CIRCUIT_BREAKER` loop breaking and post-edit reset

---

## 30-Second Quickstart

### 1. Drop-In MCP Configuration (`presets/anti-matrix.mcp.json`)

Copy [`presets/anti-matrix.mcp.json`](presets/anti-matrix.mcp.json) into your Cursor, Claude Code, or Antigravity MCP configuration:

```json
{
  "mcpServers": {
    "living-automaton-agent-guard": {
      "command": "living_automaton_kernel.exe",
      "args": [
        "--profile", "agent-guard",
        "--workspace", ".",
        "--data-dir", ".lak-data",
        "--cmd-timeout", "30",
        "--mcp-stdio"
      ]
    }
  }
}
```

### 2. `PreToolUse` Hook (`presets/anti-matrix-hook.py`)

Use [`presets/anti-matrix-hook.py`](presets/anti-matrix-hook.py) to gate tool invocations before execution (`EXIT 0` allow vs `EXIT 2` block).

### 3. Verify Release Integrity (`SHA256SUMS.txt`)

Verify your downloaded release archive against [`SHA256SUMS.txt`](SHA256SUMS.txt):

```powershell
# Windows (PowerShell)
Get-FileHash -Algorithm SHA256 .\Anti-Matrix-Alpha-Omega-v0.1-windows-x64.zip
```

```bash
# macOS / Linux
shasum -a 256 -c SHA256SUMS.txt --ignore-missing
```

---

## Repository Contents

- `README.md`: Product overview, protections, verification proof, and quickstart.
- `presets/anti-matrix.mcp.json`: Drop-in MCP configuration preset (`--profile agent-guard`).
- `presets/anti-matrix-hook.py`: Lightweight `PreToolUse` hook script.
- `SHA256SUMS.txt`: Release archive SHA-256 verification checksums.
- `LICENSE`: Commercial license terms.

> **Note:** This public showcase repository contains only presets, release checksums, documentation, and license terms. Proprietary source code and local runtime state are intentionally excluded.
