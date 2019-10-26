cd ..
source venv/bin/activate
NOW=""
now(){
	NOW=$(date +"%Y%m%d-%H%M%S")
}
now
#{ pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"; } &
wait
echo "SPLIT completed $NOW"
now
{ pv056-apply-od-methods -c configs/od/default.json > "scripts/log-$NOW-od.log"; } &
wait
echo "OD completed $NOW"
now
{ pv056-remove-outliers  -c configs/rm_o/default.json -d datasets.csv & > "scripts/log-$NOW-rm_o.log"; } &
wait
echo "RM O completed $NOW"
now

{  } &
deactivate
