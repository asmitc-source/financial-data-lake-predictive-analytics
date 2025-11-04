from pathlib import Path
import subprocess

def run(cmd):
    assert subprocess.call(cmd, shell=True) == 0

def test_end_to_end():
    run('python -m src.etl')
    run('python -m src.features')
    assert Path('data/processed/features.csv').exists()
    run('python -m src.train')
    assert Path('data/processed/metrics.json').exists()
