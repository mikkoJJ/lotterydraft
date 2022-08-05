from lotterydraft.lottery import do_lottery


def test_lottery(test_data):

    # do several lotteries and verify all of them fit the requirements
    for _ in range(50):
        result = do_lottery(test_data)

        assert result["Martti"] in ["a", "b", "c", "d", "e"]
        assert result["Sauli"] in ["a", "b"]
        assert result["Tarja"] in ["c", "d", "e"]
