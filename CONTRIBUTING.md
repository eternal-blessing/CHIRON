# Contributing to Chiron

Thank you for your interest in contributing to **Chiron**! We welcome contributions of all kinds, including code, documentation, bug reports, feature requests, and improvements.

This document outlines the guidelines and best practices to help you contribute smoothly and efficiently.



## How to Contribute

### 1. Reporting Issues and Requesting Features

- Before submitting a bug report or feature request, please check the existing [issues](https://github.com/eternal-blessing/CHIRON/issues) to avoid duplicates.
- When reporting a bug, provide a clear and concise description, including:
  - Steps to reproduce the issue
  - Expected and actual behavior
  - Your system environment (OS, Python version, hardware specs)
- For feature requests, describe the problem, proposed solution, and potential use cases.

### 2. Development Setup

To begin development on Chiron:

1. Fork the repository and clone your fork locally.

    
    git clone https://github.com/eternal-blessing/CHIRON.git
    cd CHIRON
    

2. Create and activate a virtual environment:

    
    python3 -m venv venv
    source venv/bin/activate   
    

3. Install dependencies:

    
    pip install -r requirements.txt
    

4. Run the application to ensure your environment is correctly configured:

    
    python main.py
    

### 3. Coding Guidelines

- Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions for all Python code.
- Write clear, maintainable, and well-documented code. Include docstrings for all public functions, classes, and modules.
- Organize code modularly based on project structure:
  - `chiron_core.py` — core application logic
  - `webcam_interface.py` — video capture
  - `gesture_processing.py` — gesture recognition pipeline
  - `game_integration.py` — keyboard input simulation
  - `config_manager.py` — configuration management
- Write unit and integration tests for new features or bug fixes. Ensure all tests pass before submitting.

### 4. Making Changes

- Commit your changes with clear, concise commit messages using [Conventional Commits]style, e.g.:

    
    feat(gesture_processing): add support for dynamic swipe gestures
    fix(webcam_interface): handle webcam initialization errors gracefully
    docs(README): update installation instructions
    

- Push your branch to your fork and open a Pull Request (PR) against the `main` branch.
- Include a detailed description of your changes, referencing any relevant issues.

### 5. Review Process

- PRs will be reviewed by project maintainers for code quality, completeness, and adherence to guidelines.
- Be responsive to feedback and prepared to make improvements or adjustments as requested.
- Large or complex changes should be discussed with maintainers early via an issue or pull request.



## Code of Conduct

By contributing to this project, you agree to abide by the [Contributor Covenant Code of Conduct]. 
We expect all participants to foster a welcoming, respectful, and inclusive community.


## Additional Resources

- For usage and development details, see the [README.md](./README.md) and [Documentation](./docs/README.md).



Thank you for helping make **Chiron** better! We look forward to your contributions.

