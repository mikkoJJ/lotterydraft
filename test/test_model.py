def test_player_names(test_data):
    assert len(test_data.players) == 3
    assert ["Martti", "Tarja", "Sauli"] == [
        player.name for player in test_data.players
    ]


def test_player_bans(test_data):
    assert ["a", "b"] == test_data.players[1].bans
    assert ["c", "d", "e"] == test_data.players[2].bans


def test_choices(test_data):
    assert ["a", "b", "c", "d", "e"] == test_data.choices
