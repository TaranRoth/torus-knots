import subprocess
import json

try:
    # Replace 'node' with the path to your Node.js executable if not in PATH
    # Replace 'your_script.mjs' with the actual path to your .mjs file
    result = subprocess.run(['node', 'your_script.mjs'], capture_output=True, text=True, check=True)
    output_data = json.loads(result.stdout)
    print(output_data)
except subprocess.CalledProcessError as e:
    print(f"Error executing .mjs script: {e}")
    print(f"Stderr: {e.stderr}")
except json.JSONDecodeError:
    print("Failed to parse JSON output from .mjs script.")