import json

# Dummy data representing metadata in various formats (e.g., EXIF, Dublin Core)
dummy_metadata_exif = {
    "Image Width": 1920,
    "Image Height": 1080,
    "Author": "John Doe",
    "Copyright": "2023 Example Inc.",
    # Missing "Creation Date" field
    "Location": "New York City, USA"
}

dummy_metadata_dc = {
    "creator": "Alice White",
    "title": "The Greatest Book Ever",
    # Missing "subject" and "description" fields
    "publisher": "Penguin Random House",
    "date": "2023-08-01"
}


def extract_metadata(metadata_dict, required_fields):
    extracted_metadata = {}

    for field in required_fields:
        mapped_field = field  # Assume direct mapping for simplicity
        value = metadata_dict.get(mapped_field, None)

        if value:
            extracted_metadata[field] = value
        else:
            # Handle missing fields with a default value (if applicable)
            if field == "date_created":
                extracted_metadata[field] = "Unknown"
            elif field == "subject":
                extracted_metadata[field] = ""
            elif field == "location":
                extracted_metadata[field] = "Unknown Location"
            # You can add more cases for other fields if needed
            else:
                # For non-required fields, skip them
                pass

    return extracted_metadata


def transform_metadata(metadata):
    # Perform necessary transformations
    # ...
    if "Creation Date" in metadata:
        metadata["date_created"] = metadata.pop("Creation Date").replace(":", "-")

    if "subject" in metadata:
        metadata["subject"] = ", ".join(metadata["subject"])
    return metadata


def main():
    required_metadata_fields = [
        "title",
        "author",
        "description",
        "date_created",
        "subject",
        "publisher",
        "location"
    ]

    exif_metadata = extract_metadata(dummy_metadata_exif, required_metadata_fields)
    transformed_exif_metadata = transform_metadata(exif_metadata)
    print("Transformed EXIF Metadata:")
    print(json.dumps(transformed_exif_metadata, indent=2))

    dc_metadata = extract_metadata(dummy_metadata_dc, required_metadata_fields)
    transformed_dc_metadata = transform_metadata(dc_metadata)
    print("\nTransformed Dublin Core Metadata:")
    print(json.dumps(transformed_dc_metadata, indent=2))


if __name__ == "__main__":
    main()
