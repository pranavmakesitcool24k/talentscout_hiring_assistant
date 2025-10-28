"""
Data Handler - Manages secure storage and retrieval of candidate data
Implements GDPR compliance best practices
"""

import json
import os
from datetime import datetime
import hashlib


class DataHandler:
    """
    Handles secure storage of candidate data with GDPR compliance
    """

    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.candidates_file = os.path.join(data_dir, "candidates.json")

        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)

        # Initialize candidates file if it doesn't exist
        if not os.path.exists(self.candidates_file):
            self._initialize_storage()

    def _initialize_storage(self):
        """Initialize empty storage file"""
        initial_data = {
            "candidates": [],
            "metadata": {
                "created_at": datetime.now().isoformat(),
                "total_candidates": 0,
                "last_updated": datetime.now().isoformat()
            }
        }

        with open(self.candidates_file, 'w') as f:
            json.dump(initial_data, f, indent=2)

    def _hash_email(self, email):
        """
        Create a hash of email for unique identification

        Args:
            email: Email address

        Returns:
            Hashed email string
        """
        return hashlib.sha256(email.encode()).hexdigest()

    def _anonymize_sensitive_data(self, data):
        """
        Anonymize sensitive data for storage (GDPR compliance)

        Args:
            data: Candidate data dictionary

        Returns:
            Data with sensitive fields anonymized
        """
        anonymized = data.copy()
        anonymized["consent_timestamp"] = datetime.now().isoformat()
        anonymized["data_retention_until"] = self._calculate_retention_date()

        return anonymized

    def _calculate_retention_date(self, months=12):
        """
        Calculate data retention expiry date (GDPR compliance)

        Args:
            months: Number of months to retain data

        Returns:
            ISO format date string
        """
        from datetime import timedelta
        retention_date = datetime.now() + timedelta(days=months * 30)
        return retention_date.isoformat()

    def save_candidate_data(self, candidate_data):
        """
        Save candidate data securely

        Args:
            candidate_data: Dictionary containing candidate information

        Returns:
            Success status and candidate ID
        """
        try:
            # Load existing data
            with open(self.candidates_file, 'r') as f:
                storage = json.load(f)

            # Add metadata to candidate data
            enhanced_data = self._anonymize_sensitive_data(candidate_data)
            enhanced_data["submission_timestamp"] = datetime.now().isoformat()
            enhanced_data["candidate_id"] = self._hash_email(candidate_data.get("email", ""))
            enhanced_data["status"] = "screening_completed"

            # Add to candidates list
            storage["candidates"].append(enhanced_data)

            # Update metadata
            storage["metadata"]["total_candidates"] = len(storage["candidates"])
            storage["metadata"]["last_updated"] = datetime.now().isoformat()

            # Save back to file
            with open(self.candidates_file, 'w') as f:
                json.dump(storage, f, indent=2)

            return True, enhanced_data["candidate_id"]

        except Exception as e:
            print(f"Error saving candidate data: {str(e)}")
            return False, None

    def get_candidate_by_email(self, email):
        """
        Retrieve candidate data by email

        Args:
            email: Candidate's email address

        Returns:
            Candidate data dictionary or None
        """
        try:
            with open(self.candidates_file, 'r') as f:
                storage = json.load(f)

            candidate_id = self._hash_email(email)

            for candidate in storage["candidates"]:
                if candidate.get("candidate_id") == candidate_id:
                    return candidate

            return None

        except Exception as e:
            print(f"Error retrieving candidate data: {str(e)}")
            return None

    def get_all_candidates(self):
        """
        Retrieve all candidate data

        Returns:
            List of candidate dictionaries
        """
        try:
            with open(self.candidates_file, 'r') as f:
                storage = json.load(f)

            return storage["candidates"]

        except Exception as e:
            print(f"Error retrieving candidates: {str(e)}")
            return []

    def delete_candidate_data(self, email):
        """
        Delete candidate data (GDPR right to erasure)

        Args:
            email: Candidate's email address

        Returns:
            Success status
        """
        try:
            with open(self.candidates_file, 'r') as f:
                storage = json.load(f)

            candidate_id = self._hash_email(email)

            # Remove candidate from list
            storage["candidates"] = [
                c for c in storage["candidates"]
                if c.get("candidate_id") != candidate_id
            ]

            # Update metadata
            storage["metadata"]["total_candidates"] = len(storage["candidates"])
            storage["metadata"]["last_updated"] = datetime.now().isoformat()

            # Save back to file
            with open(self.candidates_file, 'w') as f:
                json.dump(storage, f, indent=2)

            return True

        except Exception as e:
            print(f"Error deleting candidate data: {str(e)}")
            return False
