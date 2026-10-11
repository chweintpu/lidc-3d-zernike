"""Run the continuous point-sampled synthetic experiment (not CT voxel analysis)."""
import os, subprocess, sys
from pathlib import Path
root=Path(__file__).resolve().parent
env=os.environ.copy()
env.setdefault("LIDC_PROJECT_ROOT",str(root))
subprocess.run([sys.executable,str(root/"portable"/"run_zernike_surface_vs_volume_matched_FULL_v2.py")],env=env,check=True)
