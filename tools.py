import subprocess

def selenium_executor(script_code: str) -> str:
    with open("runner/temp_test.py", "w") as f:
        f.write(script_code)
    try:
        result = subprocess.run(["python", "runner/temp_test.py"], capture_output=True, text=True, timeout=60)
        return result.stdout + "\n" + result.stderr
    except Exception as e:
        return str(e)