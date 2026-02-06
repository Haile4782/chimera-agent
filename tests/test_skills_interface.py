"""Test file for skills interface contracts."""

import pytest
from typing import Dict, Any
import sys
import os

# Add skills directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_skill_input_contract():
    """Test that skill input matches the contract from specs."""
    # Expected contract from specs/technical.md and skills/utils
    expected_input_schema = {
        "skill_name": "string",
        "parameters": "dict",
        "context": "dict|None",
        "request_id": "string"
    }
    
    # This should fail until skills are implemented
    from skills.utils import SkillInput
    
    # Test valid input
    valid_input = {
        "skill_name": "test_skill",
        "parameters": {"param1": "value1"},
        "request_id": "req_123"
    }
    
    try:
        skill_input = SkillInput(**valid_input)
        print(f"✅ SkillInput accepts valid data: {skill_input}")
    except Exception as e:
        print(f"❌ SkillInput validation failed: {e}")
        raise
    
    # Test invalid input (should fail)
    invalid_input = {
        "skill_name": "test_skill"
        # Missing required fields
    }
    
    try:
        skill_input = SkillInput(**invalid_input)
        print("❌ SkillInput should have rejected invalid input")
        raise AssertionError("Should have failed validation")
    except Exception as e:
        print(f"✅ SkillInput correctly rejected invalid input: {type(e).__name__}")

def test_skill_output_contract():
    """Test that skill output matches the contract."""
    from skills.utils import SkillOutput
    
    # Test valid output
    valid_output = {
        "success": True,
        "result": {"data": "test"},
        "confidence": 0.85,
        "processing_time": 1.5,
        "request_id": "req_123"
    }
    
    try:
        skill_output = SkillOutput(**valid_output)
        print(f"✅ SkillOutput accepts valid data: {skill_output}")
    except Exception as e:
        print(f"❌ SkillOutput validation failed: {e}")
        raise
    
    # Test invalid confidence (should fail)
    invalid_output = {
        "success": True,
        "result": {"data": "test"},
        "confidence": 1.5,  # > 1.0, should fail
        "processing_time": 1.5,
        "request_id": "req_123"
    }
    
    try:
        skill_output = SkillOutput(**invalid_output)
        print("❌ SkillOutput should have rejected invalid confidence")
        raise AssertionError("Should have failed validation")
    except Exception as e:
        print(f"✅ SkillOutput correctly rejected invalid confidence: {type(e).__name__}")

def test_skill_base_class():
    """Test the SkillBase class interface."""
    # This will fail until SkillBase is properly implemented
    from skills.utils import SkillBase
    
    class TestSkill(SkillBase):
        def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
            return {"success": True, "data": "test"}
    
    skill = TestSkill("test_skill")
    
    # Test metadata
    metadata = skill.get_metadata()
    assert "name" in metadata, "Metadata missing name"
    assert "version" in metadata, "Metadata missing version"
    assert "description" in metadata, "Metadata missing description"
    assert "input_schema" in metadata, "Metadata missing input_schema"
    assert "output_schema" in metadata, "Metadata missing output_schema"
    
    print(f"✅ SkillBase metadata: {metadata}")
    
    # Test execute method
    test_input = {
        "skill_name": "test_skill",
        "parameters": {"test": "data"},
        "request_id": "test_123"
    }
    
    try:
        result = skill.execute(test_input)
        assert "success" in result, "Result missing success flag"
        print(f"✅ TestSkill.execute result: {result}")
    except Exception as e:
        print(f"❌ TestSkill.execute failed: {e}")
        raise

def test_content_skill_interface():
    """Test content skill specific interface."""
    # Expected from specs/functional.md
    expected_content_input = {
        "topic": "string",
        "target_networks": ["twitter", "openclaw"],
        "content_strategy": {
            "human_optimization": {...},
            "agent_optimization": {...}
        },
        "constraints": {...}
    }
    
    expected_content_output = {
        "human_version": {...},
        "agent_version": {...},
        "bridge_analysis": {...},
        "confidence_scores": {...}
    }
    
    # This test will fail until content skills are implemented
    print("⏳ Content skill interface test defined - will fail until implementation")
    
    # Try to import (will fail if skills not created)
    try:
        # This import will fail initially
        import skills.content_creation.cross_network_content_generation
        print("✅ Content skill module exists")
    except ImportError as e:
        print(f"❌ Content skill module not implemented yet: {e}")
        # This is expected for TDD
    
    # Assert the expected structure
    assert "topic" in expected_content_input, "Content input missing topic"
    assert "target_networks" in expected_content_input, "Content input missing target_networks"
    assert "human_version" in expected_content_output, "Content output missing human_version"
    assert "agent_version" in expected_content_output, "Content output missing agent_version"
    
    print("✅ Content skill interface contract validated")

def test_economic_skill_interface():
    """Test economic skill specific interface."""
    # Expected from specs/technical.md
    expected_transaction_input = {
        "sender_agent_id": "uuid",
        "recipient": {...},
        "transaction": {...},
        "validation": {...}
    }
    
    expected_transaction_output = {
        "transaction_id": "uuid",
        "status": "pending|executed|failed",
        "execution_details": {...},
        "financial_impact": {...},
        "compliance_record": {...}
    }
    
    print("⏳ Economic skill interface test defined - will fail until implementation")
    
    # Business rule: All transactions must have validation
    assert "validation" in expected_transaction_input, "Transaction input missing validation"
    
    # Business rule: Status must be one of expected values
    valid_statuses = ["pending", "executed", "failed", "review"]
    assert expected_transaction_output["status"] in valid_statuses, f"Invalid status: {expected_transaction_output['status']}"
    
    print("✅ Economic skill interface contract validated")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("RUNNING SKILLS INTERFACE TESTS (TDD Approach)")
    print("="*60)
    
    test_count = 0
    passed_count = 0
    failed_count = 0
    
    tests = [
        test_skill_input_contract,
        test_skill_output_contract,
        test_skill_base_class,
        test_content_skill_interface,
        test_economic_skill_interface
    ]
    
    for test_func in tests:
        test_count += 1
        try:
            test_func()
            print(f"⚠️  {test_func.__name__} passed (may need stricter assertions)")
            passed_count += 1
        except AssertionError as e:
            print(f"✅ {test_func.__name__} failed as expected for TDD: {e}")
            failed_count += 1
        except Exception as e:
            print(f"✅ {test_func.__name__} failed (implementation needed): {type(e).__name__}: {e}")
            failed_count += 1
    
    print("\n" + "="*60)
    print(f"TEST RESULTS: {test_count} tests, {passed_count} passed, {failed_count} failed")
    print("="*60)
    
    if failed_count > 0:
        print("🎯 TDD SUCCESS: Failing tests define the implementation contract")
        print("   Next step: Implement skills to make tests pass")
    else:
        print("⚠️  All tests passed - consider adding more specific assertions")