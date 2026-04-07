from modern_python import get_data


def test_posts_endpoint(mock_requests_get):
    get_data.api_data(end_point="posts")
    args, _ = mock_requests_get.call_args
    assert "/posts" in args[0]
