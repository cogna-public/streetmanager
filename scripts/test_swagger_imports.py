#!/usr/bin/env python3
"""
Test script to verify that swagger client imports are working correctly.
This script will:
1. Try to import various modules from the swagger client
2. Create instances of some model classes
3. Print success/failure for each test
"""

import sys
from pathlib import Path
import importlib

# Add the src directory to the Python path
src_path = Path(__file__).parent.parent / 'src'
sys.path.append(str(src_path))

def test_import(module_name, class_name=None):
    """Test importing a module or class."""
    try:
        if class_name:
            module = importlib.import_module(module_name)
            getattr(module, class_name)
            print(f"✅ Successfully imported {module_name}.{class_name}")
        else:
            importlib.import_module(module_name)
            print(f"✅ Successfully imported {module_name}")
    except ImportError as e:
        print(f"❌ Failed to import {module_name}{f'.{class_name}' if class_name else ''}: {e}")
    except AttributeError as e:
        print(f"❌ Failed to import {module_name}.{class_name}: {e}")

def test_readme_style_access(module_path_to_swagger_client, api_class_name="DefaultApi"):
    """Test accessing an API class as an attribute of the swagger_client module."""
    try:
        # e.g., module_path_to_swagger_client = "streetmanager.work.swagger_client"
        client_module = importlib.import_module(module_path_to_swagger_client)
        _ = getattr(client_module, api_class_name) # Check if the attribute exists
        print(f"✅ Successfully accessed {api_class_name} via {module_path_to_swagger_client}.{api_class_name} (README style)")
    except ImportError as e:
        print(f"❌ Failed to import {module_path_to_swagger_client} for README-style access: {e}")
    except AttributeError:
        print(f"❌ Failed to access {api_class_name} via {module_path_to_swagger_client}.{api_class_name} (README style)")

def main():
    """Run all import tests."""
    print("Testing swagger client imports...\n")
    
    # Test work API
    test_import("streetmanager.work.swagger_client")
    test_import("streetmanager.work.swagger_client.models.lane_rental_assessment_charge_band", "LaneRentalAssessmentChargeBand")
    test_import("streetmanager.work.swagger_client.models.permit_response", "PermitResponse")
    test_import("streetmanager.work.swagger_client.models.work_response", "WorkResponse")
    test_import("streetmanager.work.swagger_client.models.all_of_permit_lane_rental_assessment_update_request_charge_band", "AllOfPermitLaneRentalAssessmentUpdateRequestChargeBand")
    test_import("streetmanager.work.swagger_client.models.all_of_inspection_summary_response_inspection_outcome", "AllOfInspectionSummaryResponseInspectionOutcome")
    test_import("streetmanager.work.swagger_client.api_client", "ApiClient")
    test_import("streetmanager.work.swagger_client.api.default_api", "DefaultApi")

    # Test geojson API
    test_import("streetmanager.geojson.swagger_client")
    test_import("streetmanager.geojson.swagger_client.models.activity_feature", "ActivityFeature")
    test_import("streetmanager.geojson.swagger_client.api_client", "ApiClient")
    test_import("streetmanager.geojson.swagger_client.api.default_api", "DefaultApi")

    # Test lookup API
    test_import("streetmanager.lookup.swagger_client")
    test_import("streetmanager.lookup.swagger_client.models.street_response", "StreetResponse")
    test_import("streetmanager.lookup.swagger_client.api_client", "ApiClient")
    test_import("streetmanager.lookup.swagger_client.api.default_api", "DefaultApi")

    print("\nTesting README-style access patterns...\n")
    test_readme_style_access("streetmanager.work.swagger_client")
    test_readme_style_access("streetmanager.geojson.swagger_client")
    test_readme_style_access("streetmanager.lookup.swagger_client")

if __name__ == '__main__':
    main() 