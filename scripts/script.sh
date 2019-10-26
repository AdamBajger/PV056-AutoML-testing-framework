cd ..
source venv/bin/activate
NOW=""
now(){
	NOW=$(date +"%Y%m%d-%H%M%S")
}
now
<<<<<<< HEAD
pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"
wait
now
pv056-apply-od-methods -c configs/od/default.json > "scripts/log-$NOW-od.log"
=======
# pv056-split-data -c configs/split/default.json -d datasets.csv > "scripts/log-$NOW-split.log"
wait
now
pv056-apply-od-methods -c config/od/default.json > "scripts/log-$NOW-od.log"
>>>>>>> bc1946861b0d2e6447fd02fb2d542554796caa80
wait
deactivate
