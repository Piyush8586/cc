#!/bin/bash

# Set the filename for storing uptime data
filename="uptime_data.tsv"

# Check if the file exists, if not, create it and add header
if [ ! -e "$filename" ]; then
    echo -e "Timestamp\tUptime" > "$filename"
fi

# Infinite loop to keep updating the uptime every 5 minutes
while true; do
    # Get the current timestamp and uptime
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    uptime=$(uptime -p | cut -d' ' -f2-)

    # Sort the file in descending order of timestamp
    sort -r -o "$filename" "$filename"

    # Append timestamp and uptime to the file
    echo -e "$timestamp\t$uptime" >> "$filename"

    # Wait for 5 minutes
    sleep 300
done
