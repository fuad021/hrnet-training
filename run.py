import subprocess

cmd = '../venv/bin/python tools/dist_train.py --cfg experiments/coco/higher_hrnet/w48_640_foot.yaml FP16.ENABLED True FP16.DYNAMIC_LOSS_SCALE True MODEL.SYNC_BN True'
subprocess.Popen(cmd, shell=True, close_fds=True)
 
