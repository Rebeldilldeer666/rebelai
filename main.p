from datetime import datetime
import json
import logging
import sys

# -------------------------------------------------------------------
# 1. SETUP & LOGGING CONFIGURATION
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("data_workflow.log"),
        logging.StreamHandler(sys.stdout),
    ],
)


# -------------------------------------------------------------------
# 2. EXTRACT STAGE
# -------------------------------------------------------------------
def extract_data(source_path: str) -> list[dict]:
    """Fetches raw data from an API, file, or database."""
    logging.info(f"Starting extraction from: {source_path}")
    try:
        # Example: Mocking raw data extraction
        raw_data = [
            {"id": 1, "item": "Widget A", "price": "19.99", "status": "active"},
            {
                "id": 2,
                "item": "Widget B",
                "price": "invalid_price",
                "status": "active",
            },
            {
                "id": 3,
                "item": "Widget C",
                "price": "45.00",
                "status": "inactive",
            },
            {"id": 4, "item": "Widget D", "price": "100.50", "status": "active"},
        ]
        logging.info(f"Successfully extracted {len(raw_data)} records.")
        return raw_data
    except Exception as e:
        logging.error(f"Failed during extraction stage: {e}")
        raise


# -------------------------------------------------------------------
# 3. TRANSFORM STAGE
# -------------------------------------------------------------------
def transform_data(raw_data: list[dict]) -> list[dict]:
    """Cleans, converts data types, and filters records."""
    logging.info("Starting data transformation...")
    cleaned_data = []

    for row in raw_data:
        # Skip inactive items
        if row.get("status") != "active":
            continue

        # Clean and validate numerical data
        try:
            price = float(row["price"])
            cleaned_row = {
                "id": row["id"],
                "item": row["item"].strip().title(),
                "price": price,
                "processed_at": datetime.now().isoformat(),
            }
            cleaned_data.append(cleaned_row)
        except ValueError:
            logging.warning(
                f"Skipping record ID {row.get('id')}: Invalid price output '{row.get('price')}'"
            )

    logging.info(
        f"Transformation complete. Retained {len(cleaned_data)} valid active records."
    )
    return cleaned_data


# -------------------------------------------------------------------
# 4. LOAD STAGE
# -------------------------------------------------------------------
def load_data(data: list[dict], output_path: str) -> None:
    """Saves processed data to a target destination (JSON, CSV, or DB)."""
    logging.info(f"Saving processed data to: {output_path}")
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logging.info("Data load operation successful!")
    except Exception as e:
        logging.error(f"Failed to save data: {e}")
        raise


# -------------------------------------------------------------------
# 5. PIPELINE EXECUTION
# -------------------------------------------------------------------
def run_pipeline():
    logging.info("=== Starting Automated Data Workflow ===")
    try:
        raw_data = extract_data(source_path="api_or_file_source")
        processed_data = transform_data(raw_data)
        load_data(processed_data, output_path="processed_output.json")
        logging.info("=== Workflow Completed Successfully ===")
    except Exception as e:
        logging.critical(f"Pipeline failed catastrophically: {e}")


if __name__ == "__main__":
    run_pipeline()

