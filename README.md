# Language Model Experimentation Tool

This repository houses a Python script named `experiment.py` that leverages the `ollama` package for engaging with a language model (LM). The script is designed for anyone interested in exploring how LMs can be queried, how they process complex questions, and how they evaluate and generate responses.

## Key Features

- **Query Interaction**: Directly interact with a language model by sending queries and receiving answers.
- **Complexity Determination**: Before answering, the script evaluates the complexity of a query.
- **Thought Process Emulation**: Mimics a step-by-step thought process for tackling intricate questions.
- **Response Evaluation**: Compares and rates responses based on predefined criteria for quality.

## Prerequisites

Ensure you have the following installed:

- Python version 3.x or higher
- The `ollama` package, properly installed and configured within your Python environment

## How to Use

### Standard Mode

Run the script in a terminal. You'll be prompted to enter your questions and specify how many responses you'd like to compare:

```bash
python experiment.py
```

### Detailed Output Mode

For insights into the question's complexity, thought steps, and answer ratings, activate the verbose mode:

```bash
python experiment.py --verbose
```

## Behind the Scenes

- **Complexity Assessment**: Initially, the script assesses the question's complexity to adapt its approach.
- **Thought Process Simulation**: Depending on the complexity, it simulates thought steps for a thorough analysis.
- **Response Generation**: Leverages the simulated thought process to craft an answer.
- **Answer Ranking**: When multiple answers are generated, it ranks them to highlight the top response.

## Quick Start Example

1. Execute the script in verbose mode:
   ```bash
   python experiment.py --verbose
   ```
2. When prompted, type your question.
3. Specify how many responses you want for comparison.

The script will guide you through its thinking and answering process, providing insights and evaluations in verbose mode.

## Contributing

Contributions are welcome! Fork this project and submit a pull request with your enhancements or fixes.

## License

This project is released under the MIT license. For more details, refer to the LICENSE file.
