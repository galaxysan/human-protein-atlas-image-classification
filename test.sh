python -u test.py \
	-a resnet18 \
	-e \
	--resume model_best.pth.tar \
	-b 1 \
	../data/ | tee tlog18.txt
