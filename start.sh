python -u main.py \
       	-a resnet18\
	-j 4 \
	--epochs 400 \
	--batch-size 50 \
	--print-freq 1 \
	../data/ | tee mlog18.txt
