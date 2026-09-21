import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CaptureModule")

CAPTURE_PATH = "/tmp/ocr_capture.png"

def _capture_slurp_grim(output_path: str) -> bool:
    try:
        #get coordinates from slurp
        slurp = subprocess.run(
            ["slurp"],
            capture_output=True,
            text=True,
            check=True
        )
        coords = slurp.stdout.strip()
        if not coords:
            return False

        #feed coordinates into grim
        grim = subprocess.run(
            ["grim", "-g", coords, output_path],
            capture_output=True,
            text=True
        )

        if grim.returncode == 0 and os.path.exists(output_path):
            logger.info("OK Successfully captured screen via slurp + grim.")
            return True
        return False

    except (subprocess.CalledProcessError, FileNotFoundError):
        # Triggered if slurp/grim missing or user hits Esc to cancel
        return False

#im embarrassed how spectacle looks like a dependency here 
#but it actually is not i swear😭😭 grim doesnt work under
#kde because of some protocol stuff and this is the cheap
#fallback method that i came up with...
def _capture_spectacle(output_path: str) -> bool:
    try:
        logger.warning("Attempting fallback using spectacle (╥﹏╥) ...")
        spectacle = subprocess.run(
            ["spectacle", "-r", "-b", "-n", "-o", output_path],
            capture_output=True,
            text=True
        )

        if spectacle.returncode == 0 and os.path.exists(output_path):
            logger.info("OK Successfully captured screen via spectacle (˶˃𐃷˂˶)")
            return True
        return False
    
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.error("Spectacle capture failed: {e}")
        return False

def capture_region(output_path: str = CAPTURE_PATH) -> str | None:
    if os.path.exists(output_path):
        os.remove(output_path)

    if _capture_slurp_grim(output_path):
        return output_path

    #fallback fallback fallback!!
    if _capture_spectacle(output_path):
        return output_path

    logger.error("All capture methods failed or capture was cancelled.")

if __name__ == "__main__":
    result = capture_region()
    if result:
        print(f"Capture saved to: {result}")
    else:
        print("Capture failed or canceled.")