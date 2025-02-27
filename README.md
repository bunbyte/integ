# File Integrity Checker

This is a web-based tool to ensure the integrity and security of system files by verifying their integrity against known hashes or checksums. The tool generates and stores hashes the first time it receives a file and compares the hash when the file is received again.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **File Upload**: Users can upload files to upload files to the web application.
- **Hash Calculation**: The tool calculates the hash of the uploaded file using SHA-256 by default.
- **Hash Storage**: The tool stores the hash of the file in a JSON file.
- **Integrity Verification**: The tool verifies the integrity of the file by comparing the stored hash with the hash of the re-uploaded file.
- **User Feedback**: The tool provides feedback to the user about the integrity of the file.

## Prerequisites

- Python 3.6 or higher
- Flask
- A web browser

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/file_integrity_checker_web.git
   cd file_integrity_checker_web

   
