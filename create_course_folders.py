#!/usr/bin/env python3
import os

def create_course_folders():
    # List of section names from the course
    sections = [
        "Section 1: Introduction",
        "Section 2: Container Introduction",
        "Section 3: Docker essentials for beginners",
        "Section 4: Docker Networking",
        "Section 5: Docker compose and Multi container",
        "Section 6: Docker quiz time",
        "Section 7: Introduction to Kubernetes",
        "Section 8: Kubernetes for developers",
        "Section 9: Kubernetes Storage",
        "Section 10: Google Kubernetes Engine - Managed Kubernetes",
        "Section 11: Azure Kubernetes Service - Managed Kubernetes",
        "Section 12: Amazon Elastic Kubernetes Service - EKS"
    ]
    
    # Create each folder
    for section in sections:
        # Create folder name (use the section name as is)
        folder_name = section
        
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")
        else:
            print(f"Folder already exists: {folder_name}")

if __name__ == "__main__":
    print("Creating course section folders...")
    create_course_folders()
    print("Done!")
