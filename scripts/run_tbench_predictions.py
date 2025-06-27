import json
import argparse
from appworld import AppWorld


def main(experiment_name, predictions):
    for pred in predictions:
        task_id = pred['task_id']
        codes = pred['codes']
        with AppWorld(
            task_id=task_id,
            experiment_name=experiment_name,
        ) as world:
            for code in codes:
                print("\n\n" + "%" * 20 + " CODE " + "%" * 20 + "\n" + code)
                # execute the code in the world environment
                output = world.execute(code)
                print("\n\n" + "=" * 20 + " OUTPUT " + "=" * 20 + "\n" + output)
                # stop if agent has committed the task to be complete.
                if world.task_completed():
                    break
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run main function with arguments.")
    parser.add_argument("--experiment-name", type=str, required=True, help="Directory to run")
    parser.add_argument("--prediction-file", type=str, required=True, help="Output file path")

    args = parser.parse_args()

    with open(args.prediction_file, "r") as file:
        predictions = [json.loads(line) for line in file]
    main(args.experiment_name, predictions)