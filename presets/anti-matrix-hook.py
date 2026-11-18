import json
import subprocess
import sys

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {})
target = tool_input.get("command") or tool_input.get("file_path") or ""
res = subprocess.run(
    [
        "living_automaton_kernel.exe",
        "--profile", "agent-guard",
        "--data-dir", ".lak-data",
        "--workspace", ".",
        "--cmd", f"pulse proc {target}",
    ],
    capture_output=True, text=True, check=False,
)
out = (res.stdout or "") + (res.stderr or "")
if any(k in out for k in ("BLOCKED", "Layer 1", "Layer 2", "INHIBITOR_CIRCUIT_BREAKER", "ERROR")):
    sys.stderr.write(f"Blocked by Agent-Guard Kernel: {out.strip()}\n")
    sys.exit(2)
sys.exit(0)
