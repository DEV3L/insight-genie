# Insight Genie

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/downloads/)
[![OpenAI Assistants API Beta](https://img.shields.io/badge/OpenAI-Assistants%20API%20Beta-orange)](https://platform.openai.com/docs/assistants/overview)
[![Build Status](https://github.com/DEV3L/insight-genie/actions/workflows/continuous-integration.yml/badge.svg)](https://github.com/DEV3L/insight-genie/actions/workflows/continuous-integration.yml)

Your expert craftsman for software wisdom, agile insights, and leadership.

The full product definition can be found [here](Insight_Genie_Product_Definition.md).

![Insight Genie](data/files/insight_genie.png)

## Table of Contents

- [Introduction](#introduction)
- [Why Insight Genie?](#why-insight-genie)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

**Insight Genie** is a conversational AI platform designed to inspire and generate unique, insightful content. Leveraging advanced Natural Language Processing (NLP), Natural Language Generation (NLG), and Machine Learning (ML) technologies, it transforms data and dialogue into creative content across platforms. Perfect for creatives and professionals in the digital era, Insight Genie redefines content generation by fostering creativity through conversation.

Discover more about the assistant's prompt [here](prompts/prompt.md).

## Why Insight Genie?

In a digital world craving fresh and engaging content, traditional methods often fall short of inspiring true creativity. **Insight Genie** transcends these limitations by using conversational AI to empower users to effortlessly explore and create unique content that resonates on both personal and communal levels.

## Key Features

### 🚀 Content Generation

At the heart of Insight Genie is its ability to generate tailored, AI-crafted content based on your personal knowledge base and topic preferences. Whether you're seeking inspiration or looking to expand on specific ideas, Insight Genie delivers insightful content to meet your needs.

### 📥 Data Extraction and Integration

Enrich your content generation process by integrating knowledge from multiple sources:

- **Twitter**: Analyze tweets and extract meaningful insights.
- **LinkedIn**: Incorporate professional experiences and posts.
- **GitHub**: Summarize codebases and projects.
- **Personal Blogs**: Utilize existing content to generate new ideas.

### 🤖 AI Assistant Management

Leverage the power of OpenAI Assistants to enhance the content generation process. Insight Genie utilizes specialized libraries:

- **[ai-assistant-manager](https://github.com/DEV3L/ai-assistant-manager)**: Manages OpenAI Assistants, including creating, listing, and deleting assistants, as well as handling vector stores and retrieval files.
- **[ai-code-summary](https://github.com/DEV3L/ai-code-summary)**: Automates the summarization of code files into markdown format, leveraging GPT models for concise summaries.

### 🖼️ Image Analysis and Description

Process and analyze images to extract valuable information:

- Generate descriptions of images from tweets or other sources.
- Use AI to interpret diagrams, charts, and other visual content.

### 👥 Collaborative Creativity and Feedback Integration

Foster a dynamic and inventive community by collaborating with other users. Incorporate feedback into the AI's creative process to continuously improve content generation and encourage shared creativity.

### 📈 Analytics and Insight Generation

Gain valuable insights into the performance of your generated content, including:

- **Engagement Metrics**
- **Reach Analysis**
- **Impact Assessment**

Use this data to refine your content strategies and make informed decisions based on real-world analytics.

## Technology Stack

Insight Genie leverages cutting-edge technologies to deliver an unparalleled content creation experience:

- **Python 3.11+**: The core programming language.
- **Natural Language Processing (NLP)**
- **Natural Language Generation (NLG)**
- **Machine Learning (ML)**
- **OpenAI Assistants API**
- **APIs for Dynamic Data Retrieval**

### Integrations

- **[ai-assistant-manager](https://github.com/DEV3L/ai-assistant-manager)**: Simplifies the management of OpenAI Assistants.
- **[ai-code-summary](https://github.com/DEV3L/ai-code-summary)**: Automates the summarization of codebases into markdown files.

## Installation

Follow these steps to set up Insight Genie on your local machine:

### Prerequisites

- **Python 3.11 or higher**: Ensure you have the correct Python version installed. You can download it [here](https://www.python.org/downloads/).
- **OpenAI API Key**: Obtain your OpenAI API key from the [OpenAI platform](https://platform.openai.com/).

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DEV3L/insight-genie.git
   cd insight-genie
   ```

2. **Set up environment variables:**

   Copy the `env.local` file to `.env` and replace `OPENAI_API_KEY` with your actual OpenAI API key:

   ```bash
   cp env.local .env
   ```

3. **Install Hatch:**

   Insight Genie uses [Hatch](https://hatch.pypa.io/latest/) for environment management and packaging.

   ```bash
   pip install hatch
   ```

4. **Set up a virtual environment and install dependencies:**

   ```bash
   hatch env create
   hatch shell
   ```

   This will create and activate a virtual environment and install all project dependencies as specified in `pyproject.toml`.

## Usage

### Running the Chat Interface

Start interacting with Insight Genie using the chat interface:

```bash
hatch run chat
```

This command runs the `run_chat.py` script, which initializes the assistant and starts a chat session.

### Building the Assistant

If you need to build or rebuild the assistant (e.g., after updating the persona or prompt), run:

```bash
hatch run build
```

This command executes the `run_build.py` script to set up the assistant.

### Generating Code Summaries

To generate a markdown summary of your codebase using `ai-code-summary`, run:

```bash
hatch run summary .
```

This will create a comprehensive markdown file (`ai-code-summary.md`) summarizing your code, which can be used within Insight Genie or for documentation purposes.

### Processing Twitter Events

To process Twitter data and generate event-based insights, run:

```bash
hatch run process-twitter-events
```

This script processes tweets, extracts events, and generates markdown summaries with image descriptions and author information.

## Testing

### Running Tests

Insight Genie includes comprehensive unit and integration tests to ensure reliability and maintainability.

- **Unit Tests** (excluding integration tests):

  ```bash
  hatch run test
  ```

- **Integration Tests** (including tests that hit external systems):

  ```bash
  hatch run test-integration
  ```

### Coverage Reports

Generate coverage reports to assess test coverage:

```bash
hatch run test -- --cov
```

For coverage gutters (useful with code editors like VSCode):

```bash
hatch run test -- --cov --cov-report lcov
# In your editor, activate coverage gutters to visualize code coverage.
```

### Static Type Checking

Run static type checking with Pyright:

```bash
hatch run pyright
```

## Contributing

We welcome contributions from the community! Please follow these steps:

1. **Fork the repository** on GitHub.

2. **Create a new branch** for your feature or bug fix:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Commit your changes** with clear and descriptive messages.

4. **Push to your branch** on your forked repository:

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create a Pull Request** to the `main` branch of the original repository.

If you encounter any issues or have suggestions, feel free to open an issue on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **[ai-assistant-manager](https://github.com/DEV3L/ai-assistant-manager)**: For providing tools and services to manage OpenAI Assistants.
- **[ai-code-summary](https://github.com/DEV3L/ai-code-summary)**: For automating codebase summarization.
- **OpenAI**: For providing powerful AI models and APIs.

---

By integrating the **`ai-assistant-manager`** and **`ai-code-summary`** libraries, Insight Genie enhances its capabilities in AI assistant management and code summarization. This allows users to not only generate insightful content but also to maintain and understand their codebases more effectively.

### Additional Resources

- **[Prompt](prompts/prompt.md)**: View the prompt that defines the assistant's behavior.
- **[ai-assistant-manager Documentation](https://github.com/DEV3L/ai-assistant-manager)**: Learn how to use `ai-assistant-manager` to manage your AI assistants efficiently.
- **[ai-code-summary Documentation](https://github.com/DEV3L/ai-code-summary)**: Understand how to generate code summaries.

---

Feel free to explore the capabilities of Insight Genie and contribute to its growth. With its advanced AI features and integrations, it's poised to revolutionize the way we approach content creation and code understanding.

## Project Structure

The project is organized as follows:

- `data/`: Contains data used by the project, including images, prompts, and exported data.
- `insight_genie/` or root directory: Contains the source code of the project.
  - `assistants/`: Manages assistant services with `AssistantService`.
  - `chats/`: Handles chat interactions with `Chat`.
  - `clients/`: Contains API client implementations.
  - `exporters/`: Manages data exporting from various sources like Twitter and books.
  - `prompts/`: Stores prompt templates for the assistant.
  - `tests/`: Contains unit and integration tests.
- `run_chat.py`: Main script to start a chat session.
- `run_build.py`: Script to build or rebuild the assistant.
- `run_code_summary.py`: Script to generate code summaries.
- `run_process_twitter_events.py`: Script to process Twitter events.
- `.github/workflows/`: Contains GitHub Actions workflows for CI/CD.
- `pyproject.toml`: Configuration file for project dependencies, scripts, and tools.
