from sentino_api.client import SentinoClient
import matplotlib.pyplot as plt

# Replace with your actual API token
API_TOKEN = "2df5b46fc1589e6c3ddd5a0fe8678d4956ea1009"

# Initialize client
client = SentinoClient(API_TOKEN)

# Test 1: Get inventories
print("Testing get_inventories()")
inventories = client.get_inventories()
print(f"Found {len(inventories)} inventories")
print()

# Test 2: Score text and convert to DataFrame
print("Testing score_text() and DataFrame conversion")
text = "I love meeting new people and going to parties. I'm organized and always on time."

result = client.score_text(text, inventories=["big5"])
print("Raw results:")
print(result)
print()

# Convert to DataFrame
df = client.results_to_dataframe(result, inventory="big5")
print("DataFrame:")
print(df)
print()
print("DataFrame info:")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

# Test 3: Visualization
print("Creating visualization")
fig = client.plot_traits(result, inventory="big5")
plt.show()