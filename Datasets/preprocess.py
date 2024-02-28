from configs import ModelConfigs
import stow

dataset, vocab, max_len = [], set(), 0
for file in stow.ls(stow.join('Datasets', 'captcha_images_v2')):
    dataset.append([stow.relpath(file), file.name])
    vocab.update(list(file.name))
    max_len = max(max_len, len(file.name))

configs = ModelConfigs()

# Save vocab and maximum text length to configs
configs.vocab = "".join(vocab)
configs.max_text_length = max_len
configs.save()