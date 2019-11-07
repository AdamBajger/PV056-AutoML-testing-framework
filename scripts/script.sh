cd ..
source venv/bin/activate
NOW=""
now(){
	NOW=$(date +"%Y%m%d-%H%M%S")
}
#now
#TIMESTAMP_SPLIT="$NOW"
#{ pv056-split-data -c configs/split/default.json -d datasets-split.csv > "scripts/log-$TIMESTAMP_SPLIT-split.log"; } &
#wait
#echo "SPLIT completed $NOW"
#now
#TIMESTAMP_OD="$NOW"
#{ pv056-apply-od-methods -c configs/od/default.json > "scripts/log-$TIMESTAMP_OD-od.log"; } &
#wait
#echo "OD completed $NOW"
now
TIMESTAMP_RM_O="$NOW"
pv056-remove-outliers -c configs/rm_o/default.json -d datasets-rm-o.csv > "scripts/log-$TIMESTAMP_RM_O-rm_o.log"
#wait
echo "RM O completed $NOW"
now
pv056-run-clf -c configs/clf/default.json -d datasets-rm-o.csv > "scripts/log-$NOW-clf.log"
#wait
echo "CLF completed $NOW"
now
pv056-statistics -r clf_outputs/
echo "STATS completed $NOW"



deactivate
