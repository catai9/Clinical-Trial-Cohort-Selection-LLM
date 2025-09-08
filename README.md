# Clinical Trial Cohort Selection using Large Language Models

### Step 1: Set up conda environment
```bash
conda create -n n2c2 python=3.10 -y
conda activate n2c2
conda install -y pandas numpy scikit-learn tqdm nltk 
conda install -y conda-forge:transformers
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
python3 -m pip install stable-baselines3 
python3 -m pip install sentence-transformers
python3 -m pip install accelerate
python3 -m pip install --upgrade psutil
python3 -m pip install 'shimmy>=2.0'
python3 -m pip install tensorboard
```

### Step 2: Download punkt_tab (if needed)
Note that this was not included in the python scripts to avoid unnecessary checking each time (only needed once).
```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

### Step 3: Connect to Hugging Face for access to the gated repos
Download [Hugging Face CLI](https://huggingface.co/docs/huggingface_hub/en/guides/cli)
Follow the instructions to connect for the model on [Hugging Face](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)


### Step 4: Download data from n2c2 and store in data folder.

### Step 5: Run model inference using the few-shot examples for desired models. 
Example notebooks are provided for:
- mistral-7b-instruct on n2c2-2006 dataset: `mistral-7b-instruct-2006.ipynb`
- mistral-7b-instruct on n2c2-2008 dataset: `mistral-7b-instruct-2008.ipynb`
- gptj-6b on n2c2-2018 dataset: `gptj-6b-2018.ipynb`


