from neuroscangen.use_cases.generate_scan import GenerateScan


def test_generate_scan():
    generate_scan = GenerateScan()

    generated_scan = generate_scan()

    assert generated_scan is not None
