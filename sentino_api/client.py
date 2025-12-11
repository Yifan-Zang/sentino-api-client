import requests
import pandas as pd
import matplotlib.pyplot as plt
from .demo_data import SAMPLE_TEXTS

class SentinoClient:
    """Client for interacting with the Sentino Personality API."""

    def __init__(self, api_token):
        """Initialize the client with an API token

        Args:
            api_token (str): Sentino API token
        """
        self.api_token = api_token
        self.base_url = "https://api.sentino.org/api"
        self.headers = {
            "Authorization": f"Token {api_token}",
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint, method="GET", data=None):
        """Make a request to the API.

        Args:
            endpoint (str): API endpoint path
            method (str): HTTP method (GET or POST)
            data (dict): Data to send with POST requests

        Returns:
            dict: JSON response from the API
        """
        url = f"{self.base_url}/{endpoint}"

        if method == "GET":
            response = requests.get(url, headers=self.headers)
        elif method == "POST":
            response = requests.post(url, headers=self.headers, json=data)

        response.raise_for_status()  # Raise error
        return response.json()

    def get_inventories(self):
        """Get list of available personality inventories

        Returns:
            list: List of available inventories with IDs and references
        """
        return self._make_request("inventories", method="GET")

    def score_text(self, text, inventories=None):
        """Score personality traits from text

        Args:
            text (str): Text data
            inventories (list): List of inventories ("big5")

        Returns:
            dict: JSON response with personality scores
        """
        if inventories is None:
            inventories = ["big5"]

        data = {
            "text": text,
            "inventories": inventories
        }

        return self._make_request("score/text", method="POST", data=data)

    def results_to_dataframe(self, results, inventory="big5"):
        """Convert scoring results to a pandas DataFrame

        Args:
            results (dict): Results from score_text()
            inventory (str): Which inventory (default "big5")

        Returns:
            pandas.DataFrame: DataFrame format
        """
        scoring = results.get("scoring", {}).get(inventory, {})

        rows = []
        for trait, values in scoring.items():
            rows.append({
                "trait": trait,
                "score": values.get("score"),
                "quantile": values.get("quantile"),
                "confidence": values.get("confidence"),
                "confidence_text": values.get("confidence_text")
            })

        return pd.DataFrame(rows)

    def plot_traits(self, results, inventory="big5", save_path=None):
        """Will create a bar chart of personality trait scores

        Args:
            results (dict): Results from score_text()
            inventory (str): Which inventory to plot (default: "big5")
            save_path (str): Path to save the result

        Returns:
            visualization
        """
        df = self.results_to_dataframe(results, inventory)

        fig, ax = plt.subplots(figsize=(10, 6))

        # Create bar chart
        bars = ax.bar(df['trait'], df['score'])

        # Color bars based on score (positive = blue, negative = red)
        for i, score in enumerate(df['score']):
            if score > 0:
                bars[i].set_color('steelblue')
            else:
                bars[i].set_color('coral')

        ax.set_xlabel('Personality Trait', fontsize=12)
        ax.set_ylabel('Score', fontsize=12)
        ax.set_title(f'{inventory.upper()} Personality Profile', fontsize=14, fontweight='bold')
        ax.set_ylim(-1.5, 1.5)
        ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
        ax.grid(axis='y', alpha=0.3)

        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        if save_path:
            plt.savefig(save_path)

        return fig

    def analyze_demo(self, inventory="big5"):
        """Analyze demo texts and return personalities

        Args:
            inventory (str): Which inventory to use (default: "big5")

        Returns:
            list: name, text, results, and dataframe
        """
        results = []

        for sample in SAMPLE_TEXTS:
            result = self.score_text(sample["text"], inventories=[inventory])
            df = self.results_to_dataframe(result, inventory=inventory)

            results.append({
                "name": sample["name"],
                "text": sample["text"],
                "results": result,
                "dataframe": df
            })

        return results

    def compare_profiles(self, results_list, inventory="big5"):
        """Compare personality with multiple people

        Args:
            results_list (list): List of result
            inventory (str): inventory compare

        Returns:
            pandas.DataFrame: Comparison table
        """
        comparison_data = []

        for item in results_list:
            name = item.get("name", "Unknown")
            df = item["dataframe"]

            row = {"name": name}
            for _, trait_row in df.iterrows():
                row[trait_row["trait"]] = trait_row["score"]

            comparison_data.append(row)

        return pd.DataFrame(comparison_data)