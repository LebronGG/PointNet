i=6
#python train.py --log_dir log${i} --test_area ${i} --batch_size 32 --max_epoch 200
#python batch_inference.py --model_path log${i}/model.ckpt --dump_dir log${i}/dump --output_filelist log${i}/output_filelist.txt --room_data_filelist meta/area${i}_data_label.txt --visu
python batch_inference.py --model_path log${i}/model.ckpt --dump_dir log${i}/dump --output_filelist log${i}/output_filelist.txt --room_data_filelist meta/area6_data_label.txt --visu
python eval_iou_accuracy.py --test_area ${i}