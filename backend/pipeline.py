from services.ai_service import run_ai

def run_pipeline(state, prompts, images):

    # STEP 1: Strategy
    state.strategy = run_ai(
        prompts["strategy"],
        state.product_data,
        images
    )

    # STEP 2: Main Prompts
    main = run_ai(
        prompts["main"],
        state.strategy
    )

    # STEP 3: Secondary Prompts
    secondary = run_ai(
        prompts["secondary"],
        state.strategy
    )

    state.main_prompts = main
    state.secondary_prompts = secondary

    # Combine prompts (mock for now)
    state.all_prompts = ["Prompt A", "Prompt B", "Prompt C"]

    # STEP 4: Image Generation (placeholder)
    state.generated_images = [
        {"status": "READY"},
        {"status": "READY"}
    ]

    return state