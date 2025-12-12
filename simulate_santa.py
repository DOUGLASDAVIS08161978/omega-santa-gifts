#!/usr/bin/env python3
"""
Simulation runner for Mega Omega Santa
Runs for a controlled time period and captures output
"""
import subprocess
import time
import signal
import sys

def simulate_santa_run(duration_seconds=30):
    """
    Run Mega Omega Santa for a specified duration and capture output

    Args:
        duration_seconds: How long to run the simulation
    """
    print(f"Starting Mega Omega Santa simulation for {duration_seconds} seconds...")
    print("=" * 80)
    print()

    # Start the process
    process = subprocess.Popen(
        [sys.executable, "mega_omega_santa.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        universal_newlines=True
    )

    start_time = time.time()

    try:
        # Read output in real-time
        while True:
            # Check if we've exceeded the duration
            if time.time() - start_time >= duration_seconds:
                print("\n" + "=" * 80)
                print(f"Simulation time limit reached ({duration_seconds}s)")
                print("Terminating Santa Omega gracefully...")
                print("=" * 80)
                process.send_signal(signal.SIGINT)
                time.sleep(2)
                if process.poll() is None:
                    process.terminate()
                break

            # Read output line by line
            line = process.stdout.readline()
            if line:
                print(line, end='')
            elif process.poll() is not None:
                # Process has ended
                break
            else:
                # No output, small sleep
                time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user")
        process.send_signal(signal.SIGINT)
        time.sleep(1)
        if process.poll() is None:
            process.terminate()

    # Wait for process to fully terminate
    process.wait()

    print("\n" + "=" * 80)
    print("Simulation complete!")
    print("=" * 80)

if __name__ == "__main__":
    # Run simulation for 30 seconds
    simulate_santa_run(duration_seconds=30)
