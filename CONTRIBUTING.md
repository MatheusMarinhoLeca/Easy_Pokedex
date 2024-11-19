
# Contributing to the Easy Pokédex Project

Thank you for visiting the Easy Pokédex repository and for your interest in collaborating on the project. The primary goal of this project is educational: We are applying the open-source principles taught in ENSF 619 L07, using Pokémon as the subject matter for our application. This document exists to help foster collaboration and set expectations for how to contribute to the project.

<a name="before-you-start"></a>
## Before you start...
Everything in this repository is made available under the MIT License. You are welcome to submit feature requests, report issues, and participate in discussions. However, we can only accept contributions if you agree to release them under the MIT License.

## Ways to Contribute
There are numerous ways to contribute to this project, irrespective of your level of technical expertise or interest in Pokémon. We’ll outline the details and guidelines for each contribution method below.

## Table Of Contents
- **[Feature requests](#feature-requests)**
- **[Bug reports](#bug-reports)**
- **[Code contributions](#code-contributions)**
- **[Coding Style Guidelines](#coding-style-guidelines)**
- **[Documentation contributions](#documentation-contributions)**
- **[Art, design, and creative input](#art-design-creative-input)**
- **[Environment setup](#environment-setup)**
- **[Code of Conduct](#code-of-conduct)**
- **[OSS Component Use Policy Block List](#oss-component-use-policy-block-list)**

<a name="feature-requests"></a>
### Feature requests
If you have an idea for a feature you would like to see in the Easy Pokédex, feel free to [open an issue](https://github.com/MatheusMarinhoLeca/Easy_Pokedex/issues) in this GitHub repository. As an agile project, we strive to provide value. Once an issue is submitted, we will likely need to discuss and clarify the feature request via comments to refine and clarify the intent, scope, and value of the feature. Precisely articulating your original feature request will help reduce the back-and-forth necessary to evaluate the story for implementation.

<a name="bug-reports"></a>
### Bug reports
The distinction between a feature and a bug can sometimes be tricky. While a feature generally refers to a request for new functionality, a bug is related to existing functionality that is not working as intended. In order to better evaluate the bug for a fix, it is extremely helpful to follow the format below:

#### Expected behavior
Describe how you, as a user or technical evaluator, would expect the application to behave. Defining your expectations as a user can help to expose usability problems with the application. If you discover a bug, we warmly welcome you to [open an issue](https://github.com/MatheusMarinhoLeca/Easy_Pokedex/issues) in this GitHub repository, unless it is a [security bug](#security-bugs) that could be exploited and is not suitable for public collaboration.

#### Actual behavior
Describe what actually happens when you use the application in a way that doesn't meet your expectations.

#### Steps to reproduce
Provide detailed steps to reproduce the bug. The more precise and detailed your steps are, the more likely we will be able to fix the bug.

#### Security bugs
If you discover a security vulnerability in the application that can be exploited, please follow our security reporting process instead of submitting a public issue.
**TODO: Add more detail after setting up security policy on GitHub**

<a name="code-contributions"></a>
### Code contributions
If you want to contribute code, follow these steps:

#### Open an issue, if applicable
If you want to propose a new feature or work on an item that is not yet an issue, you can [open an issue](https://github.com/MatheusMarinhoLeca/Easy_Pokedex/issues) in this GitHub repository.

#### Fork the repository
To work on your changes, fork this repository into your own account.

#### Develop the feature
Once you’ve forked the repo, you can work on your contribution. Commit frequently and follow the [coding standards](#coding-standards) below.

<a name="coding-standards"></a>
### Coding standards
Follow consistent conventions throughout the codebase to make it more maintainable. 

##### Tests
Always cover your code with meaningful tests.

##### Code style
Ensure that your code is clean, concise, and adheres to the project's coding style. Avoid unnecessary complexity and repetition.

##### Commit messages
When squashing commits, write meaningful commit messages. [This guide from cbeams](https://cbea.ms/git-commit/) is a great resource on crafting quality commit messages.

<a name="coding-style-guidelines"></a>
### Coding Style Guidelines

For this project, we follow the [Google Python Style Guide](https://code.google.com/archive/p/soc/wikis/PythonStyleGuide.wiki). Please ensure your code adheres to these guidelines to maintain consistency and readability.

<a name="documentation-contributions"></a>
### Documentation contributions
If you have suggestions to improve documentation, whether it's fixing typos or creating a new Wiki category, feel free to contribute.

<a name="art-design-creative-input"></a>
### Art, design, and creative input
If you have design or creative ideas, you can [open an issue](https://github.com/MatheusMarinhoLeca/Easy_Pokedex/issues) for it. We welcome all contributions but ensure that your work aligns with the repository's standards.

<a name="environment-setup"></a>
### Environment Setup
To contribute code or run the project locally, you’ll need to set up your development environment. This project is written in Python, so ensure you have the required version installed. Follow these steps:

#### Prerequisites
- Python 3.x
- Pip (Python package manager)
- Virtual environment (recommended for isolated Python environments)

#### Setup Instructions

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/MatheusMarinhoLeca/Easy_Pokedex.git
   ```

2. **Create a virtual environment**:  
   In the project’s root directory, create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:  
   Install the required dependencies using `pip`:
   ```bash
   pip install -e '.[dev]'
   ```

4. **Run the application**:  
   To run the application locally, use:
   ```bash
   easy-pokedex
   ```

5. **Run the tests**:  
   To run the test suite and ensure everything is functioning:
   ```bash
   cd tests
   pytest -s -v
   ```

6. **Deactivate the virtual environment**:  
   When you’re done working, you can deactivate the virtual environment:
   ```bash
   deactivate
   ```

For any environment-specific issues or clarifications, feel free to open an issue or check the documentation.

<a name="code-of-conduct"></a>
### Code of Conduct

We are committed to fostering a welcoming and inclusive environment for all contributors. To help us achieve that, please adhere to the following code of conduct:

1. **Be respectful**: Treat everyone with kindness and respect. Personal attacks, harassment, or discriminatory language will not be tolerated.
2. **Be constructive**: When providing feedback, ensure that it is constructive and delivered in a respectful manner. Be open to feedback on your own work.
3. **Collaborate**: Help others when you can, and ask for help when you need it. Collaboration is key to the success of this project.
4. **Stay on topic**: Keep discussions focused on the project and its goals. Avoid irrelevant tangents that distract from the work.
5. **No discrimination**: We will not tolerate discrimination based on race, gender, age, sexual orientation, religion, or any other personal attribute.

Failure to adhere to this Code of Conduct may result in consequences, including removal from the project. If you experience or witness any violations of this Code of Conduct, please report them to the maintainers via direct message or email.

<a name="oss-component-use-policy-block-list"></a>
### OSS Component Use Policy Block List

When contributing to the Easy Pokédex project, it's important to adhere to the Open Source Software (OSS) component policy. To ensure compliance with this policy, we maintain a list of OSS components that should not be used in this project due to licensing, security, or other restrictions.

### Block List

1. **GPL-licensed software**: Any software under the GNU General Public License (GPL) is prohibited due to incompatibility with our MIT License.
2. **Unmaintained or deprecated libraries**: Any libraries that are no longer maintained or officially deprecated should be avoided to ensure long-term stability.
3. **Known vulnerable libraries**: Libraries with known security vulnerabilities that have not been patched or are not actively maintained should not be included.
4. **Closed-source or proprietary dependencies**: Dependencies that are not open-source or require proprietary licenses should not be used.

If you are unsure whether a specific OSS component falls under the block list, please raise the question in an issue before proceeding with its use in the project.

---

By contributing to this project, you agree to abide by this Code of Conduct, the OSS Component Use Policy Block List, and the Coding Style Guidelines.
