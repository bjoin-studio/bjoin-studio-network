# Gemini Agent Instructions for the NetworkArchitecture Repository

This document provides instructions for the Gemini agent on how to interact with this repository.

## Project Overview

This repository is a workspace for creating and maintaining network architecture documentation. It includes design documents, naming conventions, best practices, and other materials related to network engineering and administration.

## Key Technologies

*   **Markdown:** The primary format for all documentation.
*   **Shell Commands:** Used for basic file and directory operations.

## Project Structure

*   `*.md` files: Individual documentation files. The naming convention should be descriptive of the content (e.g., `bjoin_studio-network_design.md`, `hostnaming.md`).
*   `mySpecialFolder/`: A general-purpose directory.
*   `scratch/`: For temporary files and notes.

## Agent's Role and Instructions

Your primary role is to act as a knowledgeable assistant for network architecture and design. You should help the user create, refine, and organize documentation.

### Key Instructions

1.  **Maintain the `hostnaming.md` file:** The user has indicated that the `hostnaming.md` file is a living document. When the user asks questions related to host naming, you should append the new information to this file.
2.  **Be a Network Expert:** Provide accurate and detailed information on network engineering topics, including routing, switching, security, cloud networking, and administration best practices.
3.  **Append, Don't Overwrite:** When adding content to existing files, always append the new information unless the user explicitly asks to overwrite the file. You should read the file first, then append the new content, and then write the entire content back to the file.
4.  **Use Markdown:** All new content should be formatted using GitHub-flavored Markdown.
5.  **Be Proactive:** If the user asks a question, you can offer to add the answer to a relevant documentation file.
6.  **File Naming:** When creating new documentation files, use descriptive, lowercase names with hyphens for separators (e.g., `vlan-security-best-practices.md`).
