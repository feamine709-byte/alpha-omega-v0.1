# Anti-Matrix — Alpha Omega · V0.1

**A 100% offline, local execution firewall and tamper-evident flight recorder for AI coding agents** — built for Claude Code, Cursor, Antigravity IDE, and any Model Context Protocol (MCP) client.

**Zero cloud. Zero telemetry. Zero Docker. Zero subscriptions.**

---

## Core Protections

1. **Immutable Boundary Confinement & Destructive Command Blocking**
   - Strictly confines file reads/writes and child process execution inside `--workspace` via canonical path resolution and symlink/junction verification.
   - Blocks path traversal (`..`, drive/UNC/root escapes), destructive commands (`rm -rf`, flag-reordered variants), interactive shell LOLBins (`cmd`, `powershell`, `pwsh`, `bash`, `sh`, `zsh`, `wsl`) by default, shell metacharacters (`&&`, `|`, `;`, `:`, redirects), and null-byte smuggling.
   - Isolates child process environments (`.env_clear()` with minimal baseline OS variables) and enforces bounded wall-clock timeouts (`--cmd-timeout 30`) with deadlock-free pipe draining.

2. **Automatic DLP Secret Redaction**
   - Automatically scrubs sensitive credentials and tokens (`.env` values, `sk_live_`, `sk-proj-`, `ghp_`, `github_pat_`, `AIza`, `AKIA`, `xoxb-`, `Bearer` tokens, and active API keys) across file reads, `stdout`, `stderr`, and audit logs before output ever reaches the model context.

3. **3-Strike Anti-Loop Circuit Breaker (`INHIBITOR_CIRCUIT_BREAKER`)**
   - Detects consecutive identical failing commands executed without an intervening workspace file modification and trips a hard circuit breaker on the 3rd strike — forcing the agent to edit code or switch strategy instead of burning tokens in runaway retry loops.
   - Pairs with adaptive multi-strategy routing (`workspace_adaptive_route`) and bounded build/repair loops (`workspace_build_repair_loop`).

4. **Cryptographically Chained, Tamper-Evident Audit Flight Recorder**
   - Records execution intents, policy blocks, and outcomes in an append-only SHA-256 hash-chained `audit.log`, verifiable at any time via `kernel_audit_verify`, alongside crash-safe atomic state snapshots (`kernel.snap`).

5. **Native Cross-Platform Binaries**
   - Single standalone native executables with zero runtime dependencies for:
     - **Windows x64** (`Anti-Matrix-v0.3.0-windows-x64.zip`)
     - **macOS Apple Silicon** (`Anti-Matrix-v0.3.0-macos-arm64.zip`)
     - **macOS Intel** (`Anti-Matrix-v0.3.0-macos-x64.zip`)
     - **Linux x64** (`Anti-Matrix-v0.3.0-linux-x64.zip`)

---

## Verification & Proof

- **62/62 automated tests passing** across Windows, macOS (`arm64` & `x64`), and Linux, plus blind `--mcp-stdio` startup and framing checks.
- **60+ live adversarial & Red-Team field tests** executed inside Antigravity IDE, verifying:
  - Workspace path-escape and symlink/junction traversal blocks
  - Interactive shell & LOLBin rejection (`cmd`, `powershell`, `bash`, etc.)
  - `.env` and API key DLP redaction across file reads, `stdout`, `stderr`, and `audit.log`
  - Child-process timeout kill & pipe-drain recovery
  - Cross-restart state & policy persistence
  - 3-strike `INHIBITOR_CIRCUIT_BREAKER` loop breaking and post-edit reset

---

## Quickstart (Drop-In Presets)

### 1. MCP Server Config (`presets/anti-matrix.mcp.json`)

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

### 3. Release Checksum Verification (`SHA256SUMS.txt`)

Verify your downloaded release archive against [`SHA256SUMS.txt`](SHA256SUMS.txt):

```powershell
# Windows (PowerShell)
Get-FileHash -Algorithm SHA256 .\Anti-Matrix-v0.3.0-windows-x64.zip
```

```bash
# macOS / Linux
shasum -a 256 -c SHA256SUMS.txt --ignore-missing
```

---

## Repository Contents

- `README.md` — Product overview, security guarantees, verification proof, and quickstart.
- `presets/anti-matrix.mcp.json` — Drop-in MCP configuration preset (`--profile agent-guard`).
- `presets/anti-matrix-hook.py` — Lightweight `PreToolUse` hook script.
- `SHA256SUMS.txt` — Release archive SHA-256 verification checksums.
- `LICENSE` — Commercial license terms.

> **Note:** This public showcase repository contains only presets, release checksums, documentation, and license terms. Source code and local runtime state are intentionally excluded.
