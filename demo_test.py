from sentino_api.client import SentinoClient
import matplotlib.pyplot as plt

API_TOKEN = "2df5b46fc1589e6c3ddd5a0fe8678d4956ea1009"

# Initialize client
client = SentinoClient(API_TOKEN)

# Analyze all demo samples
results = client.analyze_demo(inventory="big5")

# Display results for each person
for person in results:
    print(f"-{person['name']}-")
    print(f"Text: {person['text']}")
    print("\nPersonality Scores:")
    print(person['dataframe'])
    print("\n")

# Create visualizations for all three people
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, person in enumerate(results):
    df = person['dataframe']

    bars = axes[i].bar(df['trait'], df['score'])

    # Color bars
    for j, score in enumerate(df['score']):
        if score > 0:
            bars[j].set_color('steelblue')
        else:
            bars[j].set_color('coral')

    axes[i].set_title(person['name'], fontweight='bold')
    axes[i].set_ylim(-1.5, 1.5)
    axes[i].axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
    axes[i].tick_params(axis='x', rotation=45)
    axes[i].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Comparison
comparison = client.compare_profiles(results, inventory="big5")
print(comparison)
print()

# Show which person scores highest on each trait
for col in comparison.columns:
    if col != "name":
        max_idx = comparison[col].idxmax()
        max_person = comparison.loc[max_idx, "name"]
        max_score = comparison.loc[max_idx, col]
        print(f"{col.capitalize()}: {max_person} ({max_score:.2f})")