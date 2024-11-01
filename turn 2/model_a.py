import json

def extract_metadata(metadata_dict, required_fields):
	extracted_metadata = {}

	for field in required_fields:
		mapped_field = field  # Assume direct mapping for simplicity
		value = metadata_dict.get(mapped_field, None)

		if value:
			extracted_metadata[field] = value
		else:
			extracted_metadata[field] = ""  # Provide default empty string for missing fields

	return extracted_metadata

def transform_metadata(metadata):
	if "Creation Date" in metadata:
		metadata["date_created"] = metadata.pop("Creation Date").replace(":", "-")

	if "subject" in metadata:
		metadata["subject"] = ", ".join(metadata["subject"])

	# Add handling for missing fields here if needed, e.g., logging or setting default values

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

	dummy_metadata_exif = {
		"Image Width": 1920,
		"Image Height": 1080,
		"Author": "John Doe",
		"Copyright": "2023 Example Inc.",
		"Location": "New York City, USA"
	}

	dummy_metadata_dc = {
		"creator": "Alice White",
		"title": "The Greatest Book Ever",
		"subject": ["Science", "Fiction"],
		"publisher": "Penguin Random House",
		"date": "2023-08-01"
	}

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
