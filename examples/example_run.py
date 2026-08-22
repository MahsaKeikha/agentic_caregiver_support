from orchestration.orchestrator import run_workflow


if __name__ == "__main__":
    result = run_workflow(
        {
            "care_recipient_identity_verified": True,
            "caregiver_role_confirmed": True,
            "consent_and_privacy_confirmed": True,
        }
    )
    print(result["governance"])
