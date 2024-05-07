# Project Title: Retriever-Augmented Generation (RAG) System for Research Papers

## Description
This project implements a Retriever-Augmented Generation (RAG) system using GPT-4 and Pinecone to assist researchers in quickly accessing up-to-date information on research papers. It dynamically combines the generative capabilities of GPT-4 with real-time data retrieval, ensuring responses are both current and relevant.

## Features
- **Local Documents**: Dynamically pulls information from your local pdf document.
- **GPT-4 Integration**: Utilizes the advanced generative capabilities of GPT-4 for creating coherent and contextually relevant answers.
- **Pinecone Vector Storage**: Employs Pinecone for efficient and scalable vector storage to manage the retrieval process.

## Installation

Follow these steps to set up the project environment and run the system locally.

### Prerequisites
Ensure you have Python 3.8 or higher installed on your machine. You can check your Python version by running:
```bash
python --version
```
### Create a virtual environment
To create a virtual environment and activate it, run the following commands:
```bash
python -m venv venv
```
### Activate the virtual environment
**On Windows**
```bash
venv\\Scripts\\activate
```
**On Unix or MacOS**
```bash
source venv/bin/activate
```
### Installing Dependencies
Install all required dependencies by running:
```bash
pip install -r requirements.txt
```
## Contributing
We welcome contributions to this project! Please feel free to fork the repository, make your changes, and submit a pull request.


## Contact
For any queries or further information, please reach out via GitHub issues or email.

### Acknowledgments
- OpenAI for GPT-4
- Pinecone for vector storage solutions
