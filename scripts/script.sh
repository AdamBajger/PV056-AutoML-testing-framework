cd ..
source venv/bin/activate
NOW=""
now(){
	NOW=$(date +"%Y%m%d-%H%M%S")
}
now
#{ pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"; } &
wait
now
{ pv056-apply-od-methods -c configs/od/default.json > "scripts/log-$NOW-od.log"; } &
wait
now
pv056-remove-outliers  -c config_remove_outliers_example.json -d datasets.csv &
wait

deactivate
