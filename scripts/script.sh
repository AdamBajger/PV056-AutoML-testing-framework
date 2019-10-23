cd ..
source venv/bin/activate
NOW=$(date +"%Y%m%d%H%M%S")
pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"
deactivate
