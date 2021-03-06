{
  "num_mels": 80,
  "num_freq": 1024,
  "sample_rate": 20000,
  "frame_length_ms": 50.0,
  "frame_shift_ms": 12.5,
  "preemphasis": 0.97,
  "min_level_db": -100,
  "ref_level_db": 20,
  "hidden_size": 128,
  "embedding_size": 256,
  "text_cleaner": "english_cleaners",

  "epochs": 200,
  "lr": 0.01,
  "lr_patience": 2,
  "lr_decay": 0.5,
  "batch_size": 32,
  "griffinf_lim_iters": 60,
  "power": 1.5,
  "r": 5,

  "num_loader_workers": 16,

  "save_step":1 ,
  "data_path": "/data/shared/KeithIto/LJSpeech-1.0",
  "output_path": "result",
  "log_dir": "/home/erogol/projects/TTS/logs/"
}
