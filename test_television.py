from television import Television
import pytest

def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power():
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_channel_up():
    tv = Television()

    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert tv.channel == 1

    tv.channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL


def test_channel_down():
    tv = Television()
    tv.power()

    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL

    tv.channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL


def test_volume_up():
    tv = Television()

    tv.volume_up()
    assert tv.volume == 0

    tv.power()
    tv.volume_up()
    assert tv.volume == 1

    tv.volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME


def test_volume_down():
    tv = Television()
    tv.power()

    tv.volume_down()
    assert tv.volume == 0

    tv.volume = 2
    tv.volume_down()
    assert tv.volume == 1


def test_mute():
    tv = Television()
    tv.power()

    tv.volume_up()
    tv.mute()
    assert tv.volume == 0

    tv.mute()
    assert tv.volume == 1


def test_mute_volume_interaction():
    tv = Television()
    tv.power()

    tv.volume = 2
    tv.mute()  

    tv.volume_down()
    assert tv.volume == 1

    tv.mute()
    tv.volume_up()
    assert tv.volume == 2


def test_mute_when_off():
    tv = Television()

    tv.mute()
    assert tv.volume == 0
    assert tv.muted == False

if __name__ == "__main__":
    pytest.main()