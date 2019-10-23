cd ..
source venv/bin/activate
NOW=""
now(){
	NOW=$(date +"%Y%m%d%H%M%S")
}
now
# pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"
now
pv056-apply-od-methods -c config/od/default.json > "scripts/log-$NOW-od.log"
deactivate
