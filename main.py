import os

# Create output directory if it doesn't exist
os.makedirs('/output', exist_ok=True)

# The dad joke
joke = "I told my Wi-Fi I needed space. It disconnected, changed the password, and started seeing the neighbor's router."

# Write to the file
with open('/output/entry.txt', 'w') as f:
    f.write(joke)

print(f"Dad joke written to /output/entry.txt: {joke}")
