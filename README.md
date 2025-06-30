# AppWorld

This branch of the `AppWorld` fork contains code to replicate experiments verifying parity between the original `AppWorld` implementation and its adaptation in [terminal-bench](https://github.com/laude-institute/terminal-bench).

## Overview

To validate the correctness of the AppWorld implementation in `terminal-bench`, we capture the API calls made by the agent during its interaction with the environment. These calls are saved in a JSONL file and evaluated using the original AppWorld harness.

After extracting the API calls using the steps described in the `terminal-bench` [fork](https://github.com/harshraj172/terminal-bench/tree/appworld_comparison), follow the instructions below to run the prediction JSONL file against the original AppWorld framework.

## Steps

Before running the commands below, ensure your `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` is set.

### **Install dependencies and data**

```bash
conda create -n venv python=3.11
pip install appworld
appworld install

# download data
appworld download data
```

### **Run terminal-bench's predicted agent API calls**

```bash
python -m scripts.run_tbench_predictions \
    --experiment-name <experiment_name> \
    --prediction-file <path_to_prediction_jsonl>
```

### **Run Evaluation**

```bash
appworld evaluate <experiment_name> dev
```