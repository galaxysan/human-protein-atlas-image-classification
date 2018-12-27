python -u main.py \
       	-a resnet18\
	-j 4 \
	--batch-size 250 \
	--print-freq 1 \
	--evaluate \
	--resume model_best.pth.tar \
	../data/ | tee mlog.txt
